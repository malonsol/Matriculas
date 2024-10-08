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
def load_dictionary():
    dictionary_path = os.path.join(os.path.dirname(__file__), 'dic_rae.txt')
    with open(dictionary_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

# Función para encontrar palabras que contengan las consonantes en el orden especificado
def find_words_with_consonants(consonants, words):
    consonants = ''.join(consonants)
    result = [word for word in words if contains_in_order(consonants, word)]
    return result

# Función para verificar si las consonantes están en el orden correcto dentro de la palabra
def contains_in_order(consonants, word):
    index = 0
    for char in word:
        if char.lower() == consonants[index].lower():
            index += 1
            if index == len(consonants):
                return True
    return False

# Función para validar consonantes
def is_consonant(c):
    return c.isalpha() and c.lower() not in 'aeiou'

# Configuración de la aplicación
st.title('El flamante juego de las matrículas')
st.subheader('by La Reina')
st.write('Introduce 3 consonantes para buscar palabras que las contengan en ese orden.')

# Input del usuario
consonants_input = st.text_input('Consonantes (3):', max_chars=3)

# Procesar la entrada del usuario
if consonants_input:
    consonants_filtered = [c for c in consonants_input if is_consonant(c)]

    if len(consonants_filtered) == 3:
        words = load_dictionary()
        matching_words = find_words_with_consonants(consonants_filtered, words)

        if matching_words:
            st.write('Palabras encontradas:')
            for word in matching_words:
                st.markdown(f'<div class="result">{word}</div>', unsafe_allow_html=True)
        else:
            st.write('No se encontraron palabras que contengan esas consonantes.')
    else:
        st.write('Por favor, introduce exactamente 3 consonantes. Cualquier otro carácter (número, vocales, símbolos...) será omitido.')
else:
    st.write('Por favor, introduce exactamente 3 consonantes.')
