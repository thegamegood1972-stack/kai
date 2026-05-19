import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Kai", layout="wide")
st.title("🌊 Kai - Asistente IA")

st.write("### Depuración: Iniciando...")

try:
    # Verificar que Secrets existe
    if "GEMINI_API_KEY" in st.secrets:
        st.success("✅ Secrets encontrado: GEMINI_API_KEY")
        api_key = st.secrets["GEMINI_API_KEY"]
        st.write(f"La clave comienza con: {api_key[:10]}...")
    else:
        st.error("❌ GEMINI_API_KEY NO encontrado en Secrets")
        st.write("Claves disponibles:", list(st.secrets.keys()))
        st.stop()
    
    # Configurar Gemini
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    st.success("✅ Conectado a Gemini!")
    
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# Chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["contenido"])

if prompt := st.chat_input("Escribe tu mensaje:"):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta = modelo.generate_content(prompt)
            st.markdown(respuesta.text)
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta.text})
