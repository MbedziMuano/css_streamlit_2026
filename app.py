import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

# 🔹 Custom CSS to make buttons close together
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    padding: 0.3em;
    margin: 0.1em 0;
    font-size: 16px;
}
div[data-testid="column"] {
    padding: 0.05rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Scientific Calculator (ℝ)")

# ✅ Safe session state initialization
if "expr" not in st.session_state:
    st.session_state["expr"] = ""

# Display
st.text_input(
    "Display",
    value=st.session_state["expr"],
    disabled=True
)

# Button logic
def press(val):
    if val == "C":
        st.session_state["expr"] = ""
    elif val == "=":
        try:
            expr = st.session_state["expr"]
            expr = expr.replace("×", "*").replace("÷", "/")
            expr = expr.replace("π", "math.pi").replace("e", "math.e")
            st.session_state["expr"] = str(eval(expr))
        except:
            st.session_state["expr"] = "Error"
    elif val == "√":
        st.session_state["expr"] += "math.sqrt("
    elif val == "x²":
        st.session_state["expr"] += "**2"
    elif val == "sin":
        st.session_state["expr"] += "math.sin("
    elif val == "cos":
        st.session_state["expr"] += "math.cos("
    elif val == "tan":
        st.session_state["expr"] += "math.tan("
    elif val == "log":
        st.session_state["expr"] += "math.log10("
    else:
        st.session_state["expr"] += val

# Button layout (compact grid)
buttons = [
    ["sin", "cos", "tan", "log"],
    ["√", "x²", "π", "e"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "×"],
    ["0", ".", "=", "÷"],
    ["C"]
]

for row in buttons:
    cols = st.columns(len(row), gap="small")
    for i, b in enumerate(row):
        if cols[i].button(b):
            press(b)