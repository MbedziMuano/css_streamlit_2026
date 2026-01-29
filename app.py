import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator (All Real Numbers ℝ)")

# ✅ SAFE initialization (dictionary style)
if "current" not in st.session_state:
    st.session_state["current"] = ""

# Display
st.text_input(
    "Display",
    value=st.session_state["current"],
    disabled=True
)

# Button logic
def press(value):
    if value == "C":
        st.session_state["current"] = ""
    elif value == "=":
        try:
            expr = (
                st.session_state["current"]
                .replace("×", "*")
                .replace("÷", "/")
            )
            st.session_state["current"] = str(eval(expr))
        except:
            st.session_state["current"] = "Error"
    else:
        st.session_state["current"] += value

# Layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "×"],
    ["0", ".", "=", "÷"],
    ["C"]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, b in enumerate(row):
        if cols[i].button(b):
            press(b)