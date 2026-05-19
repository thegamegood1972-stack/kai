import streamlit as st
from openai import OpenAI
import numpy as np

st.set_page_config(page_title="Kai - Red Neuronal", layout="wide")
st.title("🧠 Kai - Tu Asistente de Redes Neuronales")

# Configurar DeepSeek
api_key = st.secrets["DEEPSEEK_API_KEY"]
cliente = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

# Función de código de red neuronal
def codigo_red_neuronal():
    return """
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
entrada = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
red = RedNeuronal(2, 4, 1)
print(red.forward(entrada))
```"""

# Interfaz de chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["contenido"])

if prompt := st.chat_input("Pregunta sobre redes neuronales..."):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Kai está pensando..."):
            try:
                if "código" in prompt.lower() or "codigo" in prompt.lower():
                    respuesta = codigo_red_neuronal()
                else:
                    response = cliente.chat.completions.create(
                        model="deepseek-chat",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    respuesta = response.choices[0].message.content
            except Exception as e:
                respuesta = f"🌊 Lo siento, tuve un error: {str(e)}"
            st.markdown(respuesta)
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
