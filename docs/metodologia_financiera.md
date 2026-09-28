# Metodología financiera

## 1. Objetivo

Este documento recoge los principales criterios financieros utilizados para transformar la información contable en estados financieros, métricas y ratios comparables.

El objetivo no es únicamente obtener resultados numéricos, sino asegurar que los cálculos sean:

* coherentes;
* reproducibles;
* interpretables;
* financieramente defendibles.

---

# 2. Fuentes de información

El sistema parte principalmente de tres fuentes:

### Contabilidad

Contiene el detalle de movimientos contables.

Se utiliza especialmente para:

* análisis por cuenta;
* centros de coste;
* detalle transaccional;
* reconciliaciones;
* análisis posteriores.

### Balances históricos

Contienen los saldos contables utilizados para reconstruir los estados financieros históricos.

Se utilizan como fuente principal para mantener coherencia entre:

* saldos de Balance;
* movimientos;
* resultado;
* cuadre patrimonial.

### Maestro de cuentas

Permite traducir el código contable a una estructura financiera.

Cada cuenta se clasifica en dimensiones como:

* Balance o PyG;
* masa financiera;
* categoría;
* subcategoría;
* naturaleza;
* circulante;
* driver de negocio.

---

# 3. Signos contables y signos analíticos

Los datos originales mantienen los signos contables.

Sin embargo, para facilitar el análisis financiero se utiliza una representación analítica de la PyG.

En la contabilidad:

* los ingresos suelen aparecer con signo negativo;
* los gastos suelen aparecer con signo positivo.

Para la presentación analítica se invierte el signo:

```text
importe_analitico = -importe
```

De esta forma:

```text
Ingresos   → positivos
Gastos     → negativos
```

No se utiliza valor absoluto.

Esto permite conservar correctamente:

* anulaciones;
* reclasificaciones;
* correcciones;
* movimientos inversos.

---

# 4. Balance

El Balance se construye utilizando saldos de cierre mensuales.

Las principales masas utilizadas son:

```text
Activo corriente
Activo no corriente
Pasivo corriente
Pasivo no corriente
Patrimonio neto
```

A partir de ellas:

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

```text
Pasivo + Patrimonio Neto =
Pasivo total
+ Patrimonio neto
```

---

# 5. Control de cuadre

Para cada periodo se verifica:

```text
Activo =
Pasivo + Patrimonio Neto
```

La diferencia se calcula como:

```text
Diferencia =
Activo total
- Pasivo
- Patrimonio Neto
```

Se utiliza una tolerancia de:

```text
0,01 €
```

Si:

```text
|Diferencia| <= 0,01
```

el periodo se considera:

```text
CUADRA
```

En caso contrario:

```text
REVISAR
```

El cuadre del Balance es un control crítico.

Si algún periodo no cuadra, los notebooks posteriores de ratios no deben continuar.

---

# 6. Cuenta de Pérdidas y Ganancias

La PyG se construye mensualmente y mantiene una estructura jerárquica.

Entre las principales magnitudes se incluyen:

```text
Ingresos de explotación
Aprovisionamientos
Margen bruto
Gastos de personal
Otros gastos operativos
EBITDA
Amortizaciones
Deterioros
EBIT
Resultado financiero
Resultado antes de impuestos
Impuesto sobre beneficios
Resultado neto
```

---

# 7. Margen bruto

Se calcula como:

```text
Margen bruto =
Ingresos de explotación
+ Aprovisionamientos
```

Dado que los gastos se representan con signo negativo, se utiliza suma algebraica.

---

# 8. EBITDA

El EBITDA representa el resultado operativo antes de amortizaciones, deterioros, intereses e impuestos.

La estructura utilizada es:

```text
EBITDA =
Ingresos de explotación
+ Aprovisionamientos
+ Gastos de personal
+ Otros gastos operativos
+ Otros ingresos
+ Otros gastos
```

---

# 9. EBIT

Se obtiene mediante:

```text
EBIT =
EBITDA
+ Amortizaciones
+ Deterioros
```

Las amortizaciones y deterioros presentan signo negativo en la representación analítica.

---

# 10. Resultado antes de impuestos

```text
Resultado antes de impuestos =
EBIT
+ Resultado financiero
+ Resultado no recurrente
```

---

# 11. Resultado neto

```text
Resultado neto =
Resultado antes de impuestos
+ Impuesto sobre beneficios
```

---

# 12. MTD y YTD

Se diferencia expresamente entre flujos y stocks.

## MTD

MTD representa exclusivamente el movimiento correspondiente al mes seleccionado.

Ejemplos:

* ventas del mes;
* EBITDA del mes;
* EBIT del mes;
* resultado neto del mes.

---

## YTD

YTD representa el acumulado desde enero hasta el mes seleccionado.

Ejemplo:

```text
Ventas YTD en septiembre =
Ventas enero
+ ...
+ Ventas septiembre
```

Se reinicia al comenzar cada ejercicio.

---

# 13. Variables de Balance

Las variables de Balance son stocks.

Por tanto, no deben acumularse.

Ejemplo:

```text
Tesorería YTD
```

no tiene interpretación financiera adecuada como suma de los saldos mensuales.

En su lugar se utiliza:

```text
Tesorería de cierre del periodo seleccionado
```

La misma lógica se aplica a:

* activo;
* pasivo;
* patrimonio neto;
* deuda;
* existencias;
* clientes;
* proveedores.

---

# 14. Márgenes

Los márgenes se recalculan a partir de sus componentes.

Por ejemplo:

```text
Margen EBITDA =
EBITDA / Ingresos
```

Para YTD:

```text
Margen EBITDA YTD =
EBITDA YTD / Ingresos YTD
```

No se calcula como promedio de los márgenes mensuales.

---

# 15. ROA

El ROA relaciona el resultado con los activos utilizados para generarlo.

Se utiliza:

```text
ROA =
Resultado neto anualizado
/
Activo total medio YTD
```

El activo medio YTD corresponde a la media de los saldos mensuales disponibles dentro del ejercicio hasta el periodo analizado.

La anualización permite comparar ratios calculados en meses diferentes del mismo ejercicio.

---

# 16. ROE

El ROE se calcula mediante:

```text
ROE =
Resultado neto anualizado
/
Patrimonio neto medio YTD
```

El denominador debe ser positivo para mantener una interpretación financiera razonable.

---

# 17. Análisis DuPont

El ROE también se descompone mediante el modelo DuPont:

```text
ROE =
Margen neto
× Rotación de activos
× Apalancamiento financiero
```

donde:

```text
Margen neto =
Resultado neto / Ventas
```

```text
Rotación de activos =
Ventas / Activo medio
```

```text
Apalancamiento =
Activo medio / Patrimonio neto medio
```

El sistema valida que el ROE calculado directamente y el obtenido mediante DuPont sean equivalentes dentro de una tolerancia numérica mínima.

---

# 18. Liquidez

## Liquidez corriente

```text
Activo corriente
/
Pasivo corriente
```

## Prueba ácida

```text
(Activo corriente - Existencias)
/
Pasivo corriente
```

## Liquidez inmediata

```text
Tesorería
/
Pasivo corriente
```

---

# 19. Solvencia y estructura

## Endeudamiento

```text
Pasivo total
/
Activo total
```

## Autonomía financiera

```text
Patrimonio neto
/
Activo total
```

## Deuda financiera sobre activo

```text
Deuda financiera bruta
/
Activo total
```

---

# 20. Deuda financiera neta

Se calcula mediante:

```text
Deuda financiera neta =
Deuda financiera bruta
- Tesorería
```

Un resultado negativo representa una posición de caja neta.

---

# 21. Deuda neta / EBITDA

Para evitar comparar una deuda de cierre con un único mes de EBITDA se utiliza EBITDA LTM:

```text
EBITDA LTM =
suma EBITDA últimos 12 meses
```

Por tanto:

```text
Deuda neta / EBITDA =
Deuda financiera neta
/
EBITDA LTM
```

---

# 22. Circulante

## Fondo de maniobra

```text
Fondo de maniobra =
Activo corriente
- Pasivo corriente
```

## Días de cobro

Se utiliza una aproximación basada en:

```text
Clientes medios YTD
× Días transcurridos
/
Ingresos YTD
```

---

# 23. Comparativas temporales

Para cada métrica o ratio cuando corresponde se calculan:

```text
Valor actual
Valor mismo periodo del año anterior
Variación absoluta
Variación porcentual
```

La variación absoluta es:

```text
Actual - Año anterior
```

La variación porcentual es:

```text
Actual / Año anterior - 1
```

No se calcula cuando el valor comparativo es cero o demasiado próximo a cero.

---

# 24. Principio general

La metodología diferencia siempre entre:

### Flujos

Ejemplos:

* ingresos;
* EBITDA;
* EBIT;
* resultado.

Permiten:

```text
MTD
YTD
LTM
```

### Stocks

Ejemplos:

* activo;
* deuda;
* tesorería;
* patrimonio neto.

Se analizan mediante:

```text
Saldo de cierre
```

### Ratios

Se recalculan utilizando sus componentes financieros.

No deben sumarse ni promediarse automáticamente salvo que exista una justificación financiera expresa.

Esta separación evita uno de los errores más habituales en modelos financieros y herramientas de Business Intelligence.
