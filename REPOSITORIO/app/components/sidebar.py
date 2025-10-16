"""
Sidebar Component
=================

Componente del menú lateral con navegación y filtros interactivos.
"""

import streamlit as st
from components.filters import apply_filters


# ============================================================================
# FUNCIÓN PRINCIPAL DEL SIDEBAR
# ============================================================================

def render_sidebar(df):
    """
    Renderiza el menú lateral con navegación y filtros.
    
    Args:
        df (pd.DataFrame): DataFrame completo de terremotos
        
    Returns:
        tuple: (página_seleccionada, dataframe_filtrado)
    """
    
    with st.sidebar:
        # Logo y título del sidebar
        st.markdown(
            """
            <div style='text-align: center; padding: 20px 0;'>
                <h1 style='color: white; font-size: 2.5rem;'>🌊</h1>
                <h3 style='color: white;'>Dashboard</h3>
                <p style='color: #bbb; font-size: 0.9rem;'>Análisis Sísmico Global</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        
        # ===== NAVEGACIÓN =====
        st.markdown("### 🧭 Navegación")
        
        pages = [
            "🏠 Inicio",
            "📊 Exploración de Datos",
            "🗺️ Análisis Geoespacial",
            "📅 Análisis Temporal",
            "🔬 Análisis Multivariable",
            "📝 Conclusiones",
            "🤖 Machine Learning"
        ]
        
        page_selected = st.radio(
            label="Selecciona una sección:",
            options=pages,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # ===== FILTROS =====
        st.markdown("### 🎛️ Filtros de Datos")
        
        # Aplicar filtros y obtener el dataframe filtrado
        df_filtered = apply_filters(df)
        
        st.markdown("---")
        
        # ===== INFORMACIÓN ADICIONAL =====
        with st.expander("ℹ️ Acerca de", expanded=False):
            st.markdown(
                """
                **Dashboard de Análisis Sísmico**
                
                Esta herramienta permite explorar y analizar
                datos de terremotos y tsunamis a nivel global.
                
                **Datos:** 2001-2022  
                **Eventos:** Miles de registros sísmicos  
                **Objetivo:** Evaluación de riesgo tsunamigénico
                
                ---
                
                **Equipo de Desarrollo**  
                Bootcamp de Análisis de Datos 2025
                """
            )
        
        with st.expander("📚 Guía de Uso", expanded=False):
            st.markdown(
                """
                **Cómo usar este dashboard:**
                
                1. **Navegación:** Usa el menú superior para cambiar de sección
                2. **Filtros:** Ajusta los parámetros en este panel lateral
                3. **Interacción:** Los gráficos son interactivos (zoom, hover, etc.)
                4. **Descarga:** Muchas visualizaciones permiten exportar datos
                
                **Filtros disponibles:**
                - Rango de años
                - Rango de magnitud
                - Profundidad máxima
                - Tipo de evento (con/sin tsunami)
                - Regiones geográficas
                """
            )
    
    return page_selected, df_filtered
