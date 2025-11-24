import streamlit as st
import os
from pathlib import Path
from src.utils.eda_sections import mostrar_seccion_md, mostrar_graficos


def mostrar_documentacion():
    st.subheader("📘 Documentación del proyecto")

    # Ruta al proyecto raíz y al archivo de documentación
    ruta_md = Path(__file__).resolve().parents[2] / "docs" / "documentacion_tienda_aurelion.md"
    ruta_flujo = Path(__file__).resolve().parents[2] / "assets" / "flujograma_aurelion.jpg"

    if ruta_md.exists():
        contenido_md = ruta_md.read_text(encoding="utf-8")

        # --- Contexto y objetivo ---
        st.markdown("### Contexto y objetivo")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Tema")
            fin = contenido_md.find("### Fuente")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Datasets de referencia ---
        st.markdown("### Datasets de referencia")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Fuente")
            fin = contenido_md.find("### Información")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Metodología ---
        st.markdown("### Metodología e implementación")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Información")
            fin = contenido_md.find("### Pseudocódigo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Pseudocódigo ---
        st.markdown("### Pseudocódigo")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Pseudocódigo") + len("### Pseudocódigo")
            fin = contenido_md.find("### Diagrama del flujo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Diagrama del flujo ---
        st.markdown("### Diagrama del flujo")

        with st.expander("Ver detalles"):
            mostrar_graficos([
                "assets/flujograma_aurelion.png",
            ], columnas=1)

                
        # --- Interpretaciones EDA – Visualizaciones ---
        st.markdown("### Interpretaciones EDA – Visualizaciones")

        # --- Distribución de variables ---
        with st.expander("Gráfica: Distribuciones de Variables numéricas"):
            mostrar_graficos([
                "assets/plots/Distribucion_de_cantidad.png",
                "assets/plots/Distribucion_de_precio_unitario.png",
                "assets/plots/Distribucion_de_total_venta.png",
            ], columnas=3)           
            mostrar_seccion_md(
                contenido_md,
                inicio_str="# Interpretaciones EDA – Visualizaciones",
                fin_str="#### 🔸 Gráfica: correlacion"
            )

        # --- Correlación ---
        with st.expander("Gráfica: Matriz de Correlación"):
            mostrar_graficos([
                "assets/plots/Matriz_de_Correlacion.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: correlacion",
                fin_str="#### 🔸 Gráfica: ventas_total_por_mes"
            )

        # --- Ventas por mes ---
        with st.expander("Gráfica: Ventas Totales por mes"):
            mostrar_graficos([
                "assets/plots/Ventas_totales_por_mes.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: ventas_total_por_mes",
                fin_str="#### 🔸 Gráfica: relacion_cantidad"
            )

        # --- Relación cantidad ---
        with st.expander("Gráfica: Relación Cantidad - Total Ventas"):
            mostrar_graficos([
                "assets/plots/Relacion_Cantidad_-_Total_Venta.png",
            ], columnas=1)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: relacion_cantidad",
                fin_str="#### 🔸 Gráfica: outliers"
            )

        # --- Outliers ---
        with st.expander("Gráfica: Outliers y Distribución"):
            mostrar_graficos([
                "assets/plots/outliers_cantidad.png",
                "assets/plots/outliers_precio_unitario.png",
                "assets/plots/outliers_total_venta.png",
            ], columnas=3)
            mostrar_seccion_md(
                contenido_md,
                inicio_str="#### 🔸 Gráfica: outliers"
            )                         
                    
    else:
        st.warning("El archivo de documentación no se encontró.")
