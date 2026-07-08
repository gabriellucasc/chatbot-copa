import streamlit as st
from chatbot import responder
import base64
import os

def adicionar_background(imagem):
    with open(imagem, "rb") as arquivo:
        encoded = base64.b64encode(arquivo.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(5, 10, 20, 0.82), rgba(5, 10, 20, 0.82)),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            max-width: 900px;
            background: rgba(10, 15, 25, 0.78);
            padding: 2.2rem;
            border-radius: 18px;
            margin-top: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}

        h1 {{
            font-size: 2.1rem !important;
            font-weight: 700 !important;
            color: #f5f5f5 !important;
            margin-bottom: 0.2rem !important;
        }}

        .stCaption {{
            color: #c9c9c9 !important;
            font-size: 0.95rem !important;
        }}

        .stButton > button {{
            background-color: rgba(255, 255, 255, 0.08);
            color: #f5f5f5;
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 10px;
            padding: 0.4rem 0.8rem;
            font-weight: 500;
        }}

        .stButton > button:hover {{
            background-color: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.28);
            color: #ffffff;
        }}

        div[data-testid="stChatMessage"] {{
            background-color: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 0.6rem;
            margin-bottom: 0.8rem;
        }}

        div[data-testid="stChatInput"] {{
            background-color: rgba(10, 15, 25, 0.95);
        }}

        .footer-text {{
            margin-top: 1.5rem;
            color: #a8a8a8;
            font-size: 0.82rem;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="Chatbot da Copa do Mundo",
    page_icon="⚽",
    layout="centered"
)


if os.path.exists("professor.png"):
    adicionar_background("professor.png")


st.title("Chatbot da Copa do Mundo")
st.caption("Sistema conversacional com integração entre IA generativa e dados esportivos.")


if "historico" not in st.session_state:
    st.session_state.historico = []


col1, col2 = st.columns([4, 1])

with col2:
    limpar = st.button("Limpar")

if limpar:
    st.session_state.historico = []
    st.rerun()


for mensagem in st.session_state.historico:
    if mensagem["papel"] == "user":
        avatar = "👤"
    else:
        avatar = "⚽"

    with st.chat_message(mensagem["papel"], avatar=avatar):
        st.write(mensagem["conteudo"])


pergunta = st.chat_input("Digite sua pergunta sobre a Copa do Mundo...")


if pergunta:
    with st.chat_message("user", avatar="👤"):
        st.write(pergunta)

    historico_anterior = st.session_state.historico.copy()

    st.session_state.historico.append({
        "papel": "user",
        "conteudo": pergunta
    })

    with st.chat_message("assistant", avatar="⚽"):
        with st.spinner("Consultando dados e gerando resposta..."):
            resposta = responder(pergunta, historico_anterior)
            st.write(resposta)

    st.session_state.historico.append({
        "papel": "assistant",
        "conteudo": resposta
    })


st.markdown(
    """
    <div class="footer-text">
        Projeto acadêmico desenvolvido com Streamlit, API Football-Data e IA generativa.
    </div>
    """,
    unsafe_allow_html=True
)