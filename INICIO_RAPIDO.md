# 🌊 Panel de Inteligencia: Global Earthquake & Tsunami Risk Assessment

## ✅ Proyecto Completado

Este dashboard interactivo permite explorar y analizar datos sísmicos globales (2001-2022) para evaluar riesgo tsunamigénico.

---

## 🚀 Inicio Rápido

### Windows (PowerShell):
```powershell
cd app
.\run.ps1
```

### Linux/Mac:
```bash
cd app
chmod +x run.sh
./run.sh
```

### Manual:
```bash
cd app
pip install -r requirements.txt
streamlit run main.py
```

---

## 📋 Estructura del Proyecto

```
├── app/                    # 🚀 APLICACIÓN PRINCIPAL
│   ├── main.py            # Punto de entrada
│   ├── components/        # Componentes reutilizables
│   ├── pages/            # 7 páginas del dashboard
│   ├── utils/            # Utilidades y estilos
│   ├── requirements.txt  # Dependencias
│   └── README.md         # Documentación completa
│
├── data/                  # 📊 Datos
│   └── earthquake_data_tsunami.csv
│
├── docs/                  # 📚 Documentación
│   ├── EDA.md            # Informe de análisis
│   └── info.md
│
└── notebooks/            # 📓 Jupyter notebooks
    ├── EDA_ Demetrio.ipynb
    └── EDA_Paula.ipynb
```

---

## 🎯 Características

✅ **7 Secciones Principales:**
- 🏠 Introducción y contexto
- 📊 Exploración de datos (EDA)
- 🗺️ Análisis geoespacial
- 📅 Análisis temporal
- 🔬 Análisis multivariable
- 📝 Conclusiones y recomendaciones
- 🤖 Machine Learning (en desarrollo)

✅ **Filtros Interactivos:**
- Rango de años
- Rango de magnitud
- Profundidad máxima
- Tipo de evento (tsunami/no tsunami)
- Regiones geográficas

✅ **Visualizaciones Avanzadas:**
- Mapas interactivos globales
- Gráficos 3D
- Animaciones temporales
- Matrices de correlación
- Y mucho más...

---

## 📦 Requisitos

- Python 3.8+
- Dependencias en `app/requirements.txt`

---

## 📚 Documentación

- **Usuario**: `app/README.md`
- **Desarrollador**: `app/DEVELOPMENT.md`
- **Resumen**: `app/PROYECTO_COMPLETADO.md`
- **EDA**: `docs/EDA.md`

---

## 💡 Hallazgos Principales

🎯 **Factores Tsunamigénicos:**
- Magnitud ≥ 7.0
- Profundidad < 50 km
- Eventos oceánicos (dmin > 5°)

🌊 **Patrones Geoespaciales:**
- Concentración en Cinturón de Fuego del Pacífico
- Zonas de subducción críticas

📅 **Patrones Temporales:**
- Sin estacionalidad clara
- Riesgo distribuido durante todo el año

---

## 🤝 Créditos

**Equipo:**
- Demetrio: Análisis exploratorio
- Paula: Desarrollo del dashboard

**Proyecto:** Bootcamp de Análisis de Datos 2025

---

## 🌟 ¡Disfruta Explorando los Datos!

Visita `http://localhost:8501` después de ejecutar la aplicación.

**¡Juntos hacia un mundo más resiliente a tsunamis! 🌊**
