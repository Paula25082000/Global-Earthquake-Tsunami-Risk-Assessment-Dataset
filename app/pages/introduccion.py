"""
Página de Introducción
======================

Página inicial del dashboard con información general del proyecto.
"""

import streamlit as st
from utils.data_loader import get_variable_descriptions
from utils.styles import create_highlight_box


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def render(df):
    """
    Renderiza la página de introducción.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos (filtrado)
    """
    
    # ===== SECCIÓN DE BIENVENIDA =====
    st.header("🏠 Bienvenido al Dashboard de Análisis Sísmico")
    
    create_highlight_box(
        """
        <h3 style='margin-top: 0;'>🌍 Global Earthquake & Tsunami Risk Assessment</h3>
        <p style='font-size: 1.1rem; line-height: 1.6;'>
        Este panel de inteligencia te permite explorar y analizar datos históricos
        de terremotos y tsunamis para identificar patrones, evaluar riesgos y 
        comprender mejor los factores que determinan la generación de tsunamis.
        </p>
        """
    )
    
    st.markdown("---")
    
    # ===== OBJETIVO DEL PROYECTO =====
    st.subheader("🎯 Objetivo del Proyecto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            **Pregunta Central:**
            
            > ¿Qué condiciones sísmicas hacen más probable que un terremoto genere un tsunami?
            
            **Objetivos Específicos:**
            - 🔍 Identificar señales tempranas de eventos tsunamigénicos
            - 📊 Analizar relaciones entre variables sísmicas
            - 🗺️ Explorar patrones geoespaciales y temporales
            - 🤖 Desarrollar modelos predictivos de riesgo
            """
        )
    
    with col2:
        st.markdown(
            """
            **Aplicaciones Prácticas:**
            - ⚠️ Sistemas de alerta temprana
            - 📈 Evaluación de riesgo en zonas costeras
            - 🏗️ Planificación urbana y de infraestructura
            - 📚 Educación y concienciación pública
            - 🛡️ Políticas de protección civil
            """
        )
    
    st.markdown("---")
    
    # ===== ACERCA DE LOS DATOS =====
    st.subheader("📁 Acerca de los Datos")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Total de Eventos",
            value=f"{len(df):,}",
            help="Número total de eventos sísmicos registrados"
        )
    
    with col2:
        tsunami_count = df['tsunami'].sum()
        st.metric(
            label="🌊 Eventos con Tsunami",
            value=f"{tsunami_count:,}",
            help="Eventos que generaron tsunamis"
        )
    
    with col3:
        tsunami_pct = (df['tsunami'].sum() / len(df) * 100) if len(df) > 0 else 0
        st.metric(
            label="📈 Porcentaje de Tsunamis",
            value=f"{tsunami_pct:.1f}%",
            help="Proporción de eventos con tsunami"
        )
    
    with col4:
        years_span = f"{df['Year'].min()}-{df['Year'].max()}"
        st.metric(
            label="📅 Período de Datos",
            value=years_span,
            help="Rango temporal del dataset"
        )
    
    st.markdown("---")
    
    # ===== INFORMACIÓN DEL DATASET =====
    st.subheader("📋 Estructura del Dataset")
    
    tab1, tab2, tab3 = st.tabs(["📊 Vista Previa", "📖 Diccionario de Variables", "📈 Estadísticas"])
    
    with tab1:
        st.markdown("**Primeras filas del dataset:**")
        st.dataframe(
            df.head(10),
            use_container_width=True,
            height=400
        )
    
    with tab2:
        st.markdown("**Descripción de las variables principales:**")
        
        descriptions = get_variable_descriptions()
        
        # Mostrar descripciones en formato de tabla
        desc_df = {
            'Variable': [],
            'Descripción': []
        }
        
        for var, desc in descriptions.items():
            if var in df.columns:
                desc_df['Variable'].append(f"`{var}`")
                desc_df['Descripción'].append(desc)
        
        import pandas as pd
        desc_table = pd.DataFrame(desc_df)
        
        st.dataframe(
            desc_table,
            use_container_width=True,
            hide_index=True,
            height=500
        )
    
    with tab3:
        st.markdown("**Estadísticas descriptivas:**")
        st.dataframe(
            df.describe().T,
            use_container_width=True
        )
    
    st.markdown("---")
    
    # ===== METODOLOGÍA =====
    st.subheader("🔬 Metodología de Análisis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            **Análisis Exploratorio (EDA):**
            1. Distribuciones univariables
            2. Pruebas de normalidad (Shapiro-Wilk)
            3. Análisis de correlaciones (Spearman)
            4. Exploración geoespacial interactiva
            5. Análisis temporal y estacional
            6. Visualizaciones multivariables
            """
        )
    
    with col2:
        st.markdown(
            """
            **Machine Learning:**
            1. Ingeniería de características
            2. Selección de variables
            3. Modelado predictivo
            4. Validación temporal
            5. Interpretación con SHAP
            6. Reglas de alerta temprana
            """
        )
    
    st.markdown("---")
    
    # ===== HALLAZGOS PRINCIPALES =====
    st.subheader("💡 Hallazgos Principales del EDA")
    
    findings = [
        {
            "icon": "🎯",
            "title": "Factores Tsunamigénicos",
            "content": "Los tsunamis se asocian fuertemente con terremotos de **magnitud ≥ 7.0** y **profundidad < 50 km**."
        },
        {
            "icon": "🌊",
            "title": "Eventos Oceánicos",
            "content": "Muchos tsunamis ocurren en mar abierto, **lejos de estaciones sismológicas** (dmin > 5°)."
        },
        {
            "icon": "🗺️",
            "title": "Cinturón de Fuego",
            "content": "Concentración de eventos críticos en el **Cinturón de Fuego del Pacífico** y zonas de subducción."
        },
        {
            "icon": "📅",
            "title": "Sin Estacionalidad",
            "content": "**No hay estacionalidad clara**; el riesgo se distribuye durante todo el año."
        }
    ]
    
    cols = st.columns(2)
    for i, finding in enumerate(findings):
        with cols[i % 2]:
            st.info(
                f"**{finding['icon']} {finding['title']}**\n\n{finding['content']}"
            )
    
    st.markdown("---")
    
    # ===== REGLAS DE ALERTA TEMPRANA =====
    st.subheader("⚠️ Reglas Heurísticas de Alerta Temprana")
    
    st.warning(
        """
        **Criterios de Alto Riesgo Tsunamigénico:**
        
        🔴 **Riesgo Crítico:**
        - Magnitud ≥ 7.5
        - Profundidad < 30 km
        - Ubicación en zona oceánica (dmin > 5°)
        
        🟡 **Riesgo Elevado:**
        - Magnitud entre 7.0 y 7.5
        - Profundidad entre 30-50 km
        - Significancia (sig) muy alta
        
        🟢 **Riesgo Moderado:**
        - Magnitud entre 6.5 y 7.0
        - Profundidad entre 50-100 km
        - MMI/CDI ≥ 5 cerca de costa
        
        *Nota: Estas reglas son heurísticas iniciales basadas en el análisis exploratorio.*
        """
    )
    
    st.markdown("---")
    
    # ===== CÓMO USAR EL DASHBOARD =====
    st.subheader("📖 Cómo Usar este Dashboard")
    
    with st.expander("🧭 Guía de Navegación", expanded=True):
        st.markdown(
            """
            **Secciones Disponibles:**
            
            1. **🏠 Inicio** (esta página): Información general y contexto
            2. **📊 Exploración de Datos**: Distribuciones, correlaciones y estadísticas
            3. **🗺️ Análisis Geoespacial**: Mapas interactivos y patrones geográficos
            4. **📅 Análisis Temporal**: Tendencias y evolución en el tiempo
            5. **🔬 Análisis Multivariable**: Relaciones complejas entre variables
            6. **📝 Conclusiones**: Resumen de hallazgos y recomendaciones
            7. **🤖 Machine Learning**: Modelos predictivos (en desarrollo)
            
            **Interacción:**
            - Usa el **menú lateral** para navegar entre secciones
            - Ajusta los **filtros** para explorar subconjuntos de datos
            - **Haz hover** sobre los gráficos para ver detalles
            - **Haz zoom** y **pan** en las visualizaciones interactivas
            - **Descarga** datos y gráficos cuando esté disponible
            """
        )
    
    st.markdown("---")
    
    # ===== FOOTER =====
    st.info(
        """
        📚 **Referencias:**
        - Documento de EDA: `docs/EDA.md`
        - Notebook de análisis: `notebooks/EDA_ Demetrio.ipynb`
        - Dataset: `data/earthquake_data_tsunami.csv`
        
        🤝 **Equipo de Desarrollo:** Bootcamp de Análisis de Datos 2025
        """
    )
