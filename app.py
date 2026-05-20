import streamlit as st
from openai import OpenAI
import numpy as np
import time

st.set_page_config(page_title="Kai - Asistente IA", page_icon="🧠", layout="wide")

# ========== CONFIGURACIÓN DEEPSEEK ==========
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

# ========== INTERFAZ ==========
st.title("🧠 Kai - Asistente de Redes Neuronales")

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({"rol": "assistant", "contenido": "🌊 ¡Hola! Soy Kai, tu asistente de redes neuronales. ¿En qué puedo ayudarte?"})

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
                response = cliente.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                respuesta = response.choices[0].message.content
                st.markdown(respuesta)
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                respuesta = error_msg
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()
