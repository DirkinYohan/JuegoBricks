Dirkin Yohan Ojeda Rodríguez 
# 🧪 Pruebas Unitarias con Pytest en JuegoBricks

## 📦 Instalación de Dependencias

Ejecuta los siguientes comandos para instalar las herramientas necesarias:

```bash
pip install pytest
pip install pygame
```

---

## ⚙️ Configuración de GitHub Actions

Se activó la ejecución automática de pruebas unitarias en **GitHub Actions** al crear el archivo de configuración:

📂 **Ubicación:**  
`.github/workflows/pytest.yml`

---

## 🚀 Ejecutar Pruebas Unitarias

Para ejecutar las pruebas unitarias manualmente, usa el siguiente comando:

```bash
PYTHONPATH=. pytest -v --disable-warnings
```

---

## ❌ Exclusión de Archivos en Pytest

Si deseas **excluir archivos específicos** de las pruebas unitarias, configura el archivo `pytest.ini` de la siguiente manera:

📂 **Archivo:** `pytest.ini`
```ini
[pytest]
norecursedirs = tests/excluded_tests
addopts = --ignore=tests/test_bricks.py
```
- `norecursedirs`: Evita que pytest recorra ciertos directorios.
- `addopts --ignore`: Ignora archivos específicos al ejecutar pruebas.

---

## 📌 Ajustes para `requirements.txt`

Para garantizar compatibilidad con las versiones usadas en el proyecto, el archivo `requirements.txt` debe incluir:

📂 **Archivo:** `requirements.txt`
```txt
pygame==2.5.0
pytest==8.3.5
```

Puedes verificar la versión instalada de `pytest` con el siguiente comando:

```bash
pytest --version
```
📌 **Salida esperada:**
```
pytest 8.3.5
```

