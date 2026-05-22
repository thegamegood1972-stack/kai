import streamlit as st
from openai import OpenAI
from datetime import datetime
import json
import os
import hashlib

# ========== CONFIGURACIÓN ==========
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== ARCHIVO DE LOGS ==========
LOG_FILE = "kai_usage_log.json"

def registrar_uso(usuario_id, prompt, respuesta):
    """Registra cada interacción en un archivo JSON"""
    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario_id": usuario_id,
        "prompt": prompt[:200],
        "respuesta": respuesta[:200]
    }
    
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    
    logs.append(registro)
    
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

# ========== CSS ==========
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

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 🌊 **Kai AI**")
    st.markdown("---")
    st.markdown("### 📡 **Estado**")
    st.markdown('<span style="color: #00d2ff;">● Activo</span>', unsafe_allow_html=True)
    st.markdown(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    st.markdown("---")
    
    # Botón de donación
    st.markdown("### ☕ **Apoya a Kai**")
    st.markdown("[![Donar](https://img.shields.io/badge/☕_Donar-Ko--fi-ff5e5e?style=for-the-badge)](https://ko-fi.com/tuusuario)")
    st.markdown("---")
    
    st.markdown("### 🚀 **Versión**")
    st.markdown("**Kai 1.0**")
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

# ========== CONEXIÓN A LA IA ==========
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

PERSONALIDAD = """
Eres Kai, un asistente personal amigable y servicial.
Caracteristicas:
- Hablas de forma calida y cercana
- Usas emojis ocasionalmente (😊, 🌊, 🚀)
- Si no sabes algo, lo dices honestamente
"""

# ========== IDENTIFICACIÓN DEL USUARIO ==========
if "usuario_id" not in st.session_state:
    session_id = str(datetime.now().timestamp())
    st.session_state.usuario_id = hashlib.md5(session_id.encode()).hexdigest()[:8]

# ========== CHAT ==========
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": "🌊 **¡Bienvenido a Kai!**\n\nSoy tu asistente personal de inteligencia artificial.\n\n**¿En qué puedo ayudarte hoy?** 🚀"
    })

for msg in st.session_state.mensajes:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

if prompt := st.chat_input("Escribe tu mensaje aqui..."):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Kai esta pensando..."):
            try:
                response = cliente.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "system", "content": PERSONALIDAD}, {"role": "user", "content": prompt}],
                    temperature=0.7
                )
                respuesta = response.choices[0].message.content
                st.markdown(respuesta)
                
                # Registrar el uso (solo para ti, en el servidor)
                registrar_uso(st.session_state.usuario_id, prompt, respuesta)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                respuesta = f"Lo siento, tuve un error: {str(e)}"
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()

# ========== FOOTER ==========
st.markdown("""
<div class="footer">
    <p>🧠 <strong>Kai AI</strong> - Asistente Personal Inteligente</p>
    <p>⚡ Disponible 24/7 | 💡 Respuesta inmediata | ☕ Apoya con un café</p>
</div>
""", unsafe_allow_html=True)
# === TEMPORAL: VER LOGS DE CONVERSACIONES ===
with st.expander("📊 Ver conversaciones (solo creador)"):
    import json
    import os
    import pandas as pd
    
    if os.path.exists("kai_usage_log.json"):
        with open("kai_usage_log.json", "r") as f:
            logs = json.load(f)
        if logs:
            df = pd.DataFrame(logs)
            st.dataframe(df)
            st.download_button("Descargar CSV", df.to_csv(index=False), "conversaciones.csv")
        else:
            st.info("No hay conversaciones registradas aún")
    else:
        st.info("El archivo de logs aún no existe")

# ========== FOOTER ==========
st.markdown("""
<div class="footer">
    <p>🧠 <strong>Kai AI</strong> - Asistente Personal Inteligente</p>
    <p>⚡ Disponible 24/7 | 💡 Respuesta inmediata | ☕ Apoya con un café</p>
</div>
""", unsafe_allow_html=True)
