import streamlit as st
from openai import OpenAI
from datetime import datetime

# ========== CONFIGURACIÓN DE PÁGINA ==========
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CONFIGURACIÓN DE USUARIO MASTER ==========
MASTER_CODE = "kai2026"  # Código secreto para activar modo admin
MAX_MENSAJES_GRATIS = 10  # Límite de mensajes para usuarios normales

# ========== PERSONALIDAD DE KAI ==========
PERSONALIDAD = """
Eres Kai, un asistente personal amigable y servicial.
Caracteristicas:
- Hablas de forma calida y cercana
- Usas emojis ocasionalmente (😊, 🌊, 🚀)
- Llamas al usuario por su nombre si lo sabes
- Si no sabes algo, lo dices honestamente
- Te despides con "¡Hasta pronto!" o similar
"""

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
    .stTextInput > div > div > input:focus { border-color: #00d2ff; box-shadow: 0 0 15px rgba(0,210,255,0.3); }
    [data-testid="stSidebar"] { background: rgba(0,0,0,0.4); backdrop-filter: blur(10px); border-right: 1px solid rgba(255,255,255,0.1); }
    .footer { text-align: center; color: rgba(255,255,255,0.4); padding: 20px; margin-top: 40px; }
    .admin-badge { background: #00d2ff; color: #0f0c29; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; display: inline-block; }
</style>
""", unsafe_allow_html=True)

# ========== TÍTULO ==========
st.markdown('<div class="main-title">🧠 KAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tu Asistente Personal Inteligente</div>', unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 🌊 **Kai AI**")
    st.markdown("---")
    
    # Estado y modo admin
    st.markdown("### 📡 **Estado**")
    if st.session_state.get('is_master', False):
        st.markdown('<span class="admin-badge">👑 MODO ADMIN ACTIVADO</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span style="color: #00d2ff;">● Activo</span>', unsafe_allow_html=True)
    st.markdown(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    
    # Estadísticas
    st.markdown("### 📊 **Estadísticas**")
    if "mensajes" in st.session_state:
        total_msg = len(st.session_state.mensajes)
        st.metric("💬 Conversaciones", total_msg)
    if "contador_mensajes" in st.session_state:
        st.metric("📨 Mensajes usados", st.session_state.contador_mensajes)
    
    st.markdown("---")
    
    # Capacidades
    st.markdown("### 🎯 **Capacidades**")
    st.markdown("- 🧠 Inteligencia Artificial")
    st.markdown("- 💻 Código en tiempo real")
    st.markdown("- 📚 Aprendizaje continuo")
    st.markdown("- ⚡ Respuesta inmediata")
    
    st.markdown("---")
    
    # ========== BOTÓN DE DONACIÓN KO-FI ==========
    st.markdown("### ☕ **Apoya a Kai**")
    st.markdown("Si te es útil, invitame un café:")
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

# ========== INICIALIZAR VARIABLES DE SESIÓN ==========
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": "🌊 **¡Bienvenido a Kai!**\n\nSoy tu asistente personal de inteligencia artificial.\n\n**¿En qué puedo ayudarte hoy?** 🚀"
    })

if "contador_mensajes" not in st.session_state:
    st.session_state.contador_mensajes = 0

if "is_master" not in st.session_state:
    st.session_state.is_master = False

# ========== MOSTRAR MENSAJES ==========
for msg in st.session_state.mensajes:
    avatar = "🧠" if msg["rol"] == "assistant" else "👤"
    with st.chat_message(msg["rol"], avatar=avatar):
        st.markdown(msg["contenido"])

# ========== ENTRADA DEL USUARIO ==========
if prompt := st.chat_input("Escribe tu mensaje aqui..."):
    
    # ========== VERIFICAR CÓDIGO MASTER ==========
    if prompt.strip() == MASTER_CODE and not st.session_state.is_master:
        st.session_state.is_master = True
        respuesta_admin = "🧠 **👑 Modo Admin Activado.** Ahora eres el Usuario Principal. Tus mensajes no tienen límite."
        st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta_admin})
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(respuesta_admin)
        st.rerun()
    
    # ========== AGREGAR MENSAJE DEL USUARIO ==========
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # ========== VERIFICAR LÍMITE PARA USUARIOS NORMALES ==========
    if not st.session_state.is_master:
        if st.session_state.contador_mensajes >= MAX_MENSAJES_GRATIS:
            with st.chat_message("assistant", avatar="🧠"):
                st.warning(f"✨ Has alcanzado el límite de {MAX_MENSAJES_GRATIS} mensajes gratis.")
                st.info("☕ Si te gusta Kai, ¡considera invitarme un café para seguir usando el servicio sin límites! [Donar en Ko-fi](https://ko-fi.com/tuusuario)")
                st.stop()
        else:
            st.session_state.contador_mensajes += 1
    
    # ========== GENERAR RESPUESTA DE KAI ==========
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Kai esta pensando..."):
            try:
                response = cliente.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": PERSONALIDAD},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                respuesta = response.choices[0].message.content
                st.markdown(respuesta)
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
