# OpenVoice

Pretty simple if you want to test. Install OpenVoice and then drop my voice.py into your project directory. Install argparse datetime and playsound.
#   Text string
python voice.py --text "Enter text string here."
#   Text file
python voice.py --text_file "path/to/file.txt"
#   LMStudio Server
(First, start local inference server.)
python voice.py --lmstudio "Enter Prompt here."
