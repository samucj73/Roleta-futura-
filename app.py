import streamlit as st
import pytesseract
from PIL import Image, ImageOps
import numpy as np
import re
from collections import Counter

st.set_page_config(page_title="Previsor de Roleta", layout="centered")
st.title("Previsor de Números da Roleta via Imagem")

uploaded_file = st.file_uploader("Envie uma imagem JPEG com os números:", type=["jpg", "jpeg"])

def process_image(image):
    image = ImageOps.grayscale(image)
    image = ImageOps.invert(image)
    return image

def extract_numbers(text):
    return list(map(int, re.findall(r'\d+', text)))

def analisar_padroes(numeros):
    contagem = Counter(numeros)
    mais_comuns = contagem.most_common(10)
    previsoes = [num for num, _ in mais_comuns]
    return previsoes

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem Enviada", use_column_width=True)

    with st.spinner("Processando imagem e extraindo números..."):
        processed_image = process_image(image)
        text = pytesseract.image_to_string(processed_image, config='--psm 6')
        numeros = extract_numbers(text)

    if numeros:
        st.success(f"Números detectados: {numeros}")
        previsoes = analisar_padroes(numeros)
        st.subheader("10 Números Prováveis:")
        st.write(previsoes)
    else:
        st.warning("Não foram encontrados números na imagem.")
