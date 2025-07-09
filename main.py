import streamlit as st

st.set_page_config(page_title="Calculadora", layout="centered")

st.markdown("<h3 style='text-align: center;'>Calculadora</h3>", unsafe_allow_html=True)

st.text_input(" ", label_visibility="collapsed", placeholder="Expressão")

# 🔧 CSS + HTML layout com grid correto
html = """
<style>
    .calc-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 20px;
    }
    .calc-grid button {
        padding: 20px;
        font-size: 22px;
        border: none;
        border-radius: 10px;
        background-color: #444;
        color: white;
        width: 100%;
    }
</style>

<div class="calc-grid">
    <button>C</button>
    <button>⌫</button>
    <button>%</button>
    <button>/</button>
    <button>7</button>
    <button>8</button>
    <button>9</button>
    <button>*</button>
    <button>4</button>
    <button>5</button>
    <button>6</button>
    <button>-</button>
    <button>1</button>
    <button>2</button>
    <button>3</button>
    <button>+</button>
    <button>0</button>
    <button>.</button>
    <button>=</button>
    <button></button>
</div>
"""

# 👇 renderiza com HTML liberado
st.markdown(html, unsafe_allow_html=True)
