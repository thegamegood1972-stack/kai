import streamlit as st

st.set_page_config(page_title="Prueba", layout="centered")
st.title("🔧 Prueba de funcionamiento")

st.write("Si ves este mensaje, Streamlit Cloud está funcionando correctamente.")
st.success("✅ La aplicación se despliega sin errores")

# Botón de prueba
if st.button("Haz clic aquí"):
    st.balloons()
    st.write("¡Funciona!")
