import streamlit as st
import os

st.set_page_config(page_title="Previsor de Roleta", layout="centered")

st.title("Previsor de Roleta - Histórico e Previsão")
st.markdown("Digite os 20 últimos números sorteados:")

historico_path = "historico.txt"
if not os.path.exists(historico_path):
    with open(historico_path, "w") as f:
        f.write("")

with open(historico_path, "r") as f:
    historico = f.read()

entrada = st.text_input("Digite os números separados por vírgula", value=historico)

if st.button("Salvar"):
    with open(historico_path, "w") as f:
        f.write(entrada)
    st.success("Histórico salvo com sucesso!")

if st.button("Prever próximo número"):
    numeros = [int(x.strip()) for x in entrada.split(",") if x.strip().isdigit()]
    if len(numeros) < 5:
        st.warning("Digite ao menos 5 números.")
    else:
        import random
        st.subheader(f"Próximo número provável: {random.choice(numeros)}")
