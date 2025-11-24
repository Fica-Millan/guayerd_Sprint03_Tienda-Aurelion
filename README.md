# Proyecto Tienda Aurelion

## 📝 Descripción
Este proyecto consiste en una aplicación interactiva llamada **Tienda Aurelion**, desarrollada en Python utilizando **Streamlit**. La app permite realizar análisis exploratorio de datos (EDA) sobre las ventas, productos y clientes de la tienda, ofreciendo visualizaciones interactivas y análisis estadísticos detallados.

## 🌟 Características principales

- **Información General**: Vista previa y detalles de cada dataset.
- **Estadísticas**: Análisis descriptivo con visualizaciones personalizadas.
- **EDA Automatizado**: Perfilado completo del dataset unificado usando `ydata-profiling`.
- **EDA Diagnóstico**: Análisis detallado con:
  - Detección de outliers
  - Matrices de correlación
  - Series temporales de ventas
  - Top productos por categoría
  - Visualizaciones guardadas automáticamente
- **Documentación**: Acceso a la documentación técnica del proyecto.

## 📁 Estructura del proyecto

```
├── main.py                     # Archivo principal de la aplicación
├── assets/                     # Recursos estáticos (imágenes, logos)
│   └── plots/                  # Visualizaciones generadas por la app
├── data/                       # Datasets del proyecto
│   ├── clientes.xlsx
│   ├── productos.xlsx
│   ├── ventas.xlsx
│   ├── detalle_ventas.xlsx
│   └── df_tienda_aurelion.csv  # Dataset unificado (generado automáticamente)
├── docs/                       # Documentación del proyecto
├── src/                        # Módulos Python del proyecto
│   ├── __init__.py
│   ├── data_loader.py          # Funciones de carga y unificación de datos
│   ├── pages/                  # Páginas de la aplicación
│   │   ├── __init__.py
│   │   ├── general_info.py     # Información general de datasets
│   │   ├── statistics.py       # Estadísticas descriptivas
│   │   ├── automated_eda.py    # EDA automatizado con ydata-profiling
│   │   ├── diagnostic_eda.py   # EDA diagnóstico detallado
│   │   └── documentacion.py    # Visualización de documentación
│   │
│   └── utils/                  # Utilidades y helpers
│       ├── __init__.py
│       ├── classification.py   # Funciones de clasificación
│       ├── docs_loader.py      # Carga de documentación
│       ├── figures.py          # Generación de gráficos
│       ├── palette.py          # Paleta de colores
│       ├── rules.py            # Reglas de validación
│       └── validation.py       # Validación de datos
│
└── requirements.txt            # Dependencias del proyecto
```

## ⚙️ Preparación del entorno

1. Clonar o descargar los archivos del proyecto.
2. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv311
```

3. Activar el entorno virtual:
```bash
# Windows
venv311\Scripts\activate

# Mac/Linux:
source venv311/bin/activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución de la aplicación

Con el entorno virtual activo, ejecutar:

```bash
streamlit run tienda_aurelion.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado. Si no se abre, copia la URL que muestra Streamlit (normalmente http://localhost:8501).

## 📊 Datasets

La aplicación trabaja con los siguientes datasets:

- `clientes.xlsx`: Información de clientes
- `productos.xlsx`: Catálogo de productos
- `ventas.xlsx`: Registro de ventas
- `detalle_ventas.xlsx`: Detalle de productos vendidos
- `df_tienda_aurelion.csv`: Dataset unificado (generado automáticamente en la primera ejecución)

## 🛠️ Tecnologías utilizadas

- Python 3.11
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- ydata-profiling (pandas-profiling)
- NumPy
- PIL
   