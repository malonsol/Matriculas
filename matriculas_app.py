import streamlit as st
import os

# Estilo CSS para la aplicación
st.markdown("""
<style>
    .main {
        background-image: url('https://images.unsplash.com/photo-1517942228356-63411b895c49?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGNhdHxlbnwwfHx8fDE2MzY4OTg4MjE&ixlib=rb-1.2.1&q=80&w=1080'); /* URL de la imagen */
        background-size: cover;
        background-position: center;
        color: white; /* Cambiar color del texto si es necesario */
    }
    h1 {
        color: #4CAF50; /* Color del título */
        font-family: 'Poppins', sans-serif; /* Fuente del título */
    }
    h2 {
        color: #FF9800; /* Color del subtítulo */
        font-family: 'Poppins', sans-serif; /* Fuente del subtítulo */
    }
    .result {
        font-family: 'Roboto', sans-serif; /* Fuente del texto de resultados */
        color: #212121; /* Color del texto */
        margin: 10px 0;
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@400&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Cargar el diccionario de palabras
@st.cache
def load
