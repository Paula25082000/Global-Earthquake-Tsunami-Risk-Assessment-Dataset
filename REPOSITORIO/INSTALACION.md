# 🚀 Guía de Instalación y Ejecución

## ⚡ Instalación Rápida

### Paso 1: Verificar Python

Abre PowerShell y ejecuta:
```powershell
python --version
```

Deberías ver algo como: `Python 3.8.x` o superior.

Si no tienes Python instalado, descárgalo de: https://www.python.org/downloads/

---

### Paso 2: Navegar a la Carpeta del Proyecto

```powershell
cd "C:\Users\paula\Downloads\Bootcamp\Global-Earthquake-Tsunami-Risk-Assessment-Dataset\app"
```

---

### Paso 3: Instalar Dependencias

```powershell
pip install -r requirements.txt
```

Este comando instalará:
- streamlit (framework web)
- pandas (manipulación de datos)
- numpy (computación numérica)
- plotly (visualizaciones interactivas)
- scipy (análisis estadístico)

**Nota:** La instalación puede tardar 2-3 minutos.

---

### Paso 4: Ejecutar la Aplicación

```powershell
streamlit run main.py
```

**O simplemente ejecuta el script automatizado:**
```powershell
.\run.ps1
```

---

## 🌐 Acceso al Dashboard

La aplicación se abrirá automáticamente en tu navegador en:
```
http://localhost:8501
```

Si no se abre automáticamente, copia y pega esa URL en tu navegador.

---

## 🛑 Detener la Aplicación

Presiona `Ctrl + C` en la terminal de PowerShell.

---

## 🔧 Solución de Problemas

### Error: "streamlit no se reconoce como comando"

**Solución:**
```powershell
python -m pip install --upgrade streamlit
```

Luego ejecuta:
```powershell
python -m streamlit run main.py
```

---

### Error: "No se encuentra el archivo CSV"

**Verifica que el archivo existe:**
```powershell
Test-Path "..\data\earthquake_data_tsunami.csv"
```

Debería devolver `True`. Si devuelve `False`, verifica la ruta del archivo de datos.

---

### Error: "Import ... could not be resolved"

Esto es normal en el editor antes de instalar las dependencias. Ejecuta:
```powershell
pip install -r requirements.txt
```

---

### La aplicación es lenta

1. **Reduce el tamaño de muestra** en gráficos pesados (coordenadas paralelas)
2. **Aplica filtros** para trabajar con menos datos
3. **Cierra otras aplicaciones** para liberar RAM

---

### Puertos en uso

Si el puerto 8501 está ocupado, Streamlit usará automáticamente otro puerto (8502, 8503, etc.)

---

## 📦 Dependencias Detalladas

| Librería | Versión | Propósito |
|----------|---------|-----------|
| streamlit | ≥1.28.0 | Framework web para el dashboard |
| pandas | ≥2.0.0 | Manipulación y análisis de datos |
| numpy | ≥1.24.0 | Operaciones numéricas |
| plotly | ≥5.17.0 | Visualizaciones interactivas |
| scipy | ≥1.11.0 | Análisis estadístico avanzado |
| python-dateutil | ≥2.8.2 | Manejo de fechas y tiempo |

---

## 🐍 Entorno Virtual (Opcional pero Recomendado)

Para evitar conflictos con otras instalaciones de Python:

### Crear entorno virtual:
```powershell
python -m venv venv
```

### Activar entorno virtual:
```powershell
.\venv\Scripts\Activate.ps1
```

Si hay error de política de ejecución:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Instalar dependencias:
```powershell
pip install -r requirements.txt
```

### Ejecutar aplicación:
```powershell
streamlit run main.py
```

### Desactivar entorno virtual:
```powershell
deactivate
```

---

## 🌐 Navegadores Recomendados

- ✅ Google Chrome (Recomendado)
- ✅ Microsoft Edge
- ✅ Mozilla Firefox
- ⚠️ Safari (puede tener problemas con algunas visualizaciones)

---

## 💾 Requisitos del Sistema

- **SO**: Windows 10/11, Linux, macOS
- **RAM**: 4 GB mínimo, 8 GB recomendado
- **Espacio**: 500 MB para dependencias
- **Python**: 3.8 o superior
- **Conexión**: Internet para instalar dependencias

---

## 📊 Verificar Instalación

Después de instalar, verifica:

```powershell
# Verificar streamlit
streamlit --version

# Verificar pandas
python -c "import pandas; print(pandas.__version__)"

# Verificar plotly
python -c "import plotly; print(plotly.__version__)"
```

---

## 🔄 Actualizar Dependencias

Para actualizar a las últimas versiones:

```powershell
pip install --upgrade -r requirements.txt
```

---

## 📞 Soporte

Si encuentras problemas no cubiertos aquí:

1. Revisa `README.md` en la carpeta `app/`
2. Consulta `DEVELOPMENT.md` para detalles técnicos
3. Verifica que tienes Python 3.8+ instalado
4. Asegúrate de estar en la carpeta correcta (`app/`)

---

## ✅ Checklist de Instalación

- [ ] Python 3.8+ instalado
- [ ] Navegado a la carpeta `app/`
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Archivo CSV existe en `../data/earthquake_data_tsunami.csv`
- [ ] Aplicación ejecutada (`streamlit run main.py`)
- [ ] Dashboard abierto en el navegador (`http://localhost:8501`)

---

## 🎉 ¡Todo Listo!

Si completaste todos los pasos, deberías ver el dashboard en tu navegador.

**¡Disfruta explorando los datos sísmicos! 🌊**

---

*Si necesitas ayuda adicional, consulta la documentación completa en `app/README.md`*
