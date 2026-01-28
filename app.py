import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    st.success(f"Result: {result}")