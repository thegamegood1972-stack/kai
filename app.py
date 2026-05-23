import streamlit as st
from openai import OpenAI
from datetime import datetime
import json
import os
import hashlib
import uuid

# ========== CONFIGURACIÓN DE PÁGINA ==========
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CSS PERSONALIZADO ==========
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
    .main-title { text-align: center; font-size: 4rem; font-weight: bold; background: linear-gradient(90deg, #00d2ff, #3a7bd5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0; }
    .subtitle { text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 30px; font-size: 1.2rem; }
    .stat-card { background: rgba(255,255,255,0.08); border-radius: 20px; padding: 20px; text-align: center; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.15); transition: all 0.3s ease; }
    .stat-card:hover { transform: translateY(-8px); background: rgba(255,255,255,0.15); }
    .stButton > button { background: linear-gradient(90deg, #00d2ff, #3a7bd5); color: white; border: none; border-radius: 30px; padding: 12px 35px; font-weight: bold; transition: all 0.3s ease; width: 100%; }
    .stButton > button:hover { transform: scale(1.02); box-shadow: 0 0 25px rgba(0,210,255,0.5); }
    .stTextInput > div > div > input { border-radius: 30px; border: 2px solid rgba(0,210,255,0.3); background: rgba(0,0,0,0.4); color: white; font-size: 1rem; padding: 12px 25px; }
    [data-testid="stSidebar"] { background: rgba(0,0,0,0.4); backdrop-filter: blur(10px); border-right: 1px solid rgba(255,255,255,0.1); }
    .footer { text-align: center; color: rgba(255,255,255,0.4); padding: 20px; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

# ========== TÍTULO ==========
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Personal Inteligente</div>', unsafe_allow_html=True)

# ========== CONEXIÓN A LA IA ==========
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

# ========== IDENTIFICACIÓN DEL USUARIO ==========
if "usuario_id" not in st.session_state:
    session_id = str(datetime.now().timestamp())
    st.session_state.usuario_id = hashlib.md5(session_id.encode()).hexdigest()[:8]

# ========== SISTEMA DE CHATS ==========
CHATS_FILE = "kai_chats.json"

def cargar_chats():
    if os.path.exists(CHATS_FILE):
        with open(CHATS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_chats(chats):
    with open(CHATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(chats, f, ensure_ascii=False, indent=2)

def crear_nuevo_chat(titulo="Nueva conversación"):
    chat_id = str(uuid.uuid4())[:8]
    return {
        "id": chat_id,
        "titulo": titulo,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mensajes": [
            {"rol": "assistant", "contenido": "🌊 **¡Bienvenido a Kai!**\n\nSoy tu asistente personal de inteligencia artificial.\n\n**¿En qué puedo ayudarte hoy?** 🚀"}
        ]
    }

# ========== INICIALIZAR CHATS ==========
if "chats" not in st.session_state:
    st.session_state.chats = cargar_chats()
    if not st.session_state.chats:
        nuevo = crear_nuevo_chat()
        st.session_state.chats[nuevo["id"]] = nuevo

if "chat_actual_id" not in st.session_state:
    st.session_state.chat_actual_id = list(st.session_state.chats.keys())[0]

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 🌊 **Kai AI**")
    st.markdown("---")
    
    if st.button("➕ Nueva conversación", use_container_width=True):
        nuevo = crear_nuevo_chat()
        st.session_state.chats[nuevo["id"]] = nuevo
        st.session_state.chat_actual_id = nuevo["id"]
        guardar_chats(st.session_state.chats)
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📋 **Conversaciones**")
    
    for chat_id, chat in st.session_state.chats.items():
        if chat_id == st.session_state.chat_actual_id:
            st.markdown(f"<div style='background: rgba(0,210,255,0.2); border-radius: 10px; padding: 5px 10px; margin: 2px 0;'>🧠 <strong>{chat['titulo'][:30]}</strong></div>", unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([4, 1])
            with col1:
                if st.button(f"💬 {chat['titulo'][:30]}", key=f"chat_{chat_id}", use_container_width=True):
                    st.session_state.chat_actual_id = chat_id
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"del_{chat_id}"):
                    if len(st.session_state.chats) > 1:
                        del st.session_state.chats[chat_id]
                        if st.session_state.chat_actual_id == chat_id:
                            st.session_state.chat_actual_id = list(st.session_state.chats.keys())[0]
                        guardar_chats(st.session_state.chats)
                        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 **Estadísticas**")
    st.metric("💬 Mensajes", sum(len(c["mensajes"]) for c in st.session_state.chats.values()))
    st.metric("📁 Conversaciones", len(st.session_state.chats))
    
    st.markdown("---")
    st.markdown("### ☕ **Apoya a Kai**")
    st.markdown("[![Donar](https://img.shields.io/badge/☕_Donar-Ko--fi-ff5e5e?style=for-the-badge)](https://ko-fi.com/tuusuario)")
    st.markdown("---")
    st.markdown("### 🚀 **Versión**")
    st.markdown("**Kai 2.0**")
    st.caption("By Giovanni")

# ========== COLUMNAS ==========
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-card"><h2>🧠</h2><p>IA Avanzada</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><h2>⚡</h2><p>Rápida</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><h2>💡</h2><p>Inteligente</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><h2>🌊</h2><p>Personal</p></div>', unsafe_allow_html=True)

st.markdown("---")

# ========== MOSTRAR CHAT ACTUAL ==========
chat_actual = st.session_state.chats[st.session_state.chat_actual_id]

col_title, col_edit = st.columns([4, 1])
with col_title:
    st.markdown(f"### 💬 {chat_actual['titulo']}")
with col_edit:
    if st.button("✏️ Renombrar"):
        nuevo_titulo = st.text_input("Nuevo título:", value=chat_actual['titulo'])
        if nuevo_titulo:
            chat_actual['titulo'] = nuevo_titulo
            guardar_chats(st.session_state.chats)
            st.rerun()

for msg in chat_actual["mensajes"]:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

# ========== PROCESAR MENSAJE ==========
if prompt := st.chat_input("Escribe tu mensaje aqui..."):
    chat_actual["mensajes"].append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Kai está pensando..."):
            try:
                historial_api = [
                    {"role": "system", "content": "Eres Kai, un asistente personal amigable y servicial. Mantienes el contexto de la conversación."}
                ]
                for msg in chat_actual["mensajes"][-10:]:
                    if msg["rol"] == "user":
                        historial_api.append({"role": "user", "content": msg["contenido"]})
                    else:
                        historial_api.append({"role": "assistant", "content": msg["contenido"]})
                response = cliente.chat.completions.create(
                    model="deepseek-chat",
                    messages=historial_api,
                    temperature=0.7
                )
                respuesta = response.choices[0].message.content
                st.markdown(respuesta)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                respuesta = f"Lo siento, tuve un error: {str(e)}"
    
    chat_actual["mensajes"].append({"rol": "assistant", "contenido": respuesta})
    if len([m for m in chat_actual["mensajes"] if m["rol"] == "user"]) == 1:
        chat_actual["titulo"] = prompt[:30] + ("..." if len(prompt) > 30 else "")
    guardar_chats(st.session_state.chats)
    st.rerun()

# ========== FOOTER ==========
st.markdown("""
<div class="footer">
    <p>🧠 <strong>Kai AI</strong> - Asistente Personal Inteligente</p>
    <p>⚡ Disponible 24/7 | 💡 Conversaciones separadas | ☕ Apoya con un café</p>
</div>
""", unsafe_allow_html=True)
