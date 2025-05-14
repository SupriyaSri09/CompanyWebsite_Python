import streamlit as st
from mail_util import send_email
import  pandas

st.header("Contact Me")

df=pandas.read_csv("topics.csv",sep=",")

with st.form(key="contact_us_form"):
    user_email_Addr = st.text_input("Your Email Address")
    topic_to_discuss=st.selectbox("What topic do you want to discuss",df["topic"])
    user_message = st.text_area("Message")
    thankyou_msg = """\n
        Subject: Python Learning Course
        <h3>Thank you for contacting us. We will get back to you soon123</h3>
        """
    submit_button=st.form_submit_button("Submit")
    if submit_button:
        #Mail to user
        send_email(thankyou_msg,user_email_Addr)

        #Mail to Team
        message = f"""\
    Subject: New Inquiry
    
    from : {user_email_Addr}
    Topic to discuss {topic_to_discuss}
    {user_message}
    """
        send_email(message,"supriya.prakash.ldn@gmail.com")
        st.info("Your email was sent successfully")