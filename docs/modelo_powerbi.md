
# ARCHIVO: modelo_powerbi.md

# Modelo de datos Power BI

## 1. Objetivo

El modelo final de Power BI se construye siguiendo una arquitectura de estrella sencilla.

Python realiza la mayor parte de la preparación y lógica financiera.

Power BI se centra en:

* visualización;
* interacción;
* filtros;
* navegación;
* storytelling ejecutivo.

---

## 2. Tablas finales

Las tablas se encuentran en:

```text
data/powerbi/
```

---

# 3. Dimensiones

## Dim_Calendario

Granularidad:

```text
1 fila por mes
```

Principales campos:

```text
fecha
año
mes_numero
mes_nombre
año_mes
trimestre
orden_año_mes
tipo_periodo
```

`tipo_periodo` diferencia:

```text
Histórico
Forecast
```

El límite se determina dinámicamente a partir del último periodo histórico disponible.

---

## Dim_Cuentas

Granularidad:

```text
1 fila por cuenta N5
```

Contiene la clasificación financiera de cada cuenta.

Entre sus campos:

* cuenta;
* descripción;
* estado financiero;
* masa financiera;
* categoría;
* subcategoría;
* naturaleza;
* circulante;
* driver.

---

## Dim_CentrosCoste

Granularidad:

```text
1 fila por centro de coste
```

Incluye:

```text
SIN CENTRO
```

para movimientos sin centro asignado.

---

## Dim_Ratios

Granularidad:

```text
1 fila por ratio
```

Incluye metadatos como:

```text
ratio
grupo
unidad
formula
interpretacion
criterio
```

Permite mantener la descripción financiera fuera de las tablas de hechos.

---

## Dim_Escenarios

Contiene:

```text
Real
Pesimista
Base
Optimista
```

Además incluye campos de orden y tipo.

```text
Real        → Histórico
Pesimista   → Forecast
Base        → Forecast
Optimista   → Forecast
```

---

# 4. Fact_Finanzas

Contiene las principales magnitudes financieras históricas y previstas.

Granularidad aproximada:

```text
Fecha
× Métrica
× Horizonte
× Escenario
```

Principales campos:

```text
fecha
metrica
horizonte
valor
valor_ly
variacion_abs
variacion_pct
escenario
tipo_periodo
año
mes_numero
año_mes
```

---

## Horizontes

### MTD

Movimiento mensual.

Utilizado para:

* ingresos;
* margen bruto;
* EBITDA;
* EBIT;
* resultado neto.

---

### YTD

Acumulado desde enero hasta el periodo.

Utilizado para magnitudes de flujo históricas.

---

### CIERRE

Saldo correspondiente al cierre del mes.

Utilizado para:

* activos;
* pasivos;
* patrimonio neto;
* tesorería;
* deuda;
* clientes;
* proveedores;
* existencias.

---

# 5. Fact_Ratios

Granularidad:

```text
Fecha
× Ratio
× Horizonte
× Escenario
```

Principales campos:

```text
fecha
ratio
horizonte
valor
valor_ly
variacion_abs
variacion_pct
estado
escenario
tipo_periodo
año
mes_numero
año_mes
```

Los ratios históricos ya están calculados en Python.

Power BI no debe recalcular innecesariamente estos indicadores.

---

# 6. Fact_CentrosCoste

Contiene el análisis de PyG por centro de coste.

Principales campos:

```text
fecha
centro_coste
categoria_financiera
subcategoria_financiera
driver_negocio
valor_mes
valor_ytd
```

Permite localizar las principales causas operativas dentro de la organización.

---

# 7. Fact_Diagnostico

Granularidad:

```text
1 fila por periodo
```

Contiene:

```text
fecha
diagnostico
numero_alertas
```

Su objetivo es proporcionar una síntesis automática de las principales variaciones financieras.

---

# 8. Fact_Alertas

Contiene los principales ratios clasificados como desfavorables en cada periodo.

Se limita a un número reducido de alertas para evitar saturar el dashboard.

Principales campos:

```text
fecha
ratio
horizonte
valor
valor_ly
variacion_abs
variacion_pct
estado
grupo
interpretacion
```

---

# 9. Fact_ResumenEscenarios

Contiene un resumen del horizonte forecast para:

```text
Pesimista
Base
Optimista
```

Incluye magnitudes como:

* ingresos previstos;
* EBITDA;
* resultado neto;
* activo final;
* pasivo final;
* patrimonio final;
* caja final;
* deuda final;
* fondo de maniobra final;
* márgenes previstos.

---

# 10. Relaciones

El modelo recomendado utiliza relaciones:

```text
1 → *
```

desde las dimensiones hacia las tablas de hechos.

---

## Calendario

```text
Dim_Calendario[fecha]
        ↓
Fact_Finanzas[fecha]
```

```text
Dim_Calendario[fecha]
        ↓
Fact_Ratios[fecha]
```

```text
Dim_Calendario[fecha]
        ↓
Fact_CentrosCoste[fecha]
```

```text
Dim_Calendario[fecha]
        ↓
Fact_Diagnostico[fecha]
```

```text
Dim_Calendario[fecha]
        ↓
Fact_Alertas[fecha]
```

---

## Ratios

```text
Dim_Ratios[ratio]
       ↓
Fact_Ratios[ratio]
```

También puede relacionarse con las alertas si se utiliza el ratio como dimensión común.

---

## Centros de coste

```text
Dim_CentrosCoste[centro_coste]
             ↓
Fact_CentrosCoste[centro_coste]
```

---

## Escenarios

```text
Dim_Escenarios[escenario]
          ↓
Fact_Finanzas[escenario]
```

```text
Dim_Escenarios[escenario]
          ↓
Fact_Ratios[escenario]
```

---

# 11. Dirección de filtro

Por defecto las relaciones deben utilizar:

```text
Dirección simple
```

desde la dimensión hacia la tabla de hechos.

Se evita utilizar relaciones bidireccionales salvo necesidad concreta.

Esto reduce:

* ambigüedades;
* resultados inesperados;
* complejidad del modelo.

---

# 12. Regla de agregación

No todas las métricas financieras deben agregarse de la misma forma.

## Flujos

Ejemplos:

```text
Ventas
EBITDA
EBIT
Resultado
```

Pueden analizarse mediante:

```text
MTD
YTD
```

---

## Stocks

Ejemplos:

```text
Activo
Tesorería
Deuda
Patrimonio neto
```

Deben mostrarse como saldo de cierre del último periodo seleccionado.

No deben sumarse entre meses.

---

## Ratios

Los ratios no deben sumarse.

Tampoco deben promediarse automáticamente.

Cuando se seleccionan múltiples periodos, normalmente debe utilizarse el valor correspondiente al último periodo visible o el horizonte financiero definido en Python.

---

# 13. Papel de DAX

DAX se mantiene para necesidades de presentación e interacción.

Ejemplos:

* selección de último periodo;
* títulos dinámicos;
* rankings;
* filtros;
* contexto del usuario;
* formato condicional;
* navegación.

La lógica financiera principal permanece en Python.

---

# 14. Modelo conceptual

```text
                 Dim_Calendario
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
 Fact_Finanzas    Fact_Ratios   Fact_CentrosCoste
        │              │               │
        │              │               │
        │        Dim_Ratios      Dim_CentrosCoste
        │
 Dim_Escenarios

        Dim_Calendario
              │
        ┌─────┴─────┐
        ▼           ▼
Fact_Diagnostico  Fact_Alertas
```

---

# 15. Storytelling del dashboard

El modelo está diseñado para soportar una narrativa ejecutiva:

```text
DETECTAR
   ↓
EXPLICAR
   ↓
EVALUAR RIESGO
   ↓
LOCALIZAR
   ↓
ANTICIPAR
   ↓
DECIDIR
```

La finalidad del dashboard no es únicamente mostrar estados financieros, sino facilitar la identificación de problemas, sus causas y su posible evolución futura.
