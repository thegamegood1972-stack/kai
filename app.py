import streamlit as st
import google.generativeai as genai
import numpy as np
import time

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
    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        margin-bottom: 30px;
    }
    
    /* Tarjeta de estadísticas */
    .stat-card {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Botón personalizado */
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0,210,255,0.5);
    }
    
    /* Input personalizado */
    .stTextInput > div > div > input {
        border-radius: 30px;
        border: 2px solid #00d2ff;
        background: rgba(0,0,0,0.3);
        color: white;
    }
    
    /* Mensajes del chat */
    .stChatMessage {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 10px;
        margin: 10px 0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Inteligente de Redes Neuronales</div>', unsafe_allow_html=True)

# Sidebar con información
with st.sidebar:
    st.markdown("## 🧠 Kai AI")
    st.markdown("---")
    st.markdown("### 📊 Estadísticas")
    
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("Total de mensajes", total_msg)
    
    st.markdown("---")
    st.markdown("### 🎯 Capacidades")
    st.markdown("""
    - ✅ Conversación natural
    - ✅ Código de redes neuronales
    - ✅ Explicación de conceptos IA
    - ✅ Respuesta rápida
    """)
    
    st.markdown("---")
    st.markdown("### 🌟 Versión")
    st.markdown("**Kai AI v2.0**")
    st.caption("Desarrollado por - Giovanni")

# Columnas para métricas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="stat-card">
        <h3>🧠</h3>
        <p>Redes Neuronales</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card">
        <h3>⚡</h3>
        <p>Respuesta Rápida</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card">
        <h3>💡</h3>
        <p>Aprendizaje Continuo</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="stat-card">
        <h3>🌊</h3>
        <p>IA Avanzada</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Configurar Gemini (sin DeepSeek para evitar problemas de pago)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    
    # Mostrar estado de conexión
    st.success("✅ **Kai está en línea y listo para ayudarte**")
except Exception as e:
    st.error(f"⚠️ No se pudo conectar con la IA. Error: {str(e)}")
    st.stop()

# Función para mostrar animación de escritura
def mostrar_escritura(texto, placeholder):
    palabras = texto.split()
    for i in range(len(palabras)):
        placeholder.markdown(" ".join(palabras[:i+1]) + " ▌")
        time.sleep(0.05)
    placeholder.markdown(texto)

# Inicializar historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    
    # Mensaje de bienvenida
    bienvenida = """🌊 **¡Bienvenido a Kai!**

Soy tu asistente especializado en **redes neuronales e inteligencia artificial**.

Puedes preguntarme sobre:
- 🧠 Código de redes neuronales
- 📚 Explicación de backpropagation
- 💡 Conceptos de deep learning
- 🤖 Cualquier tema de IA

**¿Por dónde empezamos?**"""
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": bienvenida})

# Mostrar mensajes del chat
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
        with st.spinner("Kai está pensando..."):
            try:
                # Verificar si pide código
                if any(p in prompt.lower() for p in ["codigo", "código", "programa", "implementar"]):
                    respuesta = """**Código de Red Neuronal Simple**

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
entrada = np.array([[0,0], [0,1], [1,0], [1,1]])
red = RedNeuronal(2, 4, 1)
print(red.forward(entrada))
