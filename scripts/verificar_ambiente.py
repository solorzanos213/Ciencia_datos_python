"""Verificación reproducible de la Semana 1. Ejecutar desde la raíz del proyecto."""
from pathlib import Path
import sys

try:
    import pandas as pd
    import numpy as np
    import faker
except ImportError as error:
    print('Falta instalar una librería:', error)
    raise SystemExit(1) from error

BASE_DIR = Path(__file__).resolve().parents[1]
print('Ambiente listo para iniciar Ciencia de Datos con Python')
print('Python:', sys.version.split()[0])
print('Pandas:', pd.__version__)
print('NumPy:', np.__version__)
print('Faker: importado correctamente')
for nombre in ('data/raw','data/processed','notebooks','outputs','docs','scripts'):
    ruta = BASE_DIR / nombre
    ruta.mkdir(parents=True, exist_ok=True)
    print('Verificada:', ruta)
