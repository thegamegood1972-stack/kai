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

# CSS personalizado
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        margin-bottom: 30px;
    }
    .stat-card {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Inteligente de Redes Neuronales</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🧠 Kai AI")
    st.markdown("---")
    st.markdown("### 📊 Estadísticas")
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("Total de mensajes", total_msg)
    st.markdown("---")
    st.markdown("### 🎯 Capacidades")
    st.markdown("- Conversacion natural")
    st.markdown("- Codigo de redes neuronales")
    st.markdown("- Explicacion de conceptos IA")
    st.markdown("- Respuesta rapida")

# Columnas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-card"><h3>🧠</h3><p>Redes Neuronales</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><h3>⚡</h3><p>Respuesta Rapida</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><h3>💡</h3><p>Aprendizaje Continuo</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><h3>🌊</h3><p>IA Avanzada</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Configurar Gemini
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    st.success("✅ Kai esta en linea y listo para ayudarte")
except Exception as e:
    st.error(f"⚠️ Error de conexion: {e}")
    st.stop()

# Funcion de animacion
def mostrar_escritura(texto, placeholder):
    palabras = texto.split()
    for i in range(len(palabras)):
        placeholder.markdown(" ".join(palabras[:i+1]) + " ▌")
        time.sleep(0.03)
    placeholder.markdown(texto)

# Inicializar mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    bienvenida = "🌊 **Bienvenido a Kai!**\n\nSoy tu asistente especializado en **redes neuronales e inteligencia artificial**.\n\nPuedes preguntarme sobre:\n- 🧠 Codigo de redes neuronales\n- 📚 Explicacion de backpropagation\n- 💡 Conceptos de deep learning\n- 🤖 Cualquier tema de IA\n\n**Por donde empezamos?**"
    st.session_state.mensajes.append({"rol": "assistant", "contenido": bienvenida})

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
            try:
                if any(p in prompt.lower() for p in ["codigo", "codigo", "programa", "implementar"]):
                    respuesta = "**Codigo de Red Neuronal Simple**\n\n```python\nimport numpy as np\n\nclass RedNeuronal:\n    def __init__(self, entradas, ocultas, salidas):\n        self.w1 = np.random.randn(entradas, ocultas) * 0.5\n        self.w2 = np.random.randn(ocultas, salidas) * 0.5\n    \n    def activacion(self, x):\n        return 1 / (1 + np.exp(-x))\n    \n    def forward(self, X):\n        self.z1 = np.dot(X, self.w1)\n        self.a1 = self.activacion(self.z1)\n        self.z2 = np.dot(self.a1, self.w2)\n        self.a2 = self.activacion(self.z2)\n        return self.a2\n\n# Ejemplo\nentrada = np.array([[0,0], [0,1], [1,0], [1,1]])\nred = RedNeuronal(2, 4, 1)\nprint(red.forward(entrada))\n```\n\n💡 **Te gustaria que explique como funciona este codigo?**"
                
                elif "backpropagation" in prompt.lower():
                    respuesta = "**🧠 Retropropagacion (Backpropagation)**\n\nEs el algoritmo que ajusta los pesos de la red neuronal para minimizar el error.\n\n**Proceso:**\n1. Forward pass - Hace una prediccion\n2. Calcular error - Diferencia entre prediccion y valor real\n3. Backward pass - Propaga el error hacia atras\n4. Actualizar pesos - Ajusta las conexiones\n5. Repetir - Durante muchas epocas\n\n**Analogia:** Es como aprender a lanzar una pelota: pruebas, ves el error, ajustas y repites hasta acertar.\n\nQuieres que te muestre un ejemplo practico?"
                
                else:
                    respuesta = modelo.generate_content(prompt).text
                
                placeholder = st.empty()
                mostrar_escritura(respuesta, placeholder)
                
            except Exception as e:
                respuesta = f"🌊 **Lo siento, tuve un error:** {str(e)}\n\nPor favor, intenta con otra pregunta."
                placeholder = st.empty()
                mostrar_escritura(respuesta, placeholder)
    
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>🧠 Kai AI - Desarrollado con Streamlit y Gemini</p>", unsafe_allow_html=True)
