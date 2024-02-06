import pyaudio
import wave
import keyboard  # Make sure to import the keyboard library
import whisper
import os

def record_and_transcribe():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    WAVE_OUTPUT_FILENAME = "temp_recorded.wav"

    # Record the audio 
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    # Create an empty list to store the recorded data
    frames = []

    # Record data until spacebar is pressed
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('space'):  # Check if spacebar is pressed
            print("Stopped")
            break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Transcribe the recording
    print("Transcribing...")
    model = whisper.load_model("tiny")
    result = model.transcribe(WAVE_OUTPUT_FILENAME)
    transcription = result["text"]

    # Clean up the recorded file
    os.remove(WAVE_OUTPUT_FILENAME)

    return transcription
