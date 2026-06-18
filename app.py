import streamlit as st
from chatbot import responder

st.title("🌎 Chatbot da Copa do Mundo")

pergunta = st.text_input("Faça uma pergunta:")

if st.button("Enviar"):
    if pergunta:
        resposta = responder(pergunta)
        st.write(resposta)