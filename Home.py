
import google.generativeai as genai
import streamlit as st

# Configure API Key
API_KEY = "AIzaSyBibBz7Lg0eTfAbl-_XZCEi_idKMeEREMU"  # Replace with your valid API key
genai.configure(api_key=API_KEY)

# Select model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI Configuration
st.set_page_config(page_title="AI Assistant", layout="wide")

# App Title & Description
st.title("🚀 AI Assistant - Powered by Google Gemini")
st.markdown("**Your personal AI assistant for chatting, summarization, grammar correction, and code generation!**")

# Sidebar Options
option = st.sidebar.radio("🔹 Choose a Feature", [
    "💬 AI Chatbot",
    "📝 Text Summarization",
    "✍️ Grammar & Writing Assistant",
    "💡 Code Generator & Explainer",
    "📖 Multi-Context Dictionary"
])

# User Input Field
user_input = st.text_area("📝 Enter your text or question:", height=150)

# Creativity Level (Slider)
temperature = st.sidebar.slider("🎭 Creativity Level", 0, 10, 5)

# Process input based on selected feature
if st.button("✨ Generate Response", use_container_width=True):
    with st.spinner("⏳ Generating response..."):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter some text before generating a response.")
        else:
            # Define prompt based on selected option
            prompt = ""

            if option == "💬 AI Chatbot":
                prompt = user_input  # Direct chat mode

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
            try:
                response = model.generate_content(
                    prompt,
                    generation_config={"temperature": temperature / 10}  # Adjust creativity
                )

                # Display output
                if response and hasattr(response, "text"):
                    st.success("✅ Response Generated:")
                    st.write(response.text)
                else:
                    st.error("❌ Failed to generate a response. Please try again.")

            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
