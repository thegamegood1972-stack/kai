import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Kai - Asistente IA", layout="wide")
st.title("🧠 Kai - Asistente IA")

# Conectar a DeepSeek (yo)
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

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
            response = cliente.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}]
            )
            respuesta = response.choices[0].message.content
            st.markdown(respuesta)
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()
