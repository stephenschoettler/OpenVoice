# Open_Assistant

## Overview
Open_Assistant is an innovative voice assistant that leverages the power of open-source projects to provide an array of functionalities, from answering queries to managing smart devices (future feature), all through voice commands. It is designed to enhance user interaction with technology by offering a customizable and modular voice-controlled interface. The assistant is split into three main scripts for modularity and ease of development:
- **Ears**: Utilizes Whisper from OpenAI for voice recognition.
- **Brain**: Leverages LM Studio for processing natural language and generating responses.
- **Voice**: Uses OpenVoice for generating spoken responses.

## Features
- Advanced voice recognition and processing.
- Modular architecture for easy customization and expansion.
- Integration capabilities with smart home technologies.
- Expandable with user-created modules for various tasks.

## Installation

### Prerequisites
- Python 3.6 or newer.
- pip for Python package management.

### Steps

1. **Install OpenVoice**:
   - Follow the installation guide for OpenVoice from its official repository or documentation page. This typically involves cloning the OpenVoice repository and installing its dependencies.

2. **Integrate Open_Assistant**:
   - Clone this repository:
     ```
     git clone https://github.com/stephenschoettler/Open_Assistant.git
     ```
   - Navigate to the Open_Assistant directory:
     ```
     cd Open_Assistant
     ```
   - Install required Python dependencies. It's important to do this after setting up OpenVoice, as there might be dependencies that are common or that need specific versions:
     ```
     pip install -r requirements.txt
     ```

## Usage

To launch Open_Assistant, execute the main script from the terminal:
     ```
     python assistant.py
     ```

     
This command activates the assistant, ready to receive and process your voice commands.
## Contributing

We welcome contributions to Open_Assistant! Whether it's bug reports, feature requests, or code contributions, your help is invaluable.

To contribute:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- A shoutout to the OpenVoice project for providing the foundation for voice synthesis.
- Thanks to OpenAI's Whisper for enabling robust voice recognition.
- Appreciation for LM Studio for powering our natural language understanding and processing.
- Thank you to all the contributors who have made Open_Assistant better.

