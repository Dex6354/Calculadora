import streamlit as st

st.set_page_config(page_title="Calculadora", layout="centered")

st.title("🧮 Calculadora")

# Estado persistente para a expressão
if "expressao" not in st.session_state:
    st.session_state.expressao = ""

# Função para atualizar a expressão
def adicionar(valor):
    st.session_state.expressao += str(valor)

# Função para limpar
def limpar():
    st.session_state.expressao = ""

# Função para apagar último caractere
def apagar():
    st.session_state.expressao = st.session_state.expressao[:-1]

# Entrada da expressão (editável)
st.session_state.expressao = st.text_input("Expressão", st.session_state.expressao, key="input", label_visibility="collapsed")

# Resultado automático
try:
    resultado = eval(st.session_state.expressao)
    st.markdown(f"### Resultado: `{resultado}`")
except:
    st.markdown("### Resultado: `Erro`")

# Layout dos botões
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for linha in botoes:
    cols = st.columns(len(linha))
    for i, item in enumerate(linha):
        if cols[i].button(item):
            if item == "=":
                try:
                    st.session_state.expressao = str(eval(st.session_state.expressao))
                except:
                    st.session_state.expressao = "Erro"
            else:
                adicionar(item)

# Linha de limpar e apagar
col1, col2 = st.columns(2)
if col1.button("🧹 Limpar"):
    limpar()
if col2.button("⌫ Apagar"):
    apagar()
