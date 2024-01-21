import os
import torch
from api import BaseSpeakerTTS, ToneColorConverter
import se_extractor

# Initialization
ckpt_base = 'checkpoints/base_speakers/EN'  # Path to the base speaker model
ckpt_converter = 'checkpoints/converter'    # Path to the tone color converter
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize the BaseSpeakerTTS and ToneColorConverter
base_speaker_tts = BaseSpeakerTTS(f'{ckpt_base}/config.json', device=device)
base_speaker_tts.load_ckpt(f'{ckpt_base}/checkpoint.pth')
tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

# Reference speaker audio for voice cloning
reference_speaker_audio = 'elon.mp3'
target_se, _ = se_extractor.get_se(reference_speaker_audio, tone_color_converter, vad=True)

# Debug: Print the shape and some values of the target_se embedding
print("Shape of target_se embedding:", target_se.shape)
print("Some values of target_se embedding:", target_se[:5])  # Adjust index range as needed

# Hardcoded text to be converted to speech
text_to_speak = "Hi, I'm Elon Musk, an entrepreneur and business magnate known for founding SpaceX and co-founding Tesla Motors, with a passion for renewable energy and space exploration."

# File paths for saving the output
src_path = f'{output_dir}/tmp_output_speech.wav'
final_path = f'{output_dir}/final_output_speech.wav'

# Generate speech from text using the base speaker
base_speaker_tts.tts(text_to_speak, src_path, speaker='default', language='English', speed=1.0)

# Debug: Print a message before and after conversion
print("Starting tone color conversion...")
tone_color_converter.convert(audio_src_path=src_path, src_se=target_se, tgt_se=target_se, output_path=final_path)
print("Tone color conversion completed.")

print(f"Speech generated with cloned voice and saved to {final_path}")
