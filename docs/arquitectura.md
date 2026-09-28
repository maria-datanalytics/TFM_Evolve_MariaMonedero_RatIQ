# Arquitectura del sistema

## 1. Objetivo

El proyecto implementa un pipeline reproducible de análisis financiero que transforma datos contables originales en información preparada para análisis, forecasting y visualización en Power BI.

La arquitectura se ha diseñado priorizando:

* simplicidad;
* reproducibilidad;
* trazabilidad;
* controles de calidad;
* separación de responsabilidades entre notebooks;
* facilidad de mantenimiento.

El flujo general es:

```text
Datos originales
      ↓
NB1 · Carga y calidad
      ↓
NB2 · Maestro financiero
      ↓
NB3 · Estados financieros
      ↓
NB4 · Ratios y métricas
      ↓
NB5 · Forecast y escenarios
      ↓
NB6 · Modelo final Power BI
      ↓
data/powerbi/
```

El pipeline completo puede ejecutarse mediante:

```bash
python run_pipeline.py
```

Si cualquiera de los notebooks produce un error crítico, la ejecución se detiene y los notebooks posteriores no se ejecutan.

---

## 2. Estructura del proyecto

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   │   ├── 01/
│   │   ├── 02/
│   │   ├── 03/
│   │   ├── 04/
│   │   └── 05/
│   └── powerbi/
│
├── docs/
│
├── notebooks/
│   ├── NB1_Carga_Calidad.ipynb
│   ├── NB2_Maestro_Financiero.ipynb
│   ├── NB3_Estados_Financieros.ipynb
│   ├── NB4_Ratios.ipynb
│   ├── NB5_Forecast.ipynb
│   └── NB6_Modelo_PowerBI.ipynb
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## 3. Capas de datos

### `data/raw`

Contiene los archivos originales utilizados como fuente.

Estos archivos no deben ser modificados durante el pipeline.

Las principales fuentes del proyecto son:

* contabilidad general;
* balances históricos;
* plan o maestro de cuentas.

---

### `data/processed`

Contiene las salidas intermedias generadas por los notebooks.

Cada notebook escribe en su propia carpeta:

```text
01/ → limpieza y calidad
02/ → maestro financiero
03/ → estados financieros
04/ → métricas y ratios
05/ → forecast y escenarios
```

Esta separación permite identificar fácilmente qué notebook ha generado cada archivo.

---

### `data/powerbi`

Contiene exclusivamente las tablas finales preparadas para ser consumidas por Power BI.

Power BI no necesita acceder directamente a los archivos originales ni reconstruir la lógica financiera realizada previamente en Python.

---

## 4. Responsabilidad de cada notebook

### NB1 · Carga y calidad

Responsable de:

* cargar las fuentes originales;
* validar columnas y estructura;
* normalizar cuentas y fechas;
* separar registros válidos y excluidos;
* detectar cuentas sin maestro;
* transformar los balances;
* realizar controles entre contabilidad y balances.

No realiza clasificación financiera ni cálculo de ratios.

---

### NB2 · Maestro financiero

Responsable de transformar el plan contable en una estructura útil para análisis financiero.

Clasifica las cuentas por:

* estado financiero;
* masa financiera;
* categoría;
* subcategoría;
* naturaleza;
* circulante;
* driver de negocio.

También integra dicha clasificación con la contabilidad.

---

### NB3 · Estados financieros

Responsable de construir:

* Balance mensual;
* PyG mensual;
* PyG acumulada YTD;
* principales magnitudes financieras;
* análisis por centro de coste.

Incluye controles críticos de cuadre.

Si el Balance no cuadra dentro de la tolerancia definida, el pipeline se detiene.

---

### NB4 · Ratios y métricas

Responsable de calcular:

* ratios financieros;
* métricas MTD;
* métricas YTD;
* saldos de cierre;
* métricas LTM;
* comparativas frente al año anterior;
* variaciones absolutas y porcentuales;
* análisis DuPont.

También prepara tablas específicamente diseñadas para Power BI.

---

### NB5 · Forecast y escenarios

Responsable de:

* entrenar modelos predictivos sencillos;
* validar los modelos temporalmente;
* seleccionar el mejor modelo por variable;
* generar previsiones de 12 meses;
* construir escenarios Base, Optimista y Pesimista;
* recalcular estados y ratios previstos.

---

### NB6 · Modelo final Power BI

Responsable de organizar las salidas anteriores en un modelo de datos final.

Genera:

* dimensiones;
* tablas de hechos;
* diagnóstico financiero;
* alertas;
* resumen de escenarios.

NB6 no debe reconstruir estados financieros ni recalcular ratios ya definidos previamente.

---

## 5. Automatización

El archivo:

```text
run_pipeline.py
```

ejecuta los notebooks secuencialmente:

```text
NB1
→ NB2
→ NB3
→ NB4
→ NB5
→ NB6
```

El proceso utiliza una estrategia fail-fast.

Si un notebook falla:

```text
NB1 ✅
NB2 ✅
NB3 ❌
NB4 no ejecutado
NB5 no ejecutado
NB6 no ejecutado
```

Esto evita generar resultados derivados de información incompleta o inconsistente.

---

## 6. Separación de responsabilidades

La lógica del proyecto se divide entre Python y Power BI.

### Python

Responsable de:

* limpieza;
* validación;
* clasificación;
* estados financieros;
* ratios;
* forecasting;
* escenarios;
* lógica financiera;
* preparación de tablas.

### Power BI

Responsable principalmente de:

* filtros;
* interacción;
* visualización;
* storytelling;
* navegación;
* presentación ejecutiva.

De esta forma se evita duplicar lógica financiera entre Python y DAX.

---

## 7. Principio de diseño

La arquitectura busca que cualquier actualización futura de los datos pueda seguir el mismo flujo:

```text
Nuevos datos
   ↓
python run_pipeline.py
   ↓
Validaciones
   ↓
Nuevos CSV
   ↓
Actualizar Power BI
```

Esto convierte el proyecto en un proceso reproducible y no únicamente en un análisis realizado una sola vez.
