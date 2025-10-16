"""
Panel de Inteligencia: Global Earthquake & Tsunami Risk Assessment
==================================================================

Aplicación principal de Streamlit para análisis interactivo de datos sísmicos
y evaluación de riesgo tsunamigénico.

Autor: Equipo de Análisis
Fecha: 2025-10-16
"""

import streamlit as st
from components.sidebar import render_sidebar
from components.filters import apply_filters
from pages import (
    introduccion,
    exploracion_datos,
    analisis_geoespacial,
    analisis_temporal,
    analisis_multivariable,
    conclusiones,
    machine_learning
)
from utils.data_loader import load_data, get_data_info
from utils.styles import apply_custom_css


# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Earthquake & Tsunami Dashboard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que orquesta la aplicación de Streamlit.
    Carga datos, aplica estilos, renderiza la navegación y muestra las páginas.
    """
    
    # Aplicar estilos CSS personalizados
    apply_custom_css()
    
    # Título principal de la aplicación
    st.title("🌊 Panel de Inteligencia: Terremotos y Tsunamis")
    st.markdown("### *Global Earthquake & Tsunami Risk Assessment Dashboard*")
    st.markdown("---")
    
    # Cargar datos en la sesión de Streamlit
    with st.spinner("Cargando datos..."):
        df = load_data()
    
    # Verificar que los datos se cargaron correctamente
    if df is None:
        st.error("❌ Error al cargar los datos. Verifica que el archivo CSV existe.")
        st.stop()
    
    # Mostrar información básica de los datos cargados
    with st.expander("ℹ️ Información del Dataset", expanded=False):
        data_info = get_data_info(df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Eventos", data_info['total_events'])
        col2.metric("Eventos con Tsunami", data_info['tsunami_events'])
        col3.metric("% Tsunamis", f"{data_info['tsunami_percentage']:.2f}%")
        col4.metric("Años de Datos", data_info['years_span'])
    
    # Renderizar el menú lateral con filtros y navegación
    page_selected, df_filtered = render_sidebar(df)
    
    # Mostrar advertencia si no hay datos después de aplicar filtros
    if df_filtered.empty:
        st.warning("⚠️ No hay datos disponibles con los filtros seleccionados. Ajusta los parámetros.")
        st.stop()
    
    # Mostrar métricas de datos filtrados
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Datos Filtrados")
    st.sidebar.info(f"**Eventos:** {len(df_filtered)} de {len(df)}")
    st.sidebar.info(f"**Tsunamis:** {df_filtered['tsunami'].sum()} "
                   f"({df_filtered['tsunami'].sum()/len(df_filtered)*100:.1f}%)")
    
    # Navegación entre páginas
    st.markdown("---")
    
    # Renderizar la página seleccionada
    if page_selected == "🏠 Inicio":
        introduccion.render(df_filtered)
    
    elif page_selected == "📊 Exploración de Datos":
        exploracion_datos.render(df_filtered)
    
    elif page_selected == "🗺️ Análisis Geoespacial":
        analisis_geoespacial.render(df_filtered)
    
    elif page_selected == "📅 Análisis Temporal":
        analisis_temporal.render(df_filtered)
    
    elif page_selected == "🔬 Análisis Multivariable":
        analisis_multivariable.render(df_filtered)
    
    elif page_selected == "📝 Conclusiones":
        conclusiones.render(df_filtered)
    
    elif page_selected == "🤖 Machine Learning":
        machine_learning.render(df_filtered)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
            <p>🌍 Global Earthquake & Tsunami Risk Assessment Dashboard</p>
            <p>Datos: 2001-2022 | Powered by Streamlit + Plotly</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()
