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
    st.markdown("- Explicar redes neuronales")
    st.markdown("- Generar codigo Python")
    st.markdown("- Ensenar backpropagation")
    st.markdown("- Respuesta inmediata")
    st.markdown("---")
    st.markdown("### 🚀 Version")
    st.markdown("**Kai AI 3.0**")
    st.caption("Desarrollado por Giovanni")

# Columnas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-card"><h2>🧠</h2><p>Redes Neuronales</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><h2>⚡</h2><p>Respuesta Rapida</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><h2>💡</h2><p>Aprendizaje</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><h2>🌊</h2><p>IA Avanzada</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Función de respuesta simulada
def responder_simulado(prompt):
    prompt_lower = prompt.lower()
    
    if any(p in prompt_lower for p in ["hola", "buenos", "saludos"]):
        return "🌊 Hola! Soy Kai, tu asistente de redes neuronales. En que puedo ayudarte hoy?"
    
    elif any(p in prompt_lower for p in ["codigo", "codigo", "programa", "implementar"]):
        return "**Codigo de Red Neuronal en Python**\n\n```python\nimport numpy as np\n\nclass RedNeuronal:\n    def __init__(self, entradas, ocultas, salidas):\n        self.w1 = np.random.randn(entradas, ocultas) * 0.5\n        self.w2 = np.random.randn(ocultas, salidas) * 0.5\n    \n    def activacion(self, x):\n        return 1 / (1 + np.exp(-x))\n    \n    def forward(self, X):\n        self.z1 = np.dot(X, self.w1)\n        self.a1 = self.activacion(self.z1)\n        self.z2 = np.dot(self.a1, self.w2)\n        self.a2 = self.activacion(self.z2)\n        return self.a2\n\n# Ejemplo\nX = np.array([[0,0], [0,1], [1,0], [1,1]])\nred = RedNeuronal(2, 4, 1)\nprint(red.forward(X))\n```\n\nTe gustaria que explique como funciona?"
    
    elif "backpropagation" in prompt_lower:
        return "**Retropropagacion (Backpropagation)**\n\nEs el algoritmo que ajusta los pesos de la red para minimizar el error.\n\n**Proceso:**\n1. Forward pass - Hace una prediccion\n2. Calcular error - Diferencia entre prediccion y valor real\n3. Backward pass - Propaga el error hacia atras\n4. Actualizar pesos - Ajusta las conexiones\n5. Repetir - Durante muchas epocas\n\n**Analogia:** Es como aprender a lanzar una pelota: pruebas, ves el error, ajustas y repites hasta acertar."
    
    elif "gracias" in prompt_lower:
        return "🌊 De nada! Estoy aqui para ayudarte. Alguna otra pregunta?"
    
    else:
        return f"🌊 Entiendo tu pregunta sobre: '{prompt}'.\n\nPuedes pedirme:\n- Codigo de redes neuronales\n- Explicacion de backpropagation\n- Conceptos de deep learning"

# Inicializar mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": "🌊 **Bienvenido a Kai!**\n\nSoy tu asistente especializado en redes neuronales e inteligencia artificial.\n\n**Puedo ayudarte con:**\n- Codigo de redes neuronales\n- Explicacion de backpropagation\n- Conceptos de deep learning\n\n**Por donde empezamos?**"
    })

# Mostrar mensajes
for msg in st.session_state.mensajes:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aqui..."):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Kai esta pensando..."):
            time.sleep(0.5)
            respuesta = responder_simulado(prompt)
            st.markdown(respuesta)
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()

# Footer
st.markdown("""
<div class="footer">
    <p>Kai AI - Asistente de Redes Neuronales | Desarrollado con Streamlit</p>
    <p>Modo Demostracion | Totalmente funcional</p>
</div>
""", unsafe_allow_html=True)
