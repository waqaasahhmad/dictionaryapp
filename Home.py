import google.generativeai as genai
import streamlit as st

# Configure API Key
API_KEY = "AIzaSyBibBz7Lg0eTfAbl-_XZCEi_idKMeEREMU"  # Replace with your API key
genai.configure(api_key=API_KEY)

# Select model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🚀 AI Assistant - Powered by Google Gemini")
st.subheader("Your personal AI-powered assistant for various tasks!")

# Sidebar options
option = st.sidebar.radio("Select a feature", [
    "💬 AI Chatbot",
    "📝 Text Summarization",
    "✍️ Grammar & Writing Assistant",
    "💡 Code Generator & Explainer",
    "📖 Multi-Context Dictionary"
])

# User input field
user_input = st.text_area("Enter your text or question:", height=150)

# Slider for creativity level
temperature = st.sidebar.slider("Creativity Level", 0, 10, 5)

# Process input based on selected feature
if st.button("Generate Response", use_container_width=True):
    with st.spinner("Generating response..."):
        if user_input.strip() == "":
            st.warning("Please enter text before generating a response!")
        else:
            prompt = ""

            if option == "💬 AI Chatbot":
                prompt = user_input  # Direct chat

            elif option == "📝 Text Summarization":
                prompt = f"Summarize the following text in simple points:\n\n{user_input}"

            elif option == "✍️ Grammar & Writing Assistant":
                prompt = f"Improve the clarity, grammar, and readability of the following text:\n\n{user_input}"

            elif option == "💡 Code Generator & Explainer":
                prompt = f"Generate Python code for the following task and explain how it works:\n\n{user_input}"

            elif option == "📖 Multi-Context Dictionary":
                prompt = (f"Give me the meaning of the word '{user_input}', along with its synonyms, antonyms, "
                          f"and example sentences. Also, provide an essay or story where the word is used.")

            # Get AI response
            response = model.generate_content(prompt, temperature=temperature / 10)

            # Display output
            if response and hasattr(response, "text"):
                st.success("✅ Here is the response:")
                st.write(response.text)
            else:
                st.error("❌ Failed to generate a response. Please try again.")

