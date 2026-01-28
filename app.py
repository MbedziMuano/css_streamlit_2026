import streamlit as st

# Title
st.title("Physist")

# Inputs
name = st.text_input("Muano Mbedzi")
age = st.number_input("--", min_value=0, max_value=120)
bio = st.text_area("Physist from the univerity of venda")

# Display
st.header("Profile Overview")
if name:
    st.write(f"**Name:** {name}")
if age:
    st.write(f"**Age:** {age}")
if bio:
    st.write(f"**Bio:** {bio}")