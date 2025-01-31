import streamlit as st
import requests

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Function to generate responses using Ollama
def generate_response(prompt):
    # Define the payload for the Ollama API
    payload = {
        "model": "llama2:7b",  # Use the Llama2 7B model
        "prompt": prompt,
        "stream": False,  # Set to False to get a single response
    }
    
    # Send the request to the Ollama API
    response = requests.post(OLLAMA_API_URL, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main Streamlit app
def main():
    # Set up the Streamlit app title
    st.title("Llama2 7B Chatbot (Ollama)")
    
    # Initialize session state to store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input field for user prompt
    if prompt := st.chat_input("Type your message..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate a response using Ollama
        response = generate_response(prompt)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)

# Run the Streamlit app
if __name__ == "__main__":
    main()
