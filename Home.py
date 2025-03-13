import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBibBz7Lg0eTfAbl-_XZCEi_idKMeEREMU")
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Your prompt here")
if response and hasattr(response, "text"):
    print(response.text)
else:
    print("No response from AI.")

