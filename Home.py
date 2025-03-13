import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="ChatDictionary", layout="wide")

API_KEY = "AIzaSyBibBz7Lg0eTfAbl-_XZCEi_idKMeEREMU"  # Replace with your actual API key

# Configure API key
genai.configure(api_key=API_KEY)

# List available models
models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
model_name = models[0]  # Select the first available model

st.title("Chat Dictionary")
st.subheader("Unleash the potential of Large Language Models")

word = st.text_input("Type the word")
options = ["General", "Law", "Medicine", "Science", "Technology", "Business", 
           "Finance", "Sports", "Arts", "Literature", "History", "Philosophy"]
context = st.selectbox("Choose The Context", options=options)
temperature = st.slider("How much creative you want me to be", min_value=0, max_value=10)

button = st.button(label="Search", use_container_width=True)

prompt = (f"Give me the meaning of the word '{word}' in the context of '{context}', along with its synonyms, antonyms, "
          f"and use cases. Also, give a short essay or story using the word.")

if button:
    with st.spinner("Searching......"):
        try:
            response = genai.generate_content(model=model_name, prompt=prompt, temperature=temperature / 10)
            if response and hasattr(response, "text"):
                st.write(response.text)
            else:
                st.info("Something went wrong! Try another word.")
        except Exception as e:
            st.error(f"Error: {e}")
