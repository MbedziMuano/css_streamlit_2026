import streamlit as st

# Title
st.title("👤 Short Profile App")

# Inputs
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120)
bio = st.text_area("Short Bio")

# Display
st.header("Profile Overview")
if name:
    st.write(f"**Name:** {name}")
if age:
    st.write(f"**Age:** {age}")
if bio:
    st.write(f"**Bio:** {bio}")