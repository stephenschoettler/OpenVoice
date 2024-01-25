import argparse
import subprocess
from openai import OpenAI  # Import the OpenAI library

def generate_response_with_local_ai(input_text):
    """
    Generates a response using a local AI setup (LM Studio) through the OpenAI library.
    Adjust the base_url and other parameters as needed for your local setup.
    """
    # Initialize the OpenAI client with the local server's URL
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    
    # Create a completion request with the input text
    completion = client.chat.completions.create(
        model="local-model",  # This field is currently unused but required
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        temperature=0.7,
    )

    # Extract and return the generated message from the completion
    return completion.choices[0].message.content  # Adjust based on the actual response structure

def main():
    parser = argparse.ArgumentParser(description="Process transcribed text and generate a response using a local AI setup.")
    parser.add_argument("input_text", type=str, help="Transcribed text to process.")

    args = parser.parse_args()

    # Generate a response based on the input text using the local AI setup
    generated_response = generate_response_with_local_ai(args.input_text)
    print(f"Generated Response: {generated_response}")
    
    # Save the generated response to a file for voice.py to read
    response_file_path = "ai_response.txt"
    with open(response_file_path, "w") as file:
        file.write(generated_response)

    # Call voice.py to synthesize and possibly play the generated response
    subprocess.run(["python", "voice.py", "--response_file", response_file_path])

if __name__ == "__main__":
    main()
