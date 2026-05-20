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

# CSS personalizado
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        background: linear-gradient(90deg, #fff, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        margin-bottom: 30px;
        font-size: 1.2rem;
    }
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
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 30px;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(0,210,255,0.6);
    }
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
    [data-testid="stSidebar"] {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
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

# Sidebar
with st.sidebar:
    st.markdown("## 🌊 Kai AI")
    st.markdown("---")
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
    st.markdown("- 🧠 Explicar redes neuronales")
    st.markdown("- 💻 Generar código Python")
    st.markdown("- 📚 Enseñar backpropagation")
    st.markdown("- ⚡ Respuesta inmediata")
    st.markdown("---")
    st.markdown("### 🚀 Versión")
    st.markdown("**Kai AI 3.0**")
    st.caption("Desarrollado por Giovanni")

# Columnas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-card"><h2>🧠</h2><p>Redes Neuronales</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><h2>⚡</h2><p>Respuesta Rápida</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><h2>💡</h2><p>Aprendizaje</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><h2>🌊</h2><p>IA Avanzada</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Función de respuesta simulada (no necesita API)
def responder_simulado(prompt):
    prompt_lower = prompt.lower()
    
    if any(p in prompt_lower for p in ["hola", "buenos", "saludos"]):
        return "🌊 ¡Hola! Soy Kai, tu asistente de redes neuronales. ¿En qué puedo ayudarte hoy? 😊"
    
    elif any(p in prompt_lower for p in ["codigo", "código", "programa", "implementar"]):
        return """**🧠 Código de Red Neuronal en Python**

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

# Ejemplo de uso
X = np.array([[0,0], [0,1], [1,0], [1,1]])
red = RedNeuronal(2, 4, 1)
print(red.forward(X))
