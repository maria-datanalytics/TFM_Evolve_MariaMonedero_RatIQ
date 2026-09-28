# ==========================================================
# PIPELINE 
# ==========================================================

from pathlib import Path
import subprocess
import sys
import time


# ==========================================================
# RUTAS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
NOTEBOOKS_DIR = BASE_DIR / "notebooks"


NOTEBOOKS = [
    "NB1_Carga_Calidad.ipynb",
    "NB2_Maestro_Financiero.ipynb",
    "NB3_Estados_Financieros.ipynb",
    "NB4_Ratios.ipynb",
    "NB5_Forecast.ipynb",
    "NB6_Modelo_PowerBI.ipynb",
]


# ==========================================================
# VALIDACIÓN INICIAL
# ==========================================================

if not NOTEBOOKS_DIR.exists():
    raise FileNotFoundError(
        f"No existe la carpeta:\n{NOTEBOOKS_DIR}"
    )


rutas_notebooks = [
    NOTEBOOKS_DIR / nombre
    for nombre in NOTEBOOKS
]


faltantes = [
    ruta.name
    for ruta in rutas_notebooks
    if not ruta.exists()
]


if faltantes:
    raise FileNotFoundError(
        "Faltan notebooks del pipeline:\n"
        + "\n".join(
            f" - {nombre}"
            for nombre in faltantes
        )
    )


# ==========================================================
# EJECUCIÓN
# ==========================================================

print("=" * 65)
print("PIPELINE FINANCIERO TFM")
print("=" * 65)

print(f"Proyecto: {BASE_DIR}")
print(f"Notebooks: {NOTEBOOKS_DIR}")

print()


inicio_pipeline = time.perf_counter()


for numero, ruta_notebook in enumerate(
    rutas_notebooks,
    start=1
):

    print("=" * 65)

    print(
        f"[{numero}/{len(rutas_notebooks)}] "
        f"Ejecutando {ruta_notebook.name}"
    )

    print("=" * 65)

    inicio_notebook = time.perf_counter()


    comando = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=600",
        str(ruta_notebook),
    ]


    resultado = subprocess.run(
        comando,
        cwd=BASE_DIR,
    )


    if resultado.returncode != 0:

        print()
        print("!" * 65)
        print("PIPELINE DETENIDO")
        print("!" * 65)

        print(
            f"Error en: {ruta_notebook.name}"
        )

        print(
            "Los notebooks posteriores "
            "NO se han ejecutado."
        )

        sys.exit(
            resultado.returncode
        )


    duracion = (
        time.perf_counter()
        - inicio_notebook
    )


    print()

    print(
        f"OK - {ruta_notebook.name}"
    )

    print(
        f"Duración: {duracion:.1f} segundos"
    )

    print()


# ==========================================================
# FIN
# ==========================================================

duracion_total = (
    time.perf_counter()
    - inicio_pipeline
)


print("=" * 65)
print("PIPELINE COMPLETADO CORRECTAMENTE")
print("=" * 65)

print(
    f"Notebooks ejecutados: "
    f"{len(rutas_notebooks)}/{len(rutas_notebooks)}"
)

print(
    f"Duración total: "
    f"{duracion_total:.1f} segundos"
)

print()
print(
    "Salida final disponible en:"
)

print(
    BASE_DIR
    / "data"
    / "powerbi"
)

print("=" * 65)