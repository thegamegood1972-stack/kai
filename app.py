import streamlit as st
from openai import OpenAI
from datetime import datetime
import json
import os
import pandas as pd

# ========== CONFIGURACIÓN ==========
st.set_page_config(
    page_title="Kai - Asistente IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== ARCHIVO DE LOGS ==========
LOG_FILE = "kai_usage_log.json"

def registrar_uso(usuario_id, prompt, respuesta, costo_estimado=0):
    """Registra cada interacción en un archivo JSON"""
    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario_id": usuario_id,
        "prompt": prompt[:200],  # Guardar solo primeros 200 caracteres
        "respuesta": respuesta[:200],
        "costo_estimado": costo_estimado
    }
    
    # Cargar logs existentes
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    
    # Agregar nuevo registro
    logs.append(registro)
    
    # Guardar
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

def cargar_logs():
    """Carga todos los logs"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def obtener_estadisticas():
    """Calcula estadísticas de uso"""
    logs = cargar_logs()
    
    if not logs:
        return {
            "total_mensajes": 0,
            "usuarios_unicos": 0,
            "mensajes_hoy": 0,
            "costo_total": 0
        }
    
    hoy = datetime.now().strftime("%Y-%m-%d")
    
    return {
        "total_mensajes": len(logs),
        "usuarios_unicos": len(set(log["usuario_id"] for log in logs)),
        "mensajes_hoy": len([l for l in logs if l["fecha"].startswith(hoy)]),
        "costo_total": sum(l.get("costo_estimado", 0) for l in logs)
    }

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
    .admin-panel { background: rgba(0,210,255,0.1); border-radius: 15px; padding: 20px; margin: 20px 0; border: 1px solid rgba(0,210,255,0.3); }
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
    
    # Estadísticas en sidebar
    stats = obtener_estadisticas()
    st.markdown("### 📊 **Estadísticas Globales**")
    st.metric("💬 Mensajes Totales", stats["total_mensajes"])
    st.metric("👥 Usuarios Únicos", stats["usuarios_unicos"])
    st.metric("📨 Mensajes Hoy", stats["mensajes_hoy"])
    
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

# ========== PANEL DE ADMIN (solo para ti) ==========
with st.expander("🔧 Panel de Control (Creador)", expanded=False):
    st.markdown("### 📊 Estadísticas Detalladas")
    
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric("Total Mensajes API", stats["total_mensajes"])
    with col_b:
        st.metric("Usuarios Diferentes", stats["usuarios_unicos"])
    with col_c:
        st.metric("Mensajes Hoy", stats["mensajes_hoy"])
    with col_d:
        st.metric("Costo Estimado", f"${stats['costo_total']:.4f}")
    
    # Ver logs recientes
    st.markdown("### 📜 Últimos 10 Mensajes Registrados")
    logs = cargar_logs()
    if logs:
        df = pd.DataFrame(logs[-10:])
        st.dataframe(df[["fecha", "usuario_id", "prompt"]])
    else:
        st.info("Aún no hay mensajes registrados.")
    
    # Botón para exportar logs
    if st.button("📥 Exportar Logs Completos"):
        if logs:
            df_full = pd.DataFrame(logs)
            csv = df_full.to_csv(index=False)
            st.download_button("Descargar CSV", csv, "kai_logs.csv", "text/csv")
        else:
            st.warning("No hay logs para exportar.")

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
# Usar IP o session_id para identificar usuarios únicos
if "usuario_id" not in st.session_state:
    import hashlib
    import streamlit as st
    # Crear ID único por sesión
    session_id = st.session_state.get("session_id", str(datetime.now().timestamp()))
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
    # Agregar mensaje del usuario
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generar respuesta
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
                
                # Registrar el uso
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
