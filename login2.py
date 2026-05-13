import streamlit as st
from datetime import datetime

USUARIO = "admin"
SENHA = "9999"

def tela_login():
    st.markdown(
        """
        <style>

        .stApp {
            background-color: #121212;
        }

        /* TITULOS */
        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }

        /* TEXTOS */
        p, label, span {
            color: white !important;
        }

        /* INPUTS */
        .stTextInput > div > div > input {
            background-color: #1e1e1e;
            color: white;
            border-radius: 10px;
            border: 1px solid #00c853;
        }

        /* PLACEHOLDER */
        .stTextInput input::placeholder {
            color: #bbbbbb;
        }

        /* BOTAO */
        .stButton > button {
            background-color: #00c853;
            color: white;
            border: none;
            border-radius: 10px;
            height: 45px;
            width: 100%;
            font-size: 16px;
            font-weight: bold;
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
