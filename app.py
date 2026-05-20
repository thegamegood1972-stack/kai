import streamlit as st
import google.generativeai as genai
import numpy as np
import time

st.set_page_config(page_title="Kai - Asistente IA", page_icon="🧠", layout="wide")

# ========== DIAGNÓSTICO DE SECRETS ==========
st.write("### 🔍 Diagnóstico de Secrets")

# Verificar si st.secrets tiene datos
if st.secrets:
    st.write("✅ Secrets encontrados")
    st.write("Claves disponibles:", list(st.secrets.keys()))
else:
    st.error("❌ No se encontraron Secrets")

# Verificar específicamente GEMINI_API_KEY
if "GEMINI_API_KEY" in st.secrets:
    st.success("✅ GEMINI_API_KEY encontrada")
    # Mostrar solo primeros 10 caracteres por seguridad
    clave = st.secrets["GEMINI_API_KEY"]
    st.write(f"La clave comienza con: {clave[:15]}...")
else:
    st.error("❌ GEMINI_API_KEY NO encontrada")
    st.info("Ve a Settings → Secrets y agrega: GEMINI_API_KEY = 'tu-clave'")
    st.stop()

st.markdown("---")
st.write("### 🚀 Iniciando Kai...")
st.markdown("---")

# ========== CONFIGURAR GEMINI ==========
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    st.success("✅ Conectado a Gemini!")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# ========== INTERFAZ ==========
st.title("🧠 Kai - Asistente de Redes Neuronales")

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["contenido"])

if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Kai está pensando..."):
            try:
                respuesta = modelo.generate_content(prompt).text
                st.markdown(respuesta)
            except Exception as e:
                st.error(f"Error: {e}")
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
