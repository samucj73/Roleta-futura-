
import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
from collections import Counter
import re

# Configuração da página
st.set_page_config(page_title="Previsor de Roleta", layout="centered")

st.title("Previsor de Números da Roleta via Imagem")

# Upload da imagem
uploaded_file = st.file_uploader("Envie uma imagem JPEG com os números:", type=["jpg", "jpeg"])

def process_image(image):
    # Convertendo imagem para escala de cinza
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)  # binariza
    return img

def extract_numbers(text):
    # Extrai todos os números da string
    return list(map(int, re.findall(r'\d+', text)))

def analisar_padroes(numeros):
    # Frequência dos números
    contagem = Counter(numeros)
    mais_comuns = contagem.most_common(10)
    previsoes = [num for num, freq in mais_comuns]
    return previsoes

if uploaded_file:
    # Mostra imagem enviada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem Enviada", use_column_width=True)

    # Processa a imagem e extrai texto
    with st.spinner("Processando imagem e extraindo números..."):
        processed_img = process_image(image)
        text = pytesseract.image_to_string(processed_img, config='--psm 6')
        numeros = extract_numbers(text)

    if numeros:
        st.success(f"Números detectados: {numeros}")

        # Analisar padrões
        previsoes = analisar_padroes(numeros)
        st.subheader("10 Números Prováveis:")
        st.write(previsoes)
    else:
        st.warning("Não foram encontrados números na imagem.")
