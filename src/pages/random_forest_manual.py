# src/pages/random_forest_manual.py

import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    RocCurveDisplay
)

from src.utils.figures import mostrar_fig
from src.utils.palette import PALETA


# ===============================================================
# ENTRENAMIENTO MANUAL RANDOM FOREST
# ===============================================================
def show_random_forest_manual():

    st.subheader("Entrenamiento Manual")
    st.markdown(
        '<p style="font-size: 22px;">Entrená manualmente un modelo '
        '<span style="color: orange; font-weight:600;">Random Forest</span> ajustando los parámetros.</p>',
        unsafe_allow_html=True
    )

    # ===============================================================
    # 1️⃣ CARGA DEL DATASET
    # ===============================================================
    st.markdown("### 1. Cargar Dataset Procesado")

    try:
        # Se intenta cargar el dataset procesado previamente
        df = pd.read_csv("data/dataset_ml_productos.csv")
        st.success("Dataset cargado correctamente.")
        
        # Se muestra un preview de las primeras filas
        st.dataframe(df.head())
        
    except FileNotFoundError:
        # Detiene la ejecución si el dataset no existe
        st.error("⚠️ No se encontró el archivo data/dataset_ml_productos.csv.")
        st.stop()

    # ===============================================================
    # 2️⃣ TARGET Y FEATURES - CORREGIDO
    # ===============================================================
    st.markdown("### 2. Variable Objetivo")

    # Variable que se quiere predecir
    target = "nivel_demanda"
    
    # Validación de existencia del target
    if target not in df.columns:
        st.error(f"❌ No se encuentra la columna '{target}' en el dataset")
        st.stop()
    
    # Selección automática de features eliminando columnas no deseadas
    features= [col for col in df.columns 
              if col not in ['nivel_demanda', 'total_unidades', 
                            'total_ventas', 'unidades_por_transaccion']]
    
    # Información al usuario
    st.info(f"**Target:** `{target}` (clasificación multiclase: 0=baja, 1=media, 2=alta)")
    st.write(f"**Features:** {len(features)} variables")

    # ===============================================================
    # 3️⃣ PARÁMETROS DEL MODELO
    # ===============================================================
    st.markdown("### 3. Configuración del Modelo")

    # Distribución visual en dos columnas
    col1, col2 = st.columns(2)

    with col1:
        # Hiperparámetros principales
        n_estimators = st.slider("Cantidad de árboles", 50, 300, 100)
        max_depth = st.slider("Profundidad máxima", 2, 20, 10)
        
        # Balanceo automático basado en distribución del target
        balancear = st.checkbox("Balancear clases", value=True)

    with col2:
        # Proporción del conjunto de test
        test_size = st.slider("Tamaño del Test (%)", 10, 40, 20) / 100
        
        # Semilla para reproducibilidad
        random_state = st.number_input("Random State", value=789)

    # ===============================================================
    # 4️⃣ VALIDACIONES
    # ===============================================================
    st.markdown("### 4. Validaciones del Dataset")

    # Validación de valores faltantes
    if df.isna().sum().sum() > 0:
        st.error("❌ Hay valores faltantes en el dataset")
        st.stop()
    else:
        st.success("✅ No hay valores faltantes")

    # --- Visualización de distribución del target ---
    st.subheader("Distribución del Target")
    distribucion = df[target].value_counts().sort_index()
    st.dataframe(distribucion.rename_axis("Clase").reset_index(name="Cantidad"))

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=distribucion.index, y=distribucion.values, palette="viridis", ax=ax)
    ax.set_title("Distribución de Clases - Nivel de Demanda")
    ax.set_xlabel("Nivel de Demanda (0=baja, 1=media, 2=alta)")
    ax.set_ylabel("Cantidad de Productos")
    mostrar_fig(fig)

    # Advertencia por dataset pequeño
    if len(df) < 100:
        st.warning(
            "⚠️ El dataset es pequeño (menos de 100 filas). "
            "Para obtener un modelo más robusto y con mejor capacidad de generalización, "
            "sería recomendable contar con más datos."
        )

    # ===============================================================
    # 5️⃣ ENTRENAR MODELO
    # ===============================================================
    st.markdown("### 5. Entrenar Modelo")

    # Solo entrena el modelo si se presiona el botón
    if st.button("🎯 Entrenar modelo Random Forest", type="primary"):

        with st.spinner("Entrenando modelo..."):
            
            # Separación de datos en X (features) e y (target)
            X = df[features]
            y = df[target]

            # División del dataset respetando la proporción original de clases
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, 
                test_size=test_size, 
                random_state=random_state,
                stratify=y  # mantiene proporciones de la variable objetivo
            )

            # Creación del modelo Random Forest
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                random_state=random_state,
                n_jobs=-1,
                class_weight='balanced' if balancear else None
            )
            
            # Entrenamiento del modelo
            model.fit(X_train, y_train)

        st.success("✅ Modelo entrenado correctamente")

        # ===============================================================
        # 6️⃣ VALIDACIÓN CRUZADA
        # ===============================================================
        st.markdown("### 6. Validación Cruzada (5 folds)")
        
        # Ajuste dinámico del número de folds:
        # Para datasets pequeños, usar muchos folds puede causar errores.
        # Se define la cantidad como el mínimo entre 5 y (filas/3), garantizando suficientes datos por fold.
        cv_folds = min(5, len(df) // 3)
        
        # Validación cruzada para Accuracy.
        # cross_val_score entrena el modelo "cv_folds" veces con diferentes particiones.
        cv_accuracy = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")
        
        # Validación cruzada para F1 Weighted (maneja clases desbalanceadas)
        cv_f1 = cross_val_score(model, X, y, cv=cv_folds, scoring="f1_weighted")

        # Tabla resumen por fold
        cv_table = pd.DataFrame({
            "Fold": range(1, cv_folds + 1),
            "Accuracy": cv_accuracy,
            "F1 Weighted": cv_f1
        })

        st.dataframe(cv_table.style.format("{:.4f}"))

        # Mostrar métricas promedio
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy Promedio", f"{cv_accuracy.mean():.4f}")
        with col2:
            st.metric("F1 Score Promedio", f"{cv_f1.mean():.4f}")

        # ===============================================================
        # 7️⃣ MÉTRICAS DEL TEST
        # ===============================================================
        st.markdown("### 7. Métricas del Test")

        # Predicciones sobre los datos de test
        y_pred = model.predict(X_test)

        # Tabla con métricas clásicas de clasificación
        metricas = pd.DataFrame({
            "Métrica": ["Accuracy", "Precision", "Recall", "F1 Score"],
            "Valor": [
                accuracy_score(y_test, y_pred),
                precision_score(y_test, y_pred, average='weighted'),  # pondera según frecuencia de clases
                recall_score(y_test, y_pred, average='weighted'), 
                f1_score(y_test, y_pred, average='weighted'),
            ]
        })

        st.dataframe(metricas.style.format({"Valor": "{:.4f}"}))

        # ===============================================================
        # 8️⃣ CURVA ROC
        # ===============================================================
        st.markdown("### 8. Curva ROC / AUC")

        # Para clasificación multiclase, se usa el enfoque One-vs-Rest (OvR)
        y_proba = model.predict_proba(X_test)
        
        # AUC macro promedia el AUC de cada clase
        auc_macro = roc_auc_score(y_test, y_proba, multi_class="ovr", average="macro")

        fig, ax = plt.subplots(figsize=(8, 6))
        colores = plt.cm.tab10.colors

        # Dibujar una curva ROC por cada clase
        for i, clase in enumerate(model.classes_):
            RocCurveDisplay.from_predictions(
                y_test == clase,    # binariza la clase actual
                y_proba[:, i],      # probabilidades de esa clase
                name=f"Clase {clase}",
                ax=ax,
                color=colores[i]
            )

        # Estética del gráfico
        ax.set_title(
                "Curvas ROC (Multiclase - One vs Rest)",
                fontsize=16, fontweight="bold", color=PALETA["secundario"],
                pad=15
            )
        ax.set_xlabel("Tasa de Falsos Positivos (FPR)", fontsize=12, fontweight="bold")
        ax.set_ylabel("Tasa de Verdaderos Positivos (TPR)", fontsize=12, fontweight="bold")
        ax.grid(alpha=0.2)
        
        ax.legend(
                title="Clases",
                fontsize=10,
                title_fontsize=11,
                loc="lower right",
                frameon=True
            )
        mostrar_fig(fig)

        # Valor del AUC macro
        st.write(f"**AUC (macro):** {auc_macro:.4f}")

        # ===============================================================
        # 9️⃣ MATRIZ DE CONFUSIÓN
        # ===============================================================
        st.markdown("### 9. Matriz de Confusión")

        # Calcular matriz de confusión
        cm = confusion_matrix(y_test, y_pred)
        labels = model.classes_

        fig, ax = plt.subplots(figsize=(6, 5))
        
        # Heatmap con anotaciones
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap=sns.diverging_palette(25, 220, s=70, l=40, as_cmap=True), 
            center=0,
            xticklabels=labels,
            yticklabels=labels,
            cbar=True,
            ax=ax
        )
        
        # Estilo del gráfico
        ax.set_title("Matriz de Confusión", fontsize=14, fontweight="bold", color=PALETA["secundario"])
        ax.set_xlabel("Predicción", fontsize=12, fontweight="bold")
        ax.set_ylabel("Real", fontsize=12, fontweight="bold")
        mostrar_fig(fig)

        # ===============================================================
        # 🔸 IMPORTANCIAS
        # ===============================================================
        st.markdown("### 10. Importancia de Variables")

        # Obtener importancia entregada por el Random Forest
        importances = pd.DataFrame({
            "variable": features,
            "importancia": model.feature_importances_
        }).sort_values("importancia", ascending=False)

        st.dataframe(importances)

        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Gráfico de barras horizontal
        sns.barplot(
            data=importances.sort_values("importancia", ascending=True),
            x="importancia",
            y="variable",
            color=PALETA["acento1"],
            ax=ax
        )
        
        # Títulos y etiquetas
        ax.set_title(
            "Importancia de Variables",
            fontsize=14,
            fontweight="bold",
            color=PALETA["secundario"]
        )
        ax.set_xlabel("Importancia", fontsize=12,fontweight="bold")
        ax.set_ylabel("Variables", fontsize=12,fontweight="bold")
        mostrar_fig(fig)

        # ===============================================================
        # 1️⃣1️⃣ DESCARGAR MODELO
        # ===============================================================
        st.markdown("### 11. Descargar Modelo Entrenado")

        # Convertir modelo a bytes para descarga
        model_bytes = pickle.dumps(model)
        
        st.download_button(
            "📥 Descargar Modelo (.pkl)",
            model_bytes,
            "random_forest_manual.pkl",
            mime="application/octet-stream"
        )

        st.success("✅ Proceso completado. Modelo listo para usar.")
        
        # Guardado automático en /models
        os.makedirs("models", exist_ok=True)    # Crear carpeta 'models' si no existe

        ruta_modelo = f"models/random_forest_manual.pkl"

        # Guardar el modelo entrenado
        with open(ruta_modelo, "wb") as f:
            pickle.dump(model, f)

        st.info(f"📁 Modelo guardado automáticamente en: `{ruta_modelo}`")


    # ===============================================================
    # 1️⃣2️⃣ Classification Report (Métricas por clase)
    # ===============================================================
    st.markdown("### 12. Métricas por Clase (Classification Report)")

    # Obtener reporte en dict
    report = classification_report(
        y_test, y_pred, 
        output_dict=True, 
        zero_division=0
    )

    # Convertir a DataFrame solo para clases
    report_df = pd.DataFrame(report).transpose()
    report_df = report_df.loc[[str(c) for c in model.classes_], ["precision", "recall", "f1-score"]]

    # Mostrar tabla
    st.dataframe(
        report_df.style.format("{:.3f}")
    )

    # Heatmap
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.heatmap(
        report_df,
        annot=True,
        fmt=".3f",
        cmap="Blues",
        cbar=True,
        ax=ax
    )

    ax.set_title(
        "Classification Report - Métricas por Clase",
        fontsize=14,
        fontweight="bold",
        color=PALETA["secundario"]
    )

    ax.set_xlabel("Métrica")
    ax.set_ylabel("Clase")

    mostrar_fig(fig)

    # ===============================================================
    # 1️⃣4️⃣ Curva de Aprendizaje (Learning Curve)
    # ===============================================================
    st.markdown("### 14. Curva de Aprendizaje (Learning Curve)")

    from sklearn.model_selection import learning_curve
    import numpy as np

    train_sizes, train_scores, test_scores = learning_curve(
        model, X, y,
        cv=cv_folds,
        train_sizes=np.linspace(0.2, 1.0, 5),
        scoring="accuracy",
        n_jobs=-1
    )

    train_mean = train_scores.mean(axis=1)
    test_mean = test_scores.mean(axis=1)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(train_sizes, train_mean, marker="o", label="Entrenamiento")
    ax.plot(train_sizes, test_mean, marker="o", label="Validación")

    ax.set_title(
        "Learning Curve - Accuracy",
        fontsize=15,
        fontweight="bold",
        color=PALETA["secundario"]
    )

    ax.set_xlabel("Cantidad de muestras de entrenamiento")
    ax.set_ylabel("Accuracy")
    ax.grid(alpha=0.2)
    ax.legend()

    mostrar_fig(fig)
