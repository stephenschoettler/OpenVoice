# Import the necessary modules
import ears  # Make sure ears.py is in the same directory
import brain  # Similarly, ensure brain.py is correctly placed and accessible
import voice  # Ensure voice.py is also correctly placed and accessible

def main_loop():
    while True:
        print("Recording... Press the SPACEBAR to stop.")
        transcription = ears.record_and_transcribe()  # Call the function from ears.py
        
        if "exit" in transcription.lower():
            print("Exit command received. Shutting down...")
            break
        
        print(f"Transcription: {transcription}")
        response = brain.generate_response_with_local_ai(transcription)  # Call the function from brain.py
        print(f"AI Response: {response}")
        
        voice.vocalize_response(response)  # Call the function from voice.py

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nAssistant has been stopped.")
