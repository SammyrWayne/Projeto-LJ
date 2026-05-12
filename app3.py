import streamlit as st
import csv
import os
import pandas as pd
import plotly.express as px

from validate_docbr import CPF
from login2 import tela_login


ARQUIVO = "clientes2.csv"
validador_cpf = CPF()

# ---------------- LOGIN ----------------

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:

    tela_login()

else:

    # ---------------- CONFIG ----------------


    # ---------------- ESTILO ----------------

    st.markdown(
    """
    <style>

    .stApp {
        background-color: #121212;
        color: white;
    }

    label, p, h1, h2, h3, h4, h5, h6, span {
        color: white !important;
    }

    .stTextInput > div > div > input {
        border-radius: 10px;
        color: white;
        background-color: #1e1e1e;
    }

    .stDateInput > div > div {
        border-radius: 10px;
        color: white;
        background-color: #1e1e1e;
    }

    .stSelectbox > div > div {
        border-radius: 10px;
        color: white;
        background-color: #1e1e1e;
    }

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

    # ---------------- SIDEBAR ----------------

    st.sidebar.title("🚗 Lava Jato Pro")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Dashboard",
            "Cadastro",
            "Clientes"
        ]
    )

    if st.sidebar.button("Sair"):

        st.session_state.logado = False
        st.rerun()

    # ---------------- FUNÇÕES ----------------

    def salvar_cliente(nome, cpf, endereco, dt_nasc, tp_cliente, marca):

        arquivo_existe = os.path.isfile(ARQUIVO)

        with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:

            writer = csv.writer(arquivo)

            if not arquivo_existe:

                writer.writerow([
                    "Nome",
                    "CPF",
                    "Endereco",
                    "Nascimento",
                    "Tipo",
                    "Marca"
                ])

            writer.writerow([
                nome,
                cpf,
                endereco,
                dt_nasc,
                tp_cliente,
                marca
            ])

    def carregar_clientes():
        try:


            if os.path.exists(ARQUIVO):

                return pd.read_csv(ARQUIVO)

            return pd.DataFrame()
        except:
            return pd.DataFrame()

    def limpar_clientes():

        if os.path.exists(ARQUIVO):

            os.remove(ARQUIVO)

    # ---------------- CARREGAR DADOS ----------------

    df = carregar_clientes()

    # ---------------- DASHBOARD ----------------

    if menu == "Dashboard":

        st.title("📊 Dashboard")

        total_clientes = len(df)

        col1, col2, col3 = st.columns(3)

        col1.metric("Clientes", total_clientes)
        col2.metric("Sistema", "Online")
        col3.metric("Cadastros", total_clientes)
        

        if not df.empty and "Marca" in df.columns:
            fig = px.pie(
            df,
            names="Marca",
            title="Marcas de Carros dos Clientes"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("Nenhum dado disponível para o gráfico!")

    # ---------------- CADASTRO ----------------

    elif menu == "Cadastro":

        st.title("📋 Cadastro de Clientes")

        col1, col2 = st.columns(2)

        with col1:

            nome = st.text_input("Nome Completo")

            cpf = st.text_input("CPF")

            endereco = st.text_input("Endereço")

        with col2:

            dt_nasc = st.date_input("Data de nascimento")

            tp_cliente = st.selectbox(
                "Tipo de cliente",
                ["Pessoa Física", "Pessoa Jurídica"]
            )

            marca = st.selectbox(
                "Marca do Carro",
                ["BMW", "Audi", "Ford", "Chevrolet"]
            )

        if st.button("Cadastrar Cliente"):

            if nome and endereco and cpf:

                if validador_cpf.validate(cpf):

                    cpf_formatado = validador_cpf.mask(cpf)

                    salvar_cliente(
                        nome,
                        cpf_formatado,
                        endereco,
                        dt_nasc,
                        tp_cliente,
                        marca
                    )

                    st.success("✅ Cliente cadastrado com sucesso!")

                else:

                    st.error("❌ CPF inválido!")

            else:

                st.error("⚠️ Preencha todos os campos!")

    # ---------------- CLIENTES ----------------

    elif menu == "Clientes":

        st.title("🔎 Clientes")

        busca = st.text_input("Buscar Cliente")

        if not df.empty:

            if busca:

                resultado = df[
                    df["Nome"].str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                ]

                st.dataframe(
                    resultado,
                    use_container_width=True
                )

            else:

                st.dataframe(
                    df,
                    use_container_width=True
                )

        else:

            st.info("Nenhum cliente cadastrado")

        if st.button("🗑️ Limpar Dados"):

            limpar_clientes()

            st.warning("Todos os dados foram apagados")
