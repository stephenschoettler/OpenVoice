import argparse
import subprocess
from openai import OpenAI  # Adjust this import for your setup

def generate_response_with_local_ai(input_text, context=""):
    """
    Generates a response using a local AI setup, incorporating provided context.
    
    Parameters:
    - input_text: The latest user input text to respond to.
    - context: (Optional) A string containing the accumulated conversation context.
    """
    with open('system_message.txt', 'r') as file:
        system_message = file.read().strip()

    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    
    # Example adjustment to include context; adapt based on your model's requirements:
    full_prompt = f"{context}\n{input_text}" if context else input_text
    
    completion = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
    )

    return completion.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Generate a response using a local AI setup, optionally incorporating context.")
    parser.add_argument("input_text", type=str, help="Transcribed text to process.")
    parser.add_argument("--context", type=str, default="", help="Accumulated conversation context.")

    args = parser.parse_args()

    generated_response = generate_response_with_local_ai(args.input_text, args.context)
    print(f"Generated Response: {generated_response}")
    
    response_file_path = "ai_response.txt"
    with open(response_file_path, "w") as file:
        file.write(generated_response)

    subprocess.run(["python", "voice.py", "--response_file", response_file_path])

if __name__ == "__main__":
    main()
