# Import necessary modules
from dotenv import load_dotenv  # Load environment variables from a .env file
import streamlit as st  # Streamlit for building web apps
import os  # OS module to interact with the operating system
import google.generativeai as genai  # Google Generative AI SDK for interacting with the LLM

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key for Google Generative AI from environment variables
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the Generative AI SDK with the retrieved API key
genai.configure(api_key=api_key)

# Define the model to use; 'gemini-pro' is a Google Generative AI model
model = genai.GenerativeModel('gemini-pro') # this for text 

# Function to interact with the Gemini LLM model
def get_gemini_response(question):
    # Use the model to generate content based on the input question
    response = model.generate_content(question)
    return response.text  # Return the text of the response

# Configure the Streamlit app's page
st.set_page_config(page_title='Q&A Demo')

# Add a header to the Streamlit app
st.header('Gemini LLM Application')

# Create a text input box in the Streamlit app
input = st.text_input('input:', key='input')

# Create a button for submitting the question
sumbit = st.button('Ask the question')

# When the button is clicked, fetch the response from the Gemini model
if sumbit:
    response = get_gemini_response(input)  # Call the function with user input
    st.subheader('The response is')  # Display a subheader
    st.write(response)  # Display the model's response
