# main.py

import streamlit as st
import os
from PIL import Image
from src.pages.general_info import show_general_info
from src.pages.statistics import show_statistics
from src.pages.documentacion import mostrar_documentacion
from src.pages.automated_eda import show_automated_eda
from src.pages.diagnostic_eda import show_diagnostic_eda
from src.pages.ml_preprocessing import show_ml_preprocessing
from src.pages.automated_ml import show_automated_ml
from src.pages.random_forest_manual import show_random_forest_manual

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Tienda Aurelion", page_icon="🛒", layout="wide")

# --- ENCABEZADO ---
ruta_actual = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_actual, "assets", "logo_aurelion.png")
col1, col2 = st.columns([1, 4])
with col1:
    st.image(ruta_logo, width=180)
with col2:
    st.title("Proyecto Tienda Aurelion")
    st.markdown("Exploración interactiva de datos de ventas y documentación del proyecto.")


# Título grande en la sidebar
st.sidebar.markdown(
    '<h2 style="font-size: 24px;">Menú principal</h2>',
    unsafe_allow_html=True
)

# Menú tipo radio debajo
opcion = st.sidebar.radio(
    "",  # dejamos vacío el label porque ya pusimos el título    
    ["Información general", "Estadísticas iniciales", "EDA Automatizado", "EDA Diagnóstico", 
     "Preprocesamiento ML", "ML Automatizado", "Entrenamiento Random Forest", "Ver documentación"]
)

# --- Lógica según opción ---
if opcion == "Información general":
    show_general_info()
elif opcion == "Estadísticas iniciales":
    show_statistics()
elif opcion == "EDA Automatizado":
    show_automated_eda()
elif opcion == "EDA Diagnóstico":
    show_diagnostic_eda()
elif opcion == "Preprocesamiento ML":
    show_ml_preprocessing()
elif opcion == "ML Automatizado":
    show_automated_ml()    
elif opcion == "Entrenamiento Random Forest":
    show_random_forest_manual() 
elif opcion == "Ver documentación":
    mostrar_documentacion()
    
# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 15px; color: gray;'>
        <p><b>Sprint 03 – Fundamentos de Inteligencia Artificial</b><br>
        Programa Guayerd e IBM</p>
        <p>Desarrollado por <b>Yesica Fica Millán</b> – <a href="https://www.linkedin.com/in/yesica-fica-millan" target="_blank">LinkedIn</a></p>
        <p style='font-size:13px;'>© 2025 Proyecto Tienda Aurelion</p>
    </div>
    """,
    unsafe_allow_html=True
)
