import streamlit as st
from datetime import datetime

USUARIO = "admin"
SENHA = "9999"

def tela_login():
    st.markdown(
        """
        <style>

        .stApp{
        background-color: #121212;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.title("Login")
    agora = datetime.now()
    data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")
    st.caption(f"Data e hora atual: {data_hora}")
    
    st.write("Faça login para acessar o sistema.")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == USUARIO and senha == SENHA:
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
