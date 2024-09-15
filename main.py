import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")  # Retrieve API key from .env file
genai.configure(api_key=api_key)

# Configure our model to Gemini Flash 1.5
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat()

# Function to get a response from Google Generative AI
def get_response(question):
    response = chat.send_message(question, stream=False)  # stream=False for simple output
    return response  
# Streamlit app
st.title("Chat with Gemini AI")
st.subheader("Ask your doubts and get answers!")

# Getting user input
question = st.chat_input("ask the question", key="input")

# Sending the question to get_response function
if question:
    response_from_function = get_response(question)  # Pass the question correctly
    for chunk in response_from_function:
        st.write(chunk.text)

    
