import streamlit as st
import re 

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.header("Welcome password strength meter 🔏")
st.markdown("""  
##### This tool helps you evaluate the strength of your password based on various criteria.""")

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    if len(password) > 8:
        score += 1
    else:
        feedback.append("Length of password should be at least 8 characters")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase and one lowercase letter")
    if re.search(r'\d', password):
        score += 1
    else:   
        feedback.append("Password should contain at least one digit")
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:   
        feedback.append("Password should contain at least one special character")
    if score == 4:
        st.success("Password is very strong")
        st.balloons()
    elif  score == 3:
        st.info("Password is medium")
    elif score <= 2:
        st.warning("Password is weak")

    if feedback:
        st.markdown("#### Improvement suggestions:")
        for i, tip in enumerate(feedback, start=1):  # Add numbering using enumerate
            st.markdown(f"{i}. {tip}")  # Format each suggestion with a number
else:
    st.warning("Please enter a password to check its strength.")



