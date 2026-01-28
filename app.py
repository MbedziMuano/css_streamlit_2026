import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0, format="%.10f")
num2 = st.number_input("Enter second number", value=0.0, format="%.10f")

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed ❌")
            result = None

    if result is not None:
        st.success(f"Result: **{result}**")