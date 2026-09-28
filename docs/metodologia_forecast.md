# ARCHIVO: metodologia_forecast.md

# Metodología de forecasting y escenarios

## 1. Objetivo

El módulo predictivo tiene como objetivo generar una previsión sencilla y defendible de las principales magnitudes financieras.

Debido al tamaño limitado del histórico mensual, se priorizan modelos:

* sencillos;
* interpretables;
* reproducibles;
* fáciles de validar.

El objetivo no es maximizar la complejidad algorítmica sino obtener previsiones útiles para apoyar el análisis financiero.

---

## 2. Horizonte

El sistema genera:

```text
12 meses de forecast
```

El primer periodo previsto corresponde al mes inmediatamente posterior al último mes histórico disponible.

Por tanto, el forecast no está asociado a un año fijo.

Si el histórico termina en diciembre de 2023:

```text
Forecast → enero 2024 - diciembre 2024
```

Si en el futuro termina en junio de 2025:

```text
Forecast → julio 2025 - junio 2026
```

---

## 3. Histórico mínimo

Se exige un mínimo de:

```text
24 meses
```

Además:

* no puede haber meses duplicados;
* no puede haber huecos dentro de la serie temporal.

---

## 4. Modelos utilizados

Se comparan dos modelos.

### Modelo 1 · Tendencia

Regresión lineal utilizando como predictor únicamente el tiempo.

Conceptualmente:

```text
y = a + b · tiempo
```

Permite capturar una evolución creciente o decreciente de la variable.

---

### Modelo 2 · Tendencia + estacionalidad

Regresión lineal que incorpora:

* tendencia temporal;
* mes del año.

Conceptualmente:

```text
Variable =
Tendencia
+ efecto Enero
+ efecto Febrero
+ ...
+ efecto Diciembre
```

Esto permite capturar comportamientos estacionales repetitivos.

---

## 5. Variables modeladas

El forecast se aplica directamente a magnitudes financieras base.

Entre ellas pueden encontrarse:

### PyG

* ingresos;
* aprovisionamientos;
* gastos de personal;
* otros gastos operativos;
* amortizaciones;
* resultado financiero.

### Balance

* activo corriente;
* activo no corriente;
* pasivo corriente;
* pasivo no corriente;
* tesorería;
* clientes;
* proveedores;
* deuda financiera.

Las magnitudes derivadas como EBITDA, EBIT o resultado neto se recalculan posteriormente utilizando las relaciones financieras correspondientes.

---

## 6. Validación temporal

No se realiza una partición aleatoria train/test.

En una serie temporal esto introduciría información futura dentro del entrenamiento.

Se utiliza una división cronológica:

```text
Primeros meses
→ entrenamiento

Últimos 12 meses
→ validación
```

Por ejemplo, con 36 meses:

```text
24 meses entrenamiento
12 meses validación
```

---

## 7. Métrica de evaluación

Los modelos se comparan mediante:

```text
MAE
Mean Absolute Error
```

Se calcula:

```text
MAE =
media(
    |Valor real - Predicción|
)
```

La interpretación es directa:

> error medio absoluto cometido por el modelo en las mismas unidades que la variable analizada.

---

## 8. Selección del modelo

La selección se realiza independientemente para cada variable.

Ejemplo:

```text
Ventas
→ Tendencia + estacionalidad

Gastos de personal
→ Tendencia

Tesorería
→ Tendencia
```

Se selecciona automáticamente el modelo con:

```text
menor MAE
```

Posteriormente el modelo elegido se entrena utilizando todo el histórico disponible.

---

## 9. Forecast Base

El forecast generado directamente por los modelos constituye el:

```text
Escenario Base
```

Representa la continuación esperada de las tendencias y patrones detectados históricamente.

---

## 10. Escenario Optimista

Sobre la previsión Base se aplican hipótesis favorables de negocio.

Actualmente:

```text
Ingresos              +5 %
Aprovisionamientos     -2 % presión
Gastos de personal     -1 % presión
Otros gastos operativos -2 % presión
Tesorería             +10 %
Clientes               -5 %
Deuda financiera       -5 %
```

El objetivo es representar un entorno caracterizado por:

* mayor actividad;
* mejor control de costes;
* mejor conversión de circulante;
* mayor disponibilidad de caja;
* menor deuda financiera.

---

## 11. Escenario Pesimista

Se aplican hipótesis de deterioro respecto al escenario Base.

Actualmente:

```text
Ingresos               -5 %
Aprovisionamientos      +3 % presión
Gastos de personal      +2 % presión
Otros gastos operativos +3 % presión
Tesorería              -10 %
Clientes                +8 %
Deuda financiera        +8 %
```

Representa un entorno caracterizado por:

* menor actividad;
* mayor presión de costes;
* peor conversión de circulante;
* menor caja;
* mayor endeudamiento.

---

## 12. Recalculo de estados

Los escenarios no modifican directamente EBITDA o beneficio neto.

Primero se modifican las variables base.

Después se reconstruyen las magnitudes.

### Margen bruto

```text
Ingresos
+ Aprovisionamientos
```

### EBITDA

```text
Ingresos
+ Aprovisionamientos
+ Personal
+ Otros gastos operativos
```

### EBIT

```text
EBITDA
+ Amortizaciones
+ Deterioros
```

### Resultado antes de impuestos

```text
EBIT
+ Resultado financiero
+ Resultado no recurrente
```

### Resultado neto

```text
Resultado antes de impuestos
+ Impuesto
```

---

## 13. Balance forecast

A partir de las principales masas previstas:

```text
Activo total =
Activo corriente
+ Activo no corriente
```

```text
Pasivo total =
Pasivo corriente
+ Pasivo no corriente
```

El patrimonio neto se obtiene como residual:

```text
Patrimonio neto =
Activo
- Pasivo
```

Esto garantiza la identidad contable del Balance proyectado.

Debe interpretarse como una simplificación del modelo predictivo y no como una previsión detallada de movimientos futuros de patrimonio.

---

## 14. Interpretación

Los escenarios no deben interpretarse como predicciones probabilísticas.

No representan:

```text
95 % de probabilidad
```

ni intervalos estadísticos de confianza.

Son escenarios de sensibilidad:

```text
¿Qué ocurriría si el negocio evoluciona mejor o peor que el escenario Base?
```

Su principal finalidad es facilitar análisis y toma de decisiones.

---

## 15. Limitaciones

Las principales limitaciones son:

* histórico mensual relativamente reducido;
* ausencia de variables macroeconómicas o externas;
* ausencia de presupuesto empresarial;
* forecast basado principalmente en comportamiento histórico;
* escenarios definidos mediante hipótesis explícitas de negocio.

Por estos motivos se utilizan modelos interpretables y se evita presentar el forecast como una predicción exacta del futuro.

---

## 16. Evolución futura

La arquitectura permite incorporar posteriormente:

* más años de histórico;
* presupuesto;
* variables macroeconómicas;
* modelos adicionales;
* intervalos de predicción;
* backtesting recurrente.

Sin modificar el resto de la arquitectura financiera.

---