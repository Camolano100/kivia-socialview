import streamlit as st
import google.generativeai as genai

st.title("KIVIA SocialView - Georreferenciación con IA")

# Leer API Key desde los secrets de Streamlit
API_KEY = st.secrets.get("GEMINI_API_KEY")

if not API_KEY:
    st.error("⚠️ No se encontró la clave GEMINI_API_KEY. Agrégala en 'Edit secrets' en Streamlit Cloud.")
else:
    genai.configure(api_key=API_KEY)

st.write("Bienvenido a KIVIA SocialView.")

lat = st.text_input("Ingresa la latitud")
lng = st.text_input("Ingresa la longitud")

if st.button("Buscar lugares saludables"):
    if not lat or not lng:
        st.warning("Debes ingresar ambos valores.")
    else:
        st.success(f"Buscando lugares alrededor de ({lat}, {lng})...")

