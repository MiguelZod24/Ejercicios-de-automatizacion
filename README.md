# Automatización con Playwright y Python 🧪

Este repositorio contiene ejemplos básicos de automatización de pruebas utilizando Playwright 
con Python y Pytest.

### Archivos incluidos:

- `conftest.py`: Configura el navegador y la traza (trace.zip).
- `test_multiples.py`: Pruebas automatizadas sobre un formulario de demo.

### Tecnologías usadas:

- Python
- Playwright
- Pytest
- pytest-html-reporter

### Cómo correrlo (con reporte HTML):

```bash
pytest test_multiples.py -s -v --html=report.html
