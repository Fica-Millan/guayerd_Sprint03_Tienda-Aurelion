#src/pages/automated_ml.py

import streamlit as st
import pandas as pd
from pycaret.classification import *

def show_automated_ml():
    """
    Interfaz de Streamlit para comparar modelos de clasificación utilizando PyCaret.

    Flujo de la función:
    1. Carga el dataset preprocesado desde 'data/dataset_ml_productos.csv'.
    2. Permite configurar el experimento de PyCaret (normalización, 
       eliminación de multicolinealidad y selección de características).
    3. Compara automáticamente todos los modelos disponibles y muestra 
       la tabla de métricas y el mejor modelo encontrado.

    Requisitos:
    - El archivo 'dataset_ml_productos.csv' debe existir en la carpeta 'data'.
    - PyCaret debe estar instalado y compatible con la versión de Python usada.

    Estados de sesión:
    - 'best_model': almacena el mejor modelo encontrado por la comparación automática
      para poder usarlo posteriormente en otra página.

    Uso:
    Esta función se integra dentro de una aplicación Streamlit como una página 
    que permite ejecutar de forma rápida un benchmarking automático de modelos 
    de clasificación para facilitar la selección del modelo a desarrollar manualmente.
    """

    st.subheader("Entrenamiento de Modelos de Machine Learning")
    st.markdown(
        '<p style="font-size: 22px;">En esta sección se comparan modelos de clasificación utilizando '
        '<span style="color: orange; font-weight:600;">PyCaret.</span></p>',
        unsafe_allow_html=True
    )


    # ==============================================================
    # 1️⃣ Cargar dataset procesado
    # ==============================================================

    st.markdown("### 1. Carga del dataset preparado")

    try:
        df = pd.read_csv("data/dataset_ml_productos.csv")
        st.success("Dataset cargado correctamente.")
        st.dataframe(df.head())
    except Exception as e:
        st.error("⚠️ No se encontró `data/dataset_ml_productos.csv`. Ejecutá la página de preprocesamiento primero.")
        st.write(e)
        st.stop()

    # objetivo
    target = "nivel_demanda"
    if target not in df.columns:
        st.error(f"La columna objetivo '{target}' no está en el dataset.")
        st.stop()

    # ==============================================================
    # 2️⃣ Configurar experimento
    # ==============================================================

    st.markdown("### 2. Configuración del experimento")

    normalize = st.checkbox(
        "Normalizar variables",
        value=True,
        help="Escala todas las variables numéricas para mejorar el rendimiento de varios modelos."
    )

    remove_multicollinearity = st.checkbox(
        "Remover multicolinealidad",
        value=True,
        help="Elimina variables muy correlacionadas entre sí para evitar sobreajuste."
    )

    if st.button("Inicializar PyCaret"):
        with st.spinner("Inicializando experimento..."):
            exp = setup(
                data=df,
                target=target,
                session_id=789,
                normalize=normalize,
                remove_multicollinearity=remove_multicollinearity,
                verbose=False
            )
        st.success("Experimento inicializado.")
        st.write("Configuración establecida exitosamente:")
        st.code(exp)
        
        # Mostrar detalles internos de la configuración
        st.markdown("#### 🟠 Información del experimento")

        # Obtener datos del split
        train_df = get_config("train")
        test_df = get_config("test")

        train_count = train_df.shape[0]
        test_count = test_df.shape[0]
        total = train_count + test_count

        train_ratio = train_count / total
        test_ratio = test_count / total

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Train/Test Split:** {train_ratio:.2f} / {test_ratio:.2f}")

            # Obtener folds desde fold_generator
            fold_value = get_config("fold_generator").n_splits
            st.write("**Cross-validation folds:**", fold_value)

        with col2:
            st.write(f"**Registros en entrenamiento:** {train_count}")
            st.write(f"**Registros en test:** {test_count}")

    # ==============================================================
    # 3️⃣ Comparar modelos
    # ==============================================================

    st.markdown("### 3. Comparación automática de modelos")

    if st.button("Comparar todos los modelos"):
        with st.spinner("Entrenando y comparando modelos..."):
            best_model = compare_models(sort="AUC")

        st.success("Comparación completada.")
        
        # Mostrar tabla de métricas
        results = pull()
        st.write("### 📊 Métricas de los modelos comparados")
        st.dataframe(results)

        st.write("### 🏆 Mejor modelo encontrado:")
        st.write(best_model)
        
        # Guardar temporalmente
        st.session_state["best_model"] = best_model
