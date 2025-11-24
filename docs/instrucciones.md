# Documentación de Uso de Inteligencia Artificial

## 📌 Índice

- [Documentación de Uso de Inteligencia Artificial](#documentación-de-uso-de-inteligencia-artificial)
  - [📌 Índice](#-índice)
- [Introducción](#introducción)
- [Sprint 01 -- Registro de uso de IA](#sprint-01----registro-de-uso-de-ia)
  - [1. Creación de aplicación](#1-creación-de-aplicación)
  - [2. Creación de aplicación con Streamlit](#2-creación-de-aplicación-con-streamlit)
  - [3. Duplicación de columnas en la vista previa de datos](#3-duplicación-de-columnas-en-la-vista-previa-de-datos)
  - [4. Error con `st.write()` y parámetro no reconocido](#4-error-con-stwrite-y-parámetro-no-reconocido)
  - [5. Scroll vertical en tablas](#5-scroll-vertical-en-tablas)
  - [6. Altura dinámica en tablas](#6-altura-dinámica-en-tablas)
  - [7. Tamaño y centrado del flujograma](#7-tamaño-y-centrado-del-flujograma)
  - [Resumen Sprint 01](#resumen-sprint-01)
- [Sprint 02 -- Registro de uso de IA](#sprint-02----registro-de-uso-de-ia)
  - [1. Refinamiento de la arquitectura de la aplicación](#1-refinamiento-de-la-arquitectura-de-la-aplicación)
  - [2. Sección de Outliers y Distribuciones](#2-sección-de-outliers-y-distribuciones)
  - [3. Corrección en gráficos de boxplot y stripplot](#3-corrección-en-gráficos-de-boxplot-y-stripplot)
  - [4. Unificación de estilos y paleta de colores](#4-unificación-de-estilos-y-paleta-de-colores)
  - [5. Ajustes en visualizaciones de Streamlit](#5-ajustes-en-visualizaciones-de-streamlit)
  - [6. Depuración de duplicación de columnas en EDA](#6-depuración-de-duplicación-de-columnas-en-eda)
  - [7. Revisión de código para evitar errores de rendering](#7-revisión-de-código-para-evitar-errores-de-rendering)
  - [Resumen Sprint 02](#resumen-sprint-02)
- [Creación del Logo](#creación-del-logo)
- [Conclusión](#conclusión)

------------------------------------------------------------------------

# Introducción

El proyecto **Tienda Aurelion** forma parte del programa *Fundamentos de
Inteligencia Artificial* (Guayerd + IBM). A lo largo del desarrollo de
los distintos Sprints, se utilizaron herramientas de asistencia como
**ChatGPT** y **GitHub Copilot** para resolver dudas técnicas, optimizar
el código e implementar funcionalidades.

Esta documentación registra de forma clara y transparente **qué partes
del desarrollo fueron asistidas por IA**, qué problemas se resolvieron y
qué soluciones se adoptaron.

------------------------------------------------------------------------

# Sprint 01 -- Registro de uso de IA

## 1. Creación de aplicación

**Problema:** se pidió una propuesta integral para construir la app
completa.

**Intervención de IA:** ChatGPT generó una propuesta completa de
arquitectura y desarrollo.

**Decisión:** se rechazó para avanzar paso a paso según los
requerimientos académicos.

------------------------------------------------------------------------

## 2. Creación de aplicación con Streamlit

La IA asistió con: - instalación de dependencias - estructura base del
archivo principal - carga de datos, menú lateral y secciones - lectura
de archivos .md dentro de la app

Se generó un script base funcional para iniciar el proyecto.

------------------------------------------------------------------------

## 3. Duplicación de columnas en la vista previa de datos

**Problema:** se mostraba dos veces la columna ID.

**Solución asistida por IA:**

``` python
df.reset_index(drop=True)
```

Eliminó el índice duplicado y mejoró la visualización.

------------------------------------------------------------------------

## 4. Error con `st.write()` y parámetro no reconocido

**Error detectado:**\
`TypeError: WriteMixin.write() got an unexpected keyword argument 'use_container_width'`

**Corrección propuesta por IA:**

``` python
st.dataframe(df.describe(include="all"), use_container_width=True)
```

------------------------------------------------------------------------

## 5. Scroll vertical en tablas

Se ajustó el `height` para mejorar la lectura:

``` python
st.dataframe(..., height=450)
```

------------------------------------------------------------------------

## 6. Altura dinámica en tablas

La IA confirmó que Streamlit no admite altura "auto". Solo valores
fijos.

------------------------------------------------------------------------

## 7. Tamaño y centrado del flujograma

**Problemas:** imagen muy grande y alineada a la izquierda.

**Soluciones proporcionadas:** - `width=600` para controlar tamaño -
columnas para alinear al centro

------------------------------------------------------------------------

## Resumen Sprint 01

El primer Sprint se centró en la creación de la aplicación base y su
correcta visualización. La IA fue usada para resolver errores de
ejecución, optimizar la interfaz y asistir en decisiones técnicas sobre
Streamlit.

------------------------------------------------------------------------

# Sprint 02 -- Registro de uso de IA

## 1. Refinamiento de la arquitectura de la aplicación

Reorganización del layout para lograr una estructura más clara y
consistente. La IA propuso: - reordenamiento del flujo de EDA - limpieza
de secciones repetidas - mejor separación de componentes

------------------------------------------------------------------------

## 2. Sección de Outliers y Distribuciones

Se implementaron: - `st.expander` - `st.columns(3)` - iteración
automatizada sobre variables numéricas

La IA proporcionó fragmentos para violin plots, swarmplots y boxplots.

Se rechaza los graficos de violin plots.

------------------------------------------------------------------------

## 3. Corrección en gráficos de boxplot y stripplot

Ajustes recomendados por IA: - separación de capas entre seaborn y
matplotlib - uso de `flierprops` - evitar parámetros incompatibles

------------------------------------------------------------------------

## 4. Unificación de estilos y paleta de colores

Se estandarizó: - paleta `PALETA[...]` - tamaños de gráficos -
estructura común entre visualizaciones

------------------------------------------------------------------------

## 5. Ajustes en visualizaciones de Streamlit

La IA recomendó tamaños fijos (`figsize=(5,4)`) para mantener
consistencia visual.

------------------------------------------------------------------------

## 6. Depuración de duplicación de columnas en EDA

IA recomendó: - verificar `df.reset_index(drop=True)` - revisar lectura
del CSV - evitar crear columnas redundantes

------------------------------------------------------------------------

## 7. Revisión de código para evitar errores de rendering

Se corrigieron parámetros inválidos y errores típicos de autocomplete.

------------------------------------------------------------------------

## Resumen Sprint 02

Este sprint consolidó la calidad visual del EDA y la interacción dentro
de Streamlit. La IA funcionó como soporte para ajustes finos y
depuración.

------------------------------------------------------------------------

# Creación del Logo

Prompt utilizado en Copilot Desktop:

    quiero que hagas el logo para un supermercado minorista llamado Aurelion, quiero que tenga colores vibrantes, que sea de tamaño rectangular, donde se vean diferentes productos comestibles y en el medio que se destaque el nombre del comercio.

------------------------------------------------------------------------

# Conclusión

La integración de IA permitió acelerar el desarrollo, resolver problemas
técnicos y mantener coherencia visual y funcional en el proyecto Tienda
Aurelion. Esta documentación registra de manera transparente dónde y
cómo fue utilizada la inteligencia artificial.
