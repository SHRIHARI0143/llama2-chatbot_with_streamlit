Llama2 Chatbot with Streamlit

This project is a chatbot built using the Llama 2 model and Streamlit, powered by the Ollama API. The chatbot can generate responses based on user input, utilizing the Llama2-7B model.

Features

Uses Llama 2 (7B) for text generation.

Built with Streamlit for an interactive web-based UI.

Runs locally with Ollama as the backend for model inference.

Maintains chat history within a session.

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

Ollama installed and running

Git

VS Code (optional, but recommended)

Setup Instructions

Clone this repository:

git clone https://github.com/SHRIHARI0143/llama2-chatbot_with_streamlit.git
cd llama2-chatbot_with_streamlit

Install dependencies:

pip install -r requirements.txt

Start the Ollama server:

ollama serve

Run the Streamlit app:

streamlit run llama2_chatbot.py

Usage

Start the chatbot UI in a browser.

Type your messages in the input field.

The chatbot will generate responses based on Llama2-7B.

Troubleshooting

Common Issues

ConnectionError: Ensure Ollama is running (ollama serve).

Model not found: Run ollama pull llama2:7b to download the model.

Port 11434 not available: Check if another process is using the port.

Contributing

Feel free to fork the repository and submit pull requests. For major changes, open an issue first to discuss proposed modifications.

License

This project is open-source under the MIT License.

Developed by Shrihari 🚀
