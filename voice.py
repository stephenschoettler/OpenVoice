import os
import torch
import argparse
from datetime import datetime
from openai import OpenAI
import se_extractor  # Import the se_extractor module
from api import BaseSpeakerTTS, ToneColorConverter

# Initialization for OpenVoice AI
ckpt_base = 'checkpoints/base_speakers/EN'
ckpt_converter = 'checkpoints/converter'
device="cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs'

# Argument parser setup
parser = argparse.ArgumentParser(description='TTS with optional LMStudio integration.')
parser.add_argument('--text', type=str, help='Text to convert to speech.', default=None)
parser.add_argument('--text_file', type=str, help='File path of text to convert to speech.', default=None)
parser.add_argument('--lmstudio', type=str, help='Prompt for LMStudio.', default=None)

# Parse arguments
args = parser.parse_args()

# Decide source of text
if args.lmstudio:
    # LMStudio setup and text generation based on the prompt
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    completion = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": args.lmstudio}
        ],
        temperature=0.7,
    )
    input_text = completion.choices[0].message.content
elif args.text:
    input_text = args.text
elif args.text_file:
    with open(args.text_file, 'r') as file:
        input_text = file.read()
else:
    raise ValueError("No input text provided. Use --text, --text_file, or --lmstudio.")

# Ensure input_text is a string
if not isinstance(input_text, str):
    input_text = str(input_text)

# OpenVoice AI setup
base_speaker_tts = BaseSpeakerTTS(f'{ckpt_base}/config.json', device=device)
base_speaker_tts.load_ckpt(f'{ckpt_base}/checkpoint.pth')

tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)

# Obtain Tone Color Embedding for reference speaker
source_se = torch.load(f'{ckpt_base}/en_default_se.pth').to(device)

reference_speaker = 'resources/example_reference.mp3'
target_se, audio_name = se_extractor.get_se(reference_speaker, tone_color_converter, target_dir='processed', vad=True)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
save_path = f'{output_dir}/output_{timestamp}.wav'

# Run the base speaker tts

# Hardcoded text (add text arg to basespeakertts.tts() to change)
#text = "Hi! This is a demo of the open-source voice conversion system."

src_path = f'{output_dir}/tmp.wav'
base_speaker_tts.tts(input_text, src_path, speaker='default', language='English', speed=1.0)

# Run the tone color converter
encode_message = "@MyShell"
tone_color_converter.convert(
    audio_src_path=src_path, 
    src_se=source_se, 
    tgt_se=target_se, 
    output_path=save_path,
    message=encode_message)
