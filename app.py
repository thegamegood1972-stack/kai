import streamlit as st
from openai import OpenAI
import time
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado (oculta cualquier referencia externa)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.7);
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
    .stat-card {
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.15);
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-8px);
        background: rgba(255,255,255,0.15);
    }
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 35px;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(0,210,255,0.5);
    }
    .stTextInput > div > div > input {
        border-radius: 30px;
        border: 2px solid rgba(0,210,255,0.3);
        background: rgba(0,0,0,0.4);
        color: white;
        font-size: 1rem;
        padding: 12px 25px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00d2ff;
        box-shadow: 0 0 15px rgba(0,210,255,0.3);
    }
    [data-testid="stSidebar"] {
        background: rgba(0,0,0,0.4);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.4);
        padding: 20px;
        margin-top: 40px;
    }
    /* Ocultar cualquier referencia a APIs externas */
    .stAlert {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Título (sin menciones a DeepSeek)
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Inteligente Personal</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🌊 **Kai AI**")
    st.markdown("---")
    st.markdown("### 📡 **Estado**")
    st.markdown('<span style="color: #00d2ff;">● Activo</span>', unsafe_allow_html=True)
    st.markdown(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    st.markdown("---")
    st.markdown("### 📊 **Estadísticas**")
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("💬 Conversaciones", total_msg)
    st.markdown("---")
    st.markdown("### 🎯 **Capacidades**")
    st.markdown("- 🧠 Inteligencia Artificial")
    st.markdown("- 💻 Código en tiempo real")
    st.markdown("- 📚 Aprendizaje continuo")
    st.markdown("- ⚡ Respuesta inmediata")
    st.markdown("---")
    st.markdown("### 🚀 **Versión**")
    st.markdown("**Kai 1.0**")
    st.caption("By Giovanni")

# Columnas
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

# Conectar a la IA (sin mostrar el proveedor)
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

# Inicializar mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": "🌊 **¡Bienvenido a Kai!**\n\nSoy tu asistente personal de inteligencia artificial.\n\n**Puedo ayudarte con:**\n- 💡 Responder preguntas\n- 💻 Generar código\n- 📚 Explicar conceptos\n- 🤔 Lo que necesites\n\n**¿En qué puedo ayudarte hoy?** 🚀"
    })

# Mostrar mensajes
for msg in st.session_state.mensajes:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    with st.chat_message("assistant", avatar="🧠"):
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
                st.error(f"Error: {str(e)}")
                respuesta = f"Lo siento, tuve un error: {str(e)}"
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()

# Footer
st.markdown("""
<div class="footer">
    <p>🧠 <strong>Kai AI</strong> - Asistente Personal Inteligente</p>
    <p>⚡ Disponible 24/7 | 💡 Respuesta inmediata</p>
</div>
""", unsafe_allow_html=True)
