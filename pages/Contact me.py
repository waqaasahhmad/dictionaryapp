import streamlit as st
import yagmail

my_email = "waqaasahhmad@gmail.com"
password = "pfoejctnzplhtgwi"
receiver = "waqaasahhmad@gmail.com"


def send_email(sender, password, subject, message,receiver):
    mail = yagmail.SMTP(user=sender, password=password,smtp_ssl=True)
    mail.send(to=receiver,subject=subject, contents=message,)


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)
with col1:
    st.image('photo.png', caption='Waqas Ahmad')
with col2:
    st.title("Waqas Ahmad")
    st.caption(":blue[Python Enthusiast|Data Analyst|Automation Specialist]")
    st.info("Hello! I'm a passionate Python developer who thrives on adding a touch of creativity to every project I "
            "undertake. I believe that coding is not just about solving problems but also about crafting elegant and "
            "innovative solutions.")
with st.form("Contact me"):
    st.header("Contact me")
    email_address = st.text_input("Your Email Address")
    message = st.text_area("Your Enquiry")
    subject = "Email From Dictionary App"
    message = f"{email_address} sent this message {message}"
    submit_button =st.form_submit_button(label="Send Me")
    if submit_button:
        send_email(sender=my_email, password=password, subject=subject, message=message,receiver=receiver)
        st.info("Email was sent successfully")
