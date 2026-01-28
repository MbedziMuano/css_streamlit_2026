import streamlit as st

st.set_page_config(page_title="Real Number Calculator", page_icon="ℝ")

st.title("ℝ Real Number Calculator")
st.write("This calculator works with **all real numbers** (positive, negative, and decimals).")

# Input real numbers
a = st.number_input(
    "Enter first real number (ℝ)",
    value=0.0,
    step=0.000001,
    format="%.12f"
)

b = st.number_input(
    "Enter second real number (ℝ)",
    value=0.0,
    step=0.000001,
    format="%.12f"
)

# Operation selection
operation = st.radio(
    "Select operation",
    ["+", "−", "×", "÷"]
)

# Compute result
if st.button("Calculate"):
    try:
        if operation == "+":
            result = a + b
        elif operation == "−":
            result = a - b
        elif operation == "×":
            result = a * b
        elif operation == "÷":
            if b == 0:
                st.error("Division by zero is undefined in ℝ ❌")
                st.stop()
            result = a / b

        st.success(f"**Result:** {result}")

    except Exception as e:
        st.error(f"Error: {e}")