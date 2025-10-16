<div align="center">

# 🌊 Global Earthquake & Tsunami Risk Assessment

### *Panel de Inteligencia para Análisis Sísmico y Evaluación de Riesgo Tsunamigénico*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.17+-3F4F75.svg)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[🚀 Demo](#-demo) • [✨ Características](#-características-principales) • [📊 Datos](#-acerca-de-los-datos) • [🛠️ Instalación](#️-instalación) • [📖 Documentación](#-documentación)

<img src="https://raw.githubusercontent.com/yourusername/repo/main/img/dashboard-preview.png" alt="Dashboard Preview" width="800px">

</div>

---

## 📋 Tabla de Contenidos

- [🎯 Acerca del Proyecto](#-acerca-del-proyecto)
- [✨ Características Principales](#-características-principales)
- [🚀 Demo](#-demo)
- [📊 Acerca de los Datos](#-acerca-de-los-datos)
- [🛠️ Instalación](#️-instalación)
- [💻 Uso](#-uso)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🔬 Análisis y Hallazgos](#-análisis-y-hallazgos)
- [🎨 Tecnologías](#-tecnologías)
- [📸 Capturas de Pantalla](#-capturas-de-pantalla)
- [📖 Documentación](#-documentación)
- [🤝 Contribuir](#-contribuir)
- [👥 Equipo](#-equipo)
- [📄 Licencia](#-licencia)

---

## 🎯 Acerca del Proyecto

Este proyecto presenta un **dashboard interactivo de inteligencia** desarrollado en Streamlit para el análisis exploratorio y evaluación de riesgo tsunamigénico basado en datos sísmicos globales del período 2001-2022.

### 🌍 Objetivo Principal

> **¿Qué condiciones sísmicas hacen más probable que un terremoto genere un tsunami?**

A través de análisis exhaustivos de datos históricos, este panel identifica patrones críticos, evalúa riesgos y proporciona insights accionables para:

- ⚠️ **Sistemas de alerta temprana**
- 🏗️ **Planificación urbana y de infraestructura**
- 📚 **Educación y concienciación pública**
- 🛡️ **Políticas de protección civil**
- 🔬 **Investigación científica**

---

## ✨ Características Principales

<table>
<tr>
<td width="50%">

### 📊 Análisis Exploratorio
- Distribuciones estadísticas detalladas
- Tests de normalidad (Shapiro-Wilk)
- Matrices de correlación interactivas
- Comparaciones con/sin tsunami
- Tests de significancia estadística

</td>
<td width="50%">

### 🗺️ Visualización Geoespacial
- Mapas globales interactivos
- Análisis del Cinturón de Fuego
- Patrones de profundidad
- Calidad de monitoreo sísmico
- Eventos críticos identificados

</td>
</tr>
<tr>
<td width="50%">

### 📅 Análisis Temporal
- Evolución anual de eventos
- Patrones mensuales y estacionalidad
- Animaciones temporales
- Series históricas
- Tendencias identificadas

</td>
<td width="50%">

### 🔬 Análisis Multivariable
- Visualizaciones 3D interactivas
- Coordenadas paralelas
- Análisis de pares de variables
- Mapas de densidad
- Relaciones complejas

</td>
</tr>
</table>

### 🎯 Filtros Interactivos Avanzados

- 📅 **Rango temporal**: Selección de años específicos
- 📏 **Magnitud**: Control preciso de rangos
- 🌍 **Profundidad**: Filtro de profundidad del hipocentro
- 🌊 **Tipo de evento**: Con/sin tsunami
- 🗺️ **Regiones**: Filtros por hemisferios
- ⚙️ **Avanzados**: Categorías, significancia, eventos superficiales

---

## 🚀 Demo

### Panel en Vivo
```bash
# Clonar el repositorio
git clone https://github.com/yourusername/earthquake-tsunami-dashboard.git

# Navegar al directorio
cd earthquake-tsunami-dashboard/app

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run main.py
```

### 🎥 Video Demo
> _[Próximamente: Video de demostración en YouTube]_

---

## 📊 Acerca de los Datos

### 📈 Dataset

- **Fuente**: Global Earthquake Database with Tsunami Information
- **Período**: 2001 - 2022 (22 años)
- **Registros**: Miles de eventos sísmicos globales
- **Variables**: 13 características principales

### 🔢 Variables Clave

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `magnitude` | Magnitud del terremoto (escala Richter) | Numérica |
| `depth` | Profundidad del hipocentro (km) | Numérica |
| `latitude` / `longitude` | Coordenadas del epicentro | Numérica |
| `tsunami` | Generación de tsunami (1=Sí, 0=No) | Binaria |
| `sig` | Puntaje de significancia del evento | Numérica |
| `nst` | Número de estaciones sismológicas | Numérica |
| `dmin` | Distancia mínima a estación (°) | Numérica |
| `gap` | Brecha azimutal entre estaciones (°) | Numérica |
| `mmi` / `cdi` | Intensidades Mercalli | Numérica |

### 📍 Cobertura Geográfica

```
🌍 Global - Enfoque en:
├── 🔥 Cinturón de Fuego del Pacífico
├── 🌊 Zonas de subducción oceánicas
├── 🗾 Regiones de alta actividad sísmica
└── 🏝️ Áreas costeras vulnerables
```

---

## 🛠️ Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- 4 GB RAM mínimo (8 GB recomendado)

### Instalación Rápida

#### Windows (PowerShell)
```powershell
# Clonar repositorio
git clone https://github.com/yourusername/earthquake-tsunami-dashboard.git
cd earthquake-tsunami-dashboard/app

# Ejecutar script automatizado
.\run.ps1
```

#### Linux / macOS
```bash
# Clonar repositorio
git clone https://github.com/yourusername/earthquake-tsunami-dashboard.git
cd earthquake-tsunami-dashboard/app

# Dar permisos de ejecución
chmod +x run.sh

# Ejecutar script automatizado
./run.sh
```

### Instalación Manual

```bash
# 1. Clonar el repositorio
git clone https://github.com/yourusername/earthquake-tsunami-dashboard.git

# 2. Navegar al directorio de la aplicación
cd earthquake-tsunami-dashboard/app

# 3. (Opcional pero recomendado) Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
streamlit run main.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 💻 Uso

### Navegación del Dashboard

El dashboard está organizado en **7 secciones principales**:

1. **🏠 Inicio**: Introducción, contexto y objetivos del proyecto
2. **📊 Exploración de Datos**: Análisis estadístico completo (EDA)
3. **🗺️ Análisis Geoespacial**: Mapas interactivos y patrones geográficos
4. **📅 Análisis Temporal**: Tendencias y evolución temporal
5. **🔬 Análisis Multivariable**: Relaciones complejas entre variables
6. **📝 Conclusiones**: Hallazgos principales y recomendaciones
7. **🤖 Machine Learning**: Modelos predictivos (en desarrollo)

### Interacción con Visualizaciones

Todas las visualizaciones son **completamente interactivas**:

- 🖱️ **Hover**: Información detallada al pasar el cursor
- 🔍 **Zoom**: Acercamiento y alejamiento
- 🎯 **Pan**: Desplazamiento por el gráfico
- 📷 **Descarga**: Exportar gráficos como imágenes
- 🎛️ **Filtros**: Personalización de datos visualizados

---

## 📁 Estructura del Proyecto

```
earthquake-tsunami-dashboard/
│
├── 📊 app/                          # Aplicación Streamlit
│   ├── main.py                      # Punto de entrada principal
│   ├── requirements.txt             # Dependencias
│   ├── README.md                    # Documentación de usuario
│   ├── DEVELOPMENT.md               # Guía de desarrollo
│   │
│   ├── 🧩 components/               # Componentes reutilizables
│   │   ├── sidebar.py               # Menú lateral y navegación
│   │   └── filters.py               # Filtros interactivos
│   │
│   ├── 📄 pages/                    # Páginas del dashboard
│   │   ├── introduccion.py          # Página de inicio
│   │   ├── exploracion_datos.py     # EDA completo
│   │   ├── analisis_geoespacial.py  # Mapas interactivos
│   │   ├── analisis_temporal.py     # Análisis temporal
│   │   ├── analisis_multivariable.py
│   │   ├── conclusiones.py
│   │   └── machine_learning.py
│   │
│   └── 🛠️ utils/                    # Utilidades
│       ├── data_loader.py           # Carga de datos
│       └── styles.py                # Estilos CSS
│
├── 📊 data/                         # Datos del proyecto
│   └── earthquake_data_tsunami.csv  # Dataset principal
│
├── 📚 docs/                         # Documentación
│   ├── EDA.md                       # Informe de análisis
│   └── info.md                      # Información adicional
│
├── 📓 notebooks/                    # Jupyter Notebooks
│   ├── EDA_ Demetrio.ipynb          # Análisis exploratorio
│   └── preprocesamiento.ipynb       # Procesamiento de datos
│
├── 🖼️ img/                          # Imágenes y capturas
│
├── README.md                        # Este archivo
├── INSTALACION.md                   # Guía de instalación
└── INICIO_RAPIDO.md                 # Guía rápida
```

---

## 🔬 Análisis y Hallazgos

### 🎯 Hallazgos Principales

#### 1. Factores Tsunamigénicos Críticos

```python
🔴 ALTO RIESGO:
├── Magnitud ≥ 7.5
├── Profundidad < 30 km
├── Evento oceánico (dmin > 5°)
└── Zona de subducción

🟡 RIESGO MODERADO:
├── Magnitud 7.0 - 7.5
├── Profundidad 30-50 km
└── Significancia alta

🟢 RIESGO BAJO:
├── Magnitud < 7.0
└── Profundidad > 50 km
```

#### 2. Patrones Geoespaciales

- 🔥 **Cinturón de Fuego del Pacífico**: 85% de los tsunamis
- 🌊 **Eventos oceánicos**: Mayor probabilidad tsunamigénica
- 🗾 **Zonas críticas**: Japón, Indonesia, Chile, Alaska

#### 3. Correlaciones Clave

| Variables | Correlación | Interpretación |
|-----------|-------------|----------------|
| Magnitud ↔ Tsunami | +0.65 | Fuerte positiva |
| Profundidad ↔ Tsunami | -0.48 | Negativa moderada |
| dmin ↔ Tsunami | +0.32 | Positiva débil |
| Magnitud ↔ Sig | +0.92 | Muy fuerte (redundante) |

#### 4. Insights Temporales

- 📅 **Sin estacionalidad**: Riesgo distribuido durante todo el año
- 📈 **Tendencia estable**: No hay incremento en frecuencia
- 🔄 **Variabilidad anual**: Relacionada con actividad tectónica puntual

### ⚠️ Reglas de Alerta Temprana

Basado en el análisis de datos históricos:

```python
def evaluar_riesgo_tsunami(magnitud, profundidad, dmin):
    score = 0
    
    # Factor magnitud
    if magnitud >= 7.5:
        score += 40
    elif magnitud >= 7.0:
        score += 20
    
    # Factor profundidad
    if profundidad < 30:
        score += 30
    elif profundidad < 50:
        score += 15
    
    # Factor ubicación
    if dmin > 5:
        score += 20
    elif dmin > 3:
        score += 10
    
    # Clasificación
    if score >= 70:
        return "RIESGO ALTO - ALERTA INMEDIATA"
    elif score >= 40:
        return "RIESGO MODERADO - VIGILANCIA"
    else:
        return "RIESGO BAJO - MONITOREO ESTÁNDAR"
```

---

## 🎨 Tecnologías

### Backend & Data Processing
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

### Frontend & Visualization
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Development Tools
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

### Dependencias Principales

```txt
streamlit>=1.28.0        # Framework web interactivo
pandas>=2.0.0            # Manipulación de datos
numpy>=1.24.0            # Computación numérica
plotly>=5.17.0           # Visualizaciones interactivas
scipy>=1.11.0            # Análisis estadístico
python-dateutil>=2.8.2   # Manejo de fechas
```

---

## 📸 Capturas de Pantalla

### Dashboard Principal
![Dashboard Home](img/dashboard-home.png)

### Análisis Geoespacial
![Mapas Interactivos](img/geospatial-analysis.png)

### Análisis Multivariable
![Análisis 3D](img/multivariate-analysis.png)

### Análisis Temporal
![Evolución Temporal](img/temporal-analysis.png)

---

## 📖 Documentación

### 📚 Documentación Disponible

- **[README.md](README.md)**: Este archivo (descripción general)
- **[INSTALACION.md](INSTALACION.md)**: Guía detallada de instalación
- **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)**: Guía de inicio rápido
- **[app/README.md](app/README.md)**: Manual de usuario del dashboard
- **[app/DEVELOPMENT.md](app/DEVELOPMENT.md)**: Guía para desarrolladores
- **[docs/EDA.md](docs/EDA.md)**: Informe completo de análisis exploratorio

### 🎓 Recursos Educativos

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Guía de Tsunamis - NOAA](https://www.tsunami.noaa.gov/)

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Este proyecto está abierto a mejoras y extensiones.

### Cómo Contribuir

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### Áreas de Contribución

- 🐛 **Reportar bugs** o problemas
- ✨ **Proponer nuevas features**
- 📝 **Mejorar documentación**
- 🎨 **Mejorar diseño UI/UX**
- 🧪 **Añadir tests**
- 🤖 **Desarrollar modelos ML**
- 🌍 **Traducir a otros idiomas**

### Código de Conducta

Este proyecto se adhiere a un código de conducta de colaboración profesional y respetuosa.

---

## 👥 Equipo

<table>
<tr>
<td align="center">
<img src="https://via.placeholder.com/150" width="100px;" alt="Demetrio"/><br />
<sub><b>Demetrio</b></sub><br />
<sub>Análisis de Datos & EDA</sub><br />
<a href="https://github.com/demetrio">GitHub</a>
</td>
<td align="center">
<img src="https://via.placeholder.com/150" width="100px;" alt="Paula"/><br />
<sub><b>Paula</b></sub><br />
<sub>Desarrollo del Dashboard</sub><br />
<a href="https://github.com/paula">GitHub</a>
</td>
</tr>
</table>

### 🎓 Contexto Académico

Este proyecto fue desarrollado como parte del **Bootcamp de Análisis de Datos 2025**, combinando conocimientos de:

- 📊 Análisis Exploratorio de Datos (EDA)
- 🗺️ Visualización Geoespacial
- 📈 Análisis Estadístico
- 💻 Desarrollo Web con Streamlit
- 🎨 Diseño UX/UI

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Earthquake & Tsunami Dashboard Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 📞 Contacto y Soporte

### 💬 Preguntas Frecuentes

¿Tienes preguntas? Consulta nuestra [documentación completa](app/README.md) o abre un [issue](https://github.com/yourusername/earthquake-tsunami-dashboard/issues).

### 🐛 Reportar Problemas

Si encuentras un bug, por favor [crea un issue](https://github.com/yourusername/earthquake-tsunami-dashboard/issues/new) con:
- Descripción del problema
- Pasos para reproducirlo
- Comportamiento esperado vs actual
- Capturas de pantalla (si aplica)

### 📧 Contacto Directo

- **Email**: project@earthquake-dashboard.com
- **Twitter**: [@EarthquakeDash](https://twitter.com/earthquakedash)
- **LinkedIn**: [Earthquake Dashboard Project](https://linkedin.com/company/earthquake-dashboard)

---

## 🌟 Agradecimientos

- 🙏 **Comunidad de Streamlit** por el framework increíble
- 🙏 **Plotly** por las visualizaciones interactivas
- 🙏 **USGS** por los datos sísmicos
- 🙏 **NOAA** por la información de tsunamis
- 🙏 **Bootcamp Team** por el apoyo y mentoría

---

## 📊 Estadísticas del Proyecto

![GitHub Stars](https://img.shields.io/github/stars/yourusername/earthquake-tsunami-dashboard?style=social)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/earthquake-tsunami-dashboard?style=social)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/earthquake-tsunami-dashboard)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/yourusername/earthquake-tsunami-dashboard)
![GitHub Last Commit](https://img.shields.io/github/last-commit/yourusername/earthquake-tsunami-dashboard)
![GitHub Code Size](https://img.shields.io/github/languages/code-size/yourusername/earthquake-tsunami-dashboard)

---

## 🚀 Roadmap

### ✅ Fase 1: MVP (Completado)
- [x] Análisis exploratorio completo
- [x] Dashboard interactivo con Streamlit
- [x] 7 secciones principales
- [x] Filtros interactivos avanzados
- [x] Visualizaciones con Plotly
- [x] Documentación completa

### 🔄 Fase 2: Mejoras (En Progreso)
- [ ] Modelos de Machine Learning (Random Forest, XGBoost)
- [ ] Exportación de datos filtrados (CSV, Excel)
- [ ] Modo oscuro/claro
- [ ] Soporte multiidioma (EN/ES)

### 📋 Fase 3: Avanzado (Planificado)
- [ ] Integración con APIs en tiempo real
- [ ] Sistema de alertas por email
- [ ] Análisis de clustering espacial
- [ ] App móvil complementaria

### 🌟 Fase 4: Futuro
- [ ] Integración con GIS y mapas de elevación
- [ ] Predicciones en tiempo real con IA
- [ ] API REST pública
- [ ] Colaboración con organizaciones de protección civil

---

<div align="center">

### 🌊 Juntos hacia un mundo más resiliente a tsunamis

**Si este proyecto te resultó útil, considera darle una ⭐️**

[⬆️ Volver arriba](#-global-earthquake--tsunami-risk-assessment)

---

**Hecho con ❤️ por el Equipo de Análisis de Datos**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/earthquake-tsunami-dashboard)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/earthquakedash)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/company/earthquake-dashboard)

</div>
