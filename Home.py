import pprint
import google.generativeai as palm
import streamlit as st

st.set_page_config(page_title='ChatDictionary', layout='wide')

API_KEY = "AIzaSyC0vpxE7ypq10Qf3NbiaQLgdOvvWfK34CA"


st.title("Chat Dictionary")
st.subheader("Unleash the potential of Large Language Models")
word = st.text_input("Type the word")
options = ['General', 'Law', 'Medicine', 'Science', 'Technology', 'Business',
           'Finance', 'Sports', 'Arts', 'Literature', 'History', 'Philosophy']
context = st.selectbox("Choose The Context", options=options)
temperature = st.slider('How much creative you want me to be', min_value=0, max_value=10, help="Higher the creativity "
                                                                                               "The Less Exact answer"
                                                                                               " or more variation in "
                                                                                               "the result ")

button = st.button(label="Search",use_container_width=True)
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://www.facebook.com/waqaasahhmad/" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href=""> by Waqas Ahmad</a></p>
</div>

</div>
"""
st.markdown(ft, unsafe_allow_html=True)

prompt = (f"Give me the meaning of the word {word} in the context of {context}, along with its synonyms, antonyms, "
          f"and use cases also give a short essay or story wherein the word is used")


if button:
    with st.spinner("Searching......"):
        palm.configure(api_key=API_KEY)
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=temperature / 10,
            # The maximum length of the response
            max_output_tokens=1000,
        )
        if completion.result is None:
            st.info("Somethings wrong! Try another word.")
        else:
            st.write(completion.result)
