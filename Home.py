import streamlit as st
import google.generativeai as genai

# Set Streamlit Page Config
st.set_page_config(page_title='ChatDictionary', layout='wide')

# API Key Configuration
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

# App Title and Subtitle
st.title("Chat Dictionary")
st.subheader("Unleash the potential of Large Language Models")

# User Inputs
word = st.text_input("Type the word")
options = ['General', 'Law', 'Medicine', 'Science', 'Technology', 'Business',
           'Finance', 'Sports', 'Arts', 'Literature', 'History', 'Philosophy']
context = st.selectbox("Choose The Context", options=options)
temperature = st.slider('How much creative you want me to be', min_value=0, max_value=10, 
                        help="Higher the creativity, the less exact answer or more variation in the result")

button = st.button(label="Search", use_container_width=True)

# Prompt for AI
prompt = (f"Give me the meaning of the word '{word}' in the context of {context}, along with its synonyms, antonyms, "
          f"and use cases. Also, provide a short essay or story where the word is used.")

if button:
    with st.spinner("Searching......"):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt, generation_config={
                "temperature": temperature / 10,
                "max_output_tokens": 1000
            })
            
            if response and response.text:
                st.write(response.text)
            else:
                st.info("Something went wrong! Try another word.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
