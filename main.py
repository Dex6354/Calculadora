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

# Estilo CSS para a grade
st.markdown("""
    <style>
    .calculator-grid {
        display: grid;
        grid-template-columns: repeat(4, 80px);
        gap: 5px;
        justify-content: center;
        padding: 10px;
        max-width: 340px;
        margin: 0 auto;
    }
    .calculator-grid button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        border-radius: 10px;
        border: none;
        background-color: #f0f0f0;
        cursor: pointer;
    }
    .calculator-grid button:hover {
        background-color: #e0e0e0;
    }
    .zero-button {
        grid-column: span 2;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Grade de botões
botoes = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Renderizar a grade
with st.container():
    st.markdown('<div class="calculator-grid">', unsafe_allow_html=True)
    for linha in botoes:
        for btn in linha:
            if btn == "":
                continue  # Ignora botões vazios
            # Aplica classe especial para o botão "0"
            button_class = "zero-button" if btn == "0" else ""
            button_html = f'''
                <form method="post">
                    <button type="submit" name="btn" value="{btn}" class="{button_class}">{btn}</button>
                </form>
            '''
            st.markdown(button_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Lógica dos botões
if "btn" in st.form_submit_button:
    btn = st.form_submit_button["btn"]
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
