import streamlit as st
import google.generativeai as genai
import os

# Set up the Streamlit app
st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI-Powered Assistant")
st.write("Ask me anything, and I'll generate an AI-powered response!")

# Configure the Gemini AI API
genai.configure(api_key="AIzaSyBibBz7Lg0eTfAbl-_XZCEi_idKMeEREMU")

# Initialize the AI model
model = genai.GenerativeModel("gemini-2.0-flash")

# User input
user_input = st.text_area("Enter your question:", "")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating response..."):
            response = model.generate_content(user_input)
            st.subheader("AI Response:")
            st.write(response.text)
    else:
        st.warning("Please enter a question before generating a response.")

