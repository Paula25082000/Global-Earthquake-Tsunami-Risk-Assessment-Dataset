# Panel de Inteligencia: Global Earthquake & Tsunami Risk Assessment

## 🌊 Descripción

Dashboard interactivo desarrollado en Streamlit para análisis exploratorio y evaluación de riesgo tsunamigénico basado en datos sísmicos globales (2001-2022).

## 📋 Características

- **📊 Exploración de Datos**: Distribuciones, correlaciones y estadísticas descriptivas
- **🗺️ Análisis Geoespacial**: Mapas interactivos y patrones geográficos
- **📅 Análisis Temporal**: Tendencias y evolución en el tiempo
- **🔬 Análisis Multivariable**: Relaciones complejas entre variables
- **📝 Conclusiones**: Hallazgos principales y recomendaciones
- **🤖 Machine Learning**: Modelos predictivos (en desarrollo)

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar la Aplicación

```bash
cd app
streamlit run main.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
Global-Earthquake-Tsunami-Risk-Assessment-Dataset/
│
├── app/                          # Aplicación Streamlit
│   ├── main.py                   # Punto de entrada principal
│   ├── components/               # Componentes reutilizables
│   │   ├── __init__.py
│   │   ├── sidebar.py            # Menú lateral y navegación
│   │   └── filters.py            # Filtros interactivos
│   ├── pages/                    # Páginas del dashboard
│   │   ├── __init__.py
│   │   ├── introduccion.py       # Página de inicio
│   │   ├── exploracion_datos.py  # EDA
│   │   ├── analisis_geoespacial.py
│   │   ├── analisis_temporal.py
│   │   ├── analisis_multivariable.py
│   │   ├── conclusiones.py
│   │   └── machine_learning.py
│   └── utils/                    # Utilidades
│       ├── __init__.py
│       ├── data_loader.py        # Carga y preparación de datos
│       └── styles.py             # Estilos CSS personalizados
│
├── data/                         # Datos
│   └── earthquake_data_tsunami.csv
│
├── docs/                         # Documentación
│   ├── EDA.md                    # Informe de análisis exploratorio
│   └── info.md
│
├── notebooks/                    # Notebooks de Jupyter
│   ├── EDA_ Demetrio.ipynb
│   ├── EDA_Paula.ipynb
│   └── preprocesamiento.ipynb
│
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

## 🎯 Uso del Dashboard

### Navegación

Usa el **menú lateral izquierdo** para navegar entre las diferentes secciones:

1. **🏠 Inicio**: Información general y contexto del proyecto
2. **📊 Exploración de Datos**: Análisis estadístico detallado
3. **🗺️ Análisis Geoespacial**: Mapas interactivos
4. **📅 Análisis Temporal**: Tendencias temporales
5. **🔬 Análisis Multivariable**: Relaciones complejas
6. **📝 Conclusiones**: Resumen y recomendaciones
7. **🤖 Machine Learning**: Modelos predictivos

### Filtros Interactivos

En el menú lateral encontrarás filtros para:

- **Período de tiempo**: Rango de años
- **Magnitud**: Rango de magnitud sísmica
- **Profundidad**: Profundidad máxima del hipocentro
- **Tipo de evento**: Con/sin tsunami
- **Región geográfica**: Hemisferios

### Interacción con Gráficos

Todos los gráficos son interactivos:

- **Hover**: Pasa el ratón para ver detalles
- **Zoom**: Haz scroll o usa las herramientas de zoom
- **Pan**: Arrastra para moverte por el gráfico
- **Descargar**: Usa el icono de cámara para exportar imágenes

## 💡 Hallazgos Principales

- **🎯 Factores Críticos**: Magnitud ≥ 7.0 + Profundidad < 50 km = Alto riesgo
- **🌊 Patrones Oceánicos**: Eventos remotos (dmin > 5°) más tsunamigénicos
- **🔥 Cinturón de Fuego**: Concentración en zonas de subducción del Pacífico
- **📅 Sin Estacionalidad**: Riesgo distribuido uniformemente durante el año

## 🔧 Tecnologías Utilizadas

- **Python 3.8+**
- **Streamlit**: Framework web
- **Pandas**: Manipulación de datos
- **NumPy**: Computación numérica
- **Plotly**: Visualizaciones interactivas
- **Scipy**: Análisis estadístico

## 📊 Datos

- **Fuente**: Dataset de terremotos globales con información de tsunamis
- **Período**: 2001-2022
- **Registros**: Miles de eventos sísmicos
- **Variables**: Magnitud, profundidad, localización, tsunami, etc.

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte de un Bootcamp de Análisis de Datos.

**Equipo:**
- Demetrio: Análisis exploratorio y documentación
- Paula: Desarrollo del dashboard y visualizaciones

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

## 📧 Contacto

Para preguntas, sugerencias o colaboraciones, por favor contacta al equipo del proyecto.

---

**🌍 Juntos hacia un mundo más resiliente a tsunamis** 🌊
