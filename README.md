# RATIQ — Financial Intelligence System

**Del dato contable al diagnóstico ejecutivo en un mismo proceso.**

RATIQ es un proyecto desarrollado como Trabajo Fin de Máster cuyo objetivo es transformar información contable procedente de un ERP en un sistema automatizado de análisis financiero.

El flujo completo integra **Python, Machine Learning y Power BI** para pasar de datos contables en bruto a estados financieros, ratios, previsiones y diagnóstico ejecutivo.

## ¿Qué hace RATIQ?

El sistema automatiza las principales etapas del análisis financiero:

1. **Carga y validación de datos contables**
2. **Limpieza y controles de calidad**
3. **Clasificación contable y financiera**
4. **Construcción mensual de Balance y PyG**
5. **Cálculo e interpretación de ratios financieros**
6. **Forecast financiero a 12 meses**
7. **Generación de escenarios Base, Optimista y Pesimista**
8. **Preparación del modelo para Power BI**
9. **Visualización ejecutiva de KPIs, riesgos y tendencias**

## Arquitectura

`ERP / Business Central → CSV → Python → Power BI`

Python actúa como **motor financiero**, mientras que Power BI constituye la capa de visualización y análisis ejecutivo.

## Tecnologías

- Python
- Pandas / NumPy
- Scikit-learn
- Jupyter Notebook
- Power BI
- DAX
- Power Query

## Forecast

El sistema utiliza modelos de **regresión lineal temporal**, comparando:

- tendencia;
- tendencia + estacionalidad mensual.

Los modelos se validan mediante **backtesting temporal** y se seleccionan según su **MAE**, evitando utilizar modelos excesivamente complejos con un histórico reducido.

## Objetivo

RATIQ no pretende generar más datos, sino **aprovechar mejor los datos que ya existen**.

El proyecto busca reducir trabajo manual, aumentar la trazabilidad del análisis financiero y convertir información contable infrautilizada en:

**Información → Indicadores → Diagnóstico → Decisión**

---

### RATIQ

**Automatizar el camino entre el dato contable y la decisión financiera.**