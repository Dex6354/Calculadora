import streamlit as st

st.set_page_config(page_title="Calculadora", layout="centered")

# Título pequeno
st.markdown("<h2 style='text-align: center;'>Calculadora</h2>", unsafe_allow_html=True)

# Expressão persistente
if "expressao" not in st.session_state:
    st.session_state.expressao = ""

# Funções
def adicionar(valor):
    st.session_state.expressao += str(valor)

def limpar():
    st.session_state.expressao = ""

def apagar():
    st.session_state.expressao = st.session_state.expressao[:-1]

# Campo de entrada
st.text_input(" ", value=st.session_state.expressao, key="input", label_visibility="collapsed")

# Resultado
try:
    resultado = eval(st.session_state.expressao)
    st.markdown(f"<h3 style='text-align: center;'>Resultado: {resultado}</h3>", unsafe_allow_html=True)
except:
    st.markdown("<h3 style='text-align: center;'>Resultado: Erro</h3>", unsafe_allow_html=True)

# Grade de botões
botoes = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Estilo para botões
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

for linha in botoes:
    if linha[0] == "0":  # Linha com o botão "0" (layout especial)
        cols = st.columns([2, 1, 1])  # "0" ocupa 2 espaços, "." e "=" ocupam 1 cada
        for i, btn in enumerate(linha):
            if cols[i].button(btn, key=f"btn_{btn}", use_container_width=True):
                if btn == "=":
                    try:
                        st.session_state.expressao = str(eval(st.session_state.expressao))
                    except:
                        st.session_state.expressao = "Erro"
                else:
                    adicionar(btn)
    else:
        cols = st.columns(4)  # 4 colunas de tamanhos iguais para as outras linhas
        for i, btn in enumerate(linha):
            if cols[i].button(btn, key=f"btn_{btn}", use_container_width=True):
                if btn == "C":
                    limpar()
                elif btn == "⌫":
                    apagar()
                elif btn == "=":
                    try:
                        st.session_state.expressao = str(eval(st.session_state.expressao))
                    except:
                        st.session_state.expressao = "Erro"
                else:
                    adicionar(btn)
