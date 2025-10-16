"""
Filters Component
=================

Componente de filtros interactivos para el dataset.
Permite filtrar por año, magnitud, profundidad, tsunami, etc.
"""

import streamlit as st
import pandas as pd


# ============================================================================
# FUNCIÓN PRINCIPAL DE FILTROS
# ============================================================================

def apply_filters(df):
    """
    Renderiza controles de filtro y retorna el DataFrame filtrado.
    
    Args:
        df (pd.DataFrame): DataFrame original
        
    Returns:
        pd.DataFrame: DataFrame filtrado según las selecciones del usuario
    """
    
    df_filtered = df.copy()
    
    # ===== FILTRO DE AÑOS =====
    st.markdown("#### 📅 Período de Tiempo")
    
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    
    year_range = st.slider(
        "Rango de años:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )
    
    df_filtered = df_filtered[
        (df_filtered['Year'] >= year_range[0]) & 
        (df_filtered['Year'] <= year_range[1])
    ]
    
    # ===== FILTRO DE MAGNITUD =====
    st.markdown("#### 📏 Magnitud")
    
    min_mag = float(df['magnitude'].min())
    max_mag = float(df['magnitude'].max())
    
    mag_range = st.slider(
        "Rango de magnitud:",
        min_value=min_mag,
        max_value=max_mag,
        value=(min_mag, max_mag),
        step=0.1
    )
    
    df_filtered = df_filtered[
        (df_filtered['magnitude'] >= mag_range[0]) & 
        (df_filtered['magnitude'] <= mag_range[1])
    ]
    
    # ===== FILTRO DE PROFUNDIDAD =====
    st.markdown("#### 🌍 Profundidad")
    
    max_depth = st.slider(
        "Profundidad máxima (km):",
        min_value=0,
        max_value=int(df['depth'].max()),
        value=int(df['depth'].max()),
        step=10
    )
    
    df_filtered = df_filtered[df_filtered['depth'] <= max_depth]
    
    # ===== FILTRO DE TSUNAMI =====
    st.markdown("#### 🌊 Tipo de Evento")
    
    tsunami_filter = st.selectbox(
        "Filtrar por tsunami:",
        options=["Todos", "Solo con Tsunami", "Solo sin Tsunami"]
    )
    
    if tsunami_filter == "Solo con Tsunami":
        df_filtered = df_filtered[df_filtered['tsunami'] == 1]
    elif tsunami_filter == "Solo sin Tsunami":
        df_filtered = df_filtered[df_filtered['tsunami'] == 0]
    
    # ===== FILTRO DE REGIÓN (por hemisferio) =====
    st.markdown("#### 🗺️ Región Geográfica")
    
    regions = st.multiselect(
        "Selecciona hemisferios:",
        options=["Norte", "Sur", "Este", "Oeste"],
        default=["Norte", "Sur", "Este", "Oeste"]
    )
    
    # Aplicar filtro de región
    if "Norte" not in regions:
        df_filtered = df_filtered[df_filtered['latitude'] < 0]
    if "Sur" not in regions:
        df_filtered = df_filtered[df_filtered['latitude'] >= 0]
    if "Este" not in regions:
        df_filtered = df_filtered[df_filtered['longitude'] < 0]
    if "Oeste" not in regions:
        df_filtered = df_filtered[df_filtered['longitude'] >= 0]
    
    # ===== FILTRO AVANZADO (opcional) =====
    with st.expander("⚙️ Filtros Avanzados"):
        
        # Filtro por categoría de magnitud
        if 'magnitude_category' in df.columns:
            mag_cats = st.multiselect(
                "Categorías de magnitud:",
                options=df['magnitude_category'].dropna().unique().tolist(),
                default=df['magnitude_category'].dropna().unique().tolist()
            )
            
            if mag_cats:
                df_filtered = df_filtered[df_filtered['magnitude_category'].isin(mag_cats)]
        
        # Filtro por significancia
        if 'sig' in df.columns:
            min_sig = st.number_input(
                "Significancia mínima:",
                min_value=int(df['sig'].min()),
                max_value=int(df['sig'].max()),
                value=int(df['sig'].min())
            )
            
            df_filtered = df_filtered[df_filtered['sig'] >= min_sig]
        
        # Filtro por eventos superficiales
        shallow_only = st.checkbox("Solo eventos superficiales (< 50km)", value=False)
        if shallow_only:
            df_filtered = df_filtered[df_filtered['depth'] < 50]
        
        # Filtro por magnitud alta
        high_mag_only = st.checkbox("Solo magnitud alta (≥ 7.0)", value=False)
        if high_mag_only:
            df_filtered = df_filtered[df_filtered['magnitude'] >= 7.0]
    
    # ===== BOTÓN DE RESET =====
    if st.button("🔄 Resetear Filtros", use_container_width=True):
        st.rerun()
    
    return df_filtered


# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def get_filter_summary(df_original, df_filtered):
    """
    Genera un resumen de los filtros aplicados.
    
    Args:
        df_original (pd.DataFrame): DataFrame original
        df_filtered (pd.DataFrame): DataFrame filtrado
        
    Returns:
        dict: Diccionario con estadísticas de filtrado
    """
    
    summary = {
        'original_count': len(df_original),
        'filtered_count': len(df_filtered),
        'percentage': (len(df_filtered) / len(df_original)) * 100 if len(df_original) > 0 else 0,
        'removed_count': len(df_original) - len(df_filtered),
        'tsunami_count': df_filtered['tsunami'].sum() if 'tsunami' in df_filtered.columns else 0,
        'tsunami_percentage': (df_filtered['tsunami'].sum() / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    }
    
    return summary
