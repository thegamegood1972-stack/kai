import streamlit as st
import time
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado premium
st.markdown("""
<style>
    /* Fondo con gradiente premium */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        text-shadow: 0 0 30px rgba(0,210,255,0.3);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { opacity: 0.8; }
        50% { opacity: 1; text-shadow: 0 0 40px rgba(0,210,255,0.6); }
        100% { opacity: 0.8; }
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.7);
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
    
    /* Tarjetas premium */
    .stat-card {
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.15);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stat-card:hover {
        transform: translateY(-8px);
        background: rgba(255,255,255,0.15);
        border-color: rgba(0,210,255,0.5);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Contenedor del chat */
    .chat-container {
        background: rgba(0,0,0,0.3);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Botón premium */
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 35px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(0,210,255,0.5);
        letter-spacing: 2px;
    }
    
    /* Input premium */
    .stTextInput > div > div > input {
        border-radius: 30px;
        border: 2px solid rgba(0,210,255,0.3);
        background: rgba(0,0,0,0.4);
        color: white;
        font-size: 1rem;
        padding: 12px 25px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d2ff;
        box-shadow: 0 0 15px rgba(0,210,255,0.3);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.5);
    }
    
    /* Mensajes del chat */
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
    }
    
    /* Sidebar premium */
    [data-testid="stSidebar"] {
        background: rgba(0,0,0,0.4);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.4);
        padding: 20px;
        margin-top: 40px;
        font-size: 0.8rem;
    }
    
    /* Badge de estado */
    .status-badge {
        display: inline-block;
        background: rgba(0,210,255,0.2);
        border-radius: 20px;
        padding: 5px 15px;
        font-size: 0.8rem;
        color: #00d2ff;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Asistente Inteligente de Redes Neuronales</div>', unsafe_allow_html=True)

# Badge de estado
st.markdown('<div style="text-align: center;"><span class="status-badge">⚡ Disponible 24/7</span></div>', unsafe_allow_html=True)

# Sidebar premium
with st.sidebar:
    st.markdown("## 🌊 **Kai AI**")
    st.markdown("---")
    
    # Información del asistente
    st.markdown("### 📡 **Estado del Sistema**")
    st.markdown('<span style="color: #00d2ff;">● Activo</span>', unsafe_allow_html=True)
    st.markdown(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    
    # Estadísticas
    st.markdown("### 📊 **Estadísticas**")
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("💬 Conversaciones", total_msg)
    
    st.markdown("---")
    
    # Capacidades
    st.markdown("### 🎯 **Capacidades**")
    st.markdown("""
    <div style="background: rgba(0,210,255,0.1); border-radius: 15px; padding: 15px;">
        <span style="color: #00d2ff;">🧠</span> Redes Neuronales<br>
        <span style="color: #00d2ff;">💻</span> Código Python<br>
        <span style="color: #00d2ff;">📚</span> Backpropagation<br>
        <span style="color: #00d2ff;">⚡</span> Deep Learning
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 **Versión**")
    st.markdown("**Kai AI 3.0**")
    st.caption("Powered by Streamlit")

# Columnas de características
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0; font-size: 2.5rem;">🧠</h2>
        <p style="margin:0;"><strong>Redes Neuronales</strong></p>
        <small>Deep Learning</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0; font-size: 2.5rem;">⚡</h2>
        <p style="margin:0;"><strong>Respuesta Rápida</strong></p>
        <small>Milliseconds</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0; font-size: 2.5rem;">💡</h2>
        <p style="margin:0;"><strong>Aprendizaje</strong></p>
        <small>Continuo</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0; font-size: 2.5rem;">🌊</h2>
        <p style="margin:0;"><strong>IA Avanzada</strong></p>
        <small>GPT-4 Level</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Contenedor del chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown("### 💬 **Conversación**")

# Función de respuesta (modo demostración)
def responder(prompt):
    p = prompt.lower()
    if "hola" in p or "buenos" in p:
        return "🌊 ¡Hola! Soy Kai, tu asistente de IA. ¿En qué puedo ayudarte hoy? 😊"
    elif "codigo" in p or "código" in p:
        return "**🧠 Código de Red Neuronal**\n\n```python\nimport numpy as np\n\nclass RedNeuronal:\n    def __init__(self, entradas, ocultas, salidas):\n        self.w1 = np.random.randn(entradas, ocultas) * 0.5\n        self.w2 = np.random.randn(ocultas, salidas) * 0.5\n    \n    def forward(self, X):\n        self.z1 = np.dot(X, self.w1)\n        self.a1 = 1/(1+np.exp(-self.z1))\n        self.z2 = np.dot(self.a1, self.w2)\n        self.a2 = 1/(1+np.exp(-self.z2))\n        return self.a2\n```"
    elif "backpropagation" in p:
        return "**🧠 Retropropagación**: Algoritmo que ajusta los pesos de la red minimizando el error. 🔄"
    elif "gracias" in p:
        return "🌊 ¡De nada! Estoy aquí para ayudarte. 😊"
    else:
        return f"🌊 Entiendo tu consulta sobre: '{prompt}'\n\nPronto tendré respuestas más avanzadas con DeepSeek API. 🚀"

# Inicializar mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": "🌊 **¡Bienvenido a Kai AI!**\n\nTu asistente inteligente para **redes neuronales**.\n\n**¿Qué puedo hacer por ti?**\n- 🧠 Explicar redes neuronales\n- 💻 Generar código Python\n- 📚 Enseñar backpropagation\n- ⚡ Respuesta rápida\n\n**¡Comencemos!** 🚀"
    })

# Mostrar mensajes
for msg in st.session_state.mensajes:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Agregar mensaje del usuario
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generar respuesta
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("🌊 Kai está pensando..."):
            time.sleep(0.5)
            respuesta = responder(prompt)
            st.markdown(respuesta)
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer premium
st.markdown("""
<div class="footer">
    <p>🧠 <strong>Kai AI</strong> - Asistente de Redes Neuronales</p>
    <p>⚡ Modo Demostración | 💡 Próximamente con DeepSeek API | 🚀 Desarrollado con Streamlit</p>
</div>
""", unsafe_allow_html=True)
