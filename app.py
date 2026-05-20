import streamlit as st
import numpy as np
import time
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para diseño profesional
st.markdown("""
<style>
    /* Fondo con gradiente */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        background: linear-gradient(90deg, #fff, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        text-shadow: 0 0 30px rgba(0,210,255,0.3);
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
    
    /* Tarjetas de estadísticas */
    .stat-card {
        background: rgba(255,255,255,0.15);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.25);
    }
    
    /* Contenedor de chat */
    .chat-container {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
    
    /* Botón personalizado */
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(0,210,255,0.6);
    }
    
    /* Input personalizado */
    .stTextInput > div > div > input {
        border-radius: 30px;
        border: 2px solid #00d2ff;
        background: rgba(0,0,0,0.3);
        color: white;
        font-size: 1rem;
        padding: 12px 20px;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.6);
    }
    
    /* Mensajes del chat */
    .stChatMessage {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.6);
        padding: 20px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Inteligente de Redes Neuronales</div>', unsafe_allow_html=True)

# Sidebar con información
with st.sidebar:
    st.markdown("## 🌊 Kai AI")
    st.markdown("---")
    
    # Estado de conexión
    st.markdown("### 📡 Estado")
    st.markdown("✅ **Sistema Activo**")
    st.markdown(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    st.markdown("### 📊 Estadísticas")
    
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("💬 Mensajes", total_msg)
    
    st.markdown("---")
    st.markdown("### 🎯 Capacidades")
    st.markdown("""
    - 🧠 Explicar redes neuronales
    - 💻 Generar código Python
    - 📚 Enseñar backpropagation
    - ⚡ Respuesta inmediata
    """)
    
    st.markdown("---")
    st.markdown("### 🚀 Versión")
    st.markdown("**Kai AI 3.0**")
    st.caption("Desarrollado por Giovanni")

# Columnas de características
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0;">🧠</h2>
        <p style="margin:0;"><strong>Redes Neuronales</strong></p>
        <small>Aprendizaje profundo</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0;">⚡</h2>
        <p style="margin:0;"><strong>Respuesta Rápida</strong></p>
        <small>Milliseconds</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0;">💡</h2>
        <p style="margin:0;"><strong>Aprendizaje</strong></p>
        <small>Continuo</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h2 style="margin:0;">🌊</h2>
        <p style="margin:0;"><strong>IA Avanzada</strong></p>
        <small>Deep Learning</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Función de respuesta simulada (mientras no hay API)
def responder_simulado(prompt):
    prompt_lower = prompt.lower()
    
    if any(p in prompt_lower for p in ["hola", "buenos", "saludos"]):
        return "🌊 ¡Hola! Soy Kai, tu asistente de redes neuronales. ¿En qué puedo ayudarte hoy? 😊"
    
    elif any(p in prompt_lower for p in ["codigo", "código", "programa"]):
        return """**Aquí tienes un ejemplo de Red Neuronal en Python:**

```python
import numpy as np

class RedNeuronal:
    def __init__(self, entradas, ocultas, salidas):
        self.w1 = np.random.randn(entradas, ocultas) * 0.5
        self.w2 = np.random.randn(ocultas, salidas) * 0.5
    
    def activacion(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, X):
        self.z1 = np.dot(X, self.w1)
        self.a1 = self.activacion(self.z1)
        self.z2 = np.dot(self.a1, self.w2)
        self.a2 = self.activacion(self.z2)
        return self.a2

# Ejemplo
X = np.array([[0,0], [0,1], [1,0], [1,1]])
red = RedNeuronal(2, 4, 1)
print(red.forward(X))
