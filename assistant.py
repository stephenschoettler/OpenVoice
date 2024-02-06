import ears
import brain
import voice

def main_loop():
    context = ""  # Initialize conversation context

    while True:
        print("Listening for a prompt...")
        transcription = ears.record_and_transcribe()
        
        if "exit" in transcription.lower():
            print("Exit command received. Shutting down...")
            break
        
        # Update the context with the new user input
        context += f"\nUser: {transcription}"

        # Generate response using the updated context
        response = brain.generate_response_with_local_ai(transcription, context)

        # Update the context with the AI response
        context += f"\nAI: {response}"

        print(f"AI Response: {response}")
        
        # Vocalize the AI response
        voice.vocalize_response(response)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nAssistant has been stopped.")
