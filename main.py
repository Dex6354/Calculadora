import streamlit as st

st.set_page_config(page_title="Calculadora", layout="centered")

# Título com fonte menor
st.markdown("<h2 style='text-align: center;'>🧮 Calculadora</h2>", unsafe_allow_html=True)

# Estado da expressão
if "expressao" not in st.session_state:
    st.session_state.expressao = ""

def adicionar(valor):
    st.session_state.expressao += str(valor)

def limpar():
    st.session_state.expressao = ""

def apagar():
    st.session_state.expressao = st.session_state.expressao[:-1]

# Campo de entrada
st.session_state.expressao = st.text_input("", st.session_state.expressao, key="input")

# Resultado automático
try:
    resultado = eval(st.session_state.expressao)
    st.success(f"Resultado: {resultado}")
except:
    st.error("Resultado: Erro")

# Layout dos botões (4 por linha)
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for linha in botoes:
    cols = st.columns(4)
    for i, item in enumerate(linha):
        if cols[i].button(item, use_container_width=True):
            if item == "=":
                try:
                    st.session_state.expressao = str(eval(st.session_state.expressao))
                except:
                    st.session_state.expressao = "Erro"
            else:
                adicionar(item)

# Linha de limpeza/apagar
col1, col2 = st.columns(2)
if col1.button("🧹 Limpar", use_container_width=True):
    limpar()
if col2.button("⌫ Apagar", use_container_width=True):
    apagar()
