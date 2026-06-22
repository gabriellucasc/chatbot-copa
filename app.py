import streamlit as st
from chatbot import responder
import base64

def adicionar_background(imagem):
    with open(imagem, "rb") as arquivo:
        encoded = base64.b64encode(arquivo.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            background: rgba(0, 0, 0, 0.55);
            padding: 2rem;
            border-radius: 20px;
            margin-top: 2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

adicionar_background("professor.png")

st.title("🌎 Chatbot da Copa do Mundo")
st.caption("Comando técnico oficial do Hexa 2026 🇧🇷⚽")

pergunta = st.text_input("Faça uma pergunta:")

if st.button("Enviar"):
    if pergunta:
        resposta = responder(pergunta)
        st.write(resposta)