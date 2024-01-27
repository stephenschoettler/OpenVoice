import pyaudio
import wave
import whisper
import subprocess
import os

# Define the basic parameters for recording
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1              # Mono audio
RATE = 44100              # Sampling rate
CHUNK = 1024              # Frames per buffer
RECORD_SECONDS = 5        # Duration to record
WAVE_OUTPUT_FILENAME = "recordedFile.wav"  # Output filename

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream for recording
stream = p.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

print("Recording...")
frames = []

# Record data for RECORD_SECONDS
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

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

# Now, transcribe the recording with Whisper
print("Transcribing...")
model = whisper.load_model("tiny.en")
result = model.transcribe(WAVE_OUTPUT_FILENAME)
transcription = result["text"]
print("Transcription:", transcription)

# Optionally, save the transcription for brain.py to process
with open("transcription.txt", "w") as file:
    file.write(transcription)

# Assuming brain.py takes the path to the transcription file as an argument
# Adjust the path to brain.py as necessary
subprocess.run(["python", "brain.py", transcription])


# Clean up the recorded file if no longer needed
os.remove(WAVE_OUTPUT_FILENAME)
