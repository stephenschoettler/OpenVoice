import os
import torch
from playsound import playsound
from api import BaseSpeakerTTS, ToneColorConverter
import se_extractor

def vocalize_response(response_text, output_dir='outputs', response_file_path='ai_response.txt'):
    """
    Converts the response text into speech using advanced TTS and tone color conversion, then plays it.
    
    Parameters:
    - response_text: The text to be converted to speech.
    - output_dir: Directory to save output audio files.
    - response_file_path: Path for intermediate text storage (if needed).
    """

    # Define paths and settings
    ckpt_base = 'checkpoints/base_speakers/EN'
    ckpt_converter = 'checkpoints/converter'
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Initialize TTS and tone color converter
    base_speaker_tts = BaseSpeakerTTS(f'{ckpt_base}/config.json', device=device)
    base_speaker_tts.load_ckpt(f'{ckpt_base}/checkpoint.pth')

    tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
    tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

    os.makedirs(output_dir, exist_ok=True)
    source_se = torch.load(f'{ckpt_base}/en_default_se.pth').to(device)

    # Extract the target speaker embedding
    reference_speaker = 'resources/example_reference.mp3'
    target_se, audio_name = se_extractor.get_se(reference_speaker, tone_color_converter, target_dir='processed', vad=True)

    # Prepare the output path
    save_path = f'{output_dir}/output_en_default.wav'

    # Convert text to speech using the base speaker TTS
    src_path = f'{output_dir}/tmp.wav'
    base_speaker_tts.tts(response_text, src_path, speaker='default', language='English', speed=1.0)

    # Apply tone color conversion
    encode_message = "@MyShell"
    tone_color_converter.convert(
        audio_src_path=src_path, 
        src_se=source_se, 
        tgt_se=target_se, 
        output_path=save_path,
        message=encode_message)

    print(f"Audio generated successfully: {save_path}")

    # Play the converted audio
    playsound(save_path)

# Example usage removed for integration purposes
