import streamlit as st
import os

# Cargar el diccionario de palabras
@st.cache
def load_dictionary():
    # Obtener la ruta del archivo dic_rae.txt relativa al script
    dictionary_path = os.path.join(os.path.dirname(__file__), 'dic_rae.txt')
    with open(dictionary_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

# Función para encontrar palabras que contengan las consonantes en el orden especificado
def find_words_with_consonants(consonants, words):
    consonants = ''.join(consonants)  # Convierto la lista en un string
    result = [word for word in words if contains_in_order(consonants, word)]
    return result

# Función para verificar si las consonantes están en el orden correcto dentro de la palabra
def contains_in_order(consonants, word):
    index = 0
    for char in word:
        if char.lower() == consonants[index].lower():  # Ignora mayúsculas y minúsculas
            index += 1
            if index == len(consonants):  # Si hemos encontrado todas las consonantes
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
    # Filtrar la entrada para quedarnos solo con consonantes
    consonants_filtered = [c for c in consonants_input if is_consonant(c)]

    if len(consonants_filtered) == 3:
        words = load_dictionary()
        matching_words = find_words_with_consonants(consonants_filtered, words)

        # Mostrar resultados
        if matching_words:
            st.write('Palabras encontradas:')
            for word in matching_words:
                st.write(word)
        else:
            st.write('No se encontraron palabras que contengan esas consonantes.')
    else:
        st.write('Por favor, introduce exactamente 3 consonantes. Cualquier otro carácter (número, vocales, símbolos...) será omitido.')
else:
    st.write('Por favor, introduce exactamente 3 consonantes.')
