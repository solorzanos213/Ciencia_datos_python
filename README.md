# Ciencia de Datos con Python — Semana 1

Proyecto de trabajo para las actividades **3.2 a 3.8** de la guía SENA (2026). La **actividad 3.1** se elaboró por separado y no está incluida.

## Inicio rápido en VS Code (Windows)

1. Abre esta carpeta con **Archivo > Abrir carpeta**.
2. Abre una terminal **PowerShell** y ejecuta:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe scripts\verificar_ambiente.py
   ```

   No necesitas activar el entorno para estos comandos. Si deseas activarlo: `.\.venv\Scripts\Activate.ps1` (puede requerir ajustar políticas de ejecución).
3. En VS Code instala las extensiones recomendadas e indica como intérprete `.venv\Scripts\python.exe`.
4. Abre `notebooks/semana_01_contexto_ambiente.ipynb`, escoge el kernel `.venv` y ejecuta **Run All**.
5. Lee los archivos `docs/` y personaliza **las respuestas de experiencia propia, autoevaluación y bitácora** antes de entregar.
6. Guarda una captura auténtica del notebook ejecutado en `outputs/` (no se incluye una captura fabricada).

En Linux/macOS: `python3 -m venv .venv`, `source .venv/bin/activate`, `python -m pip install -r requirements.txt`, `python scripts/verificar_ambiente.py`.

## Estructura
- `data/raw/`: datos de origen sin editar (vacía en semana 1).
- `data/processed/`: datos transformados (vacía en semana 1).
- `notebooks/`: primer notebook de verificación.
- `outputs/`: capturas reales y resultados.
- `docs/`: diagnóstico, síntesis, mapas y matrices.
- `scripts/`: código de verificación reutilizable.

## Evidencias y guía
- **3.2**: `docs/actividad_3_2_diagnostico.md`
- **3.3**: `docs/actividad_3_3_contexto_y_mapa.md`
- **3.4**: `docs/actividad_3_4_ciclo_dato.md`
- **3.5**: `docs/actividad_3_5_caso_integrador.md`
- **3.6**: estructura, este README, `requirements.txt` y captura real de instalación.
- **3.7**: notebook y `scripts/verificar_ambiente.py`.
- **3.8**: `docs/actividad_3_8_bitacora.md`.

## Buenas prácticas
No almacenar datos reales de aprendices sin permiso. No alterar datos originales; usar rutas relativas; explicar supuestos; verificar resultados. Los ejemplos académicos son **ficticios**. El notebook se ejecuta después de instalar dependencias; no se empaqueta `.venv` porque se debe crear en el equipo que lo use.
