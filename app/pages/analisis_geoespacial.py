"""
Página de Análisis Geoespacial
===============================

Mapas interactivos y análisis de patrones geográficos.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def render(df):
    """
    Renderiza la página de análisis geoespacial.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos (filtrado)
    """
    
    st.header("🗺️ Análisis Geoespacial")
    st.markdown("Exploración de patrones geográficos y distribución espacial de eventos sísmicos.")
    st.markdown("---")
    
    # ===== MAPA PRINCIPAL =====
    st.subheader("🌍 Distribución Global de Terremotos")
    
    render_main_map(df)
    
    st.markdown("---")
    
    # ===== MAPAS TEMÁTICOS =====
    st.subheader("🗺️ Mapas Temáticos")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌊 Tsunamis vs Profundidad",
        "🔥 Cinturón de Fuego",
        "🎯 Calidad de Monitoreo",
        "⚡ Eventos Significativos"
    ])
    
    with tab1:
        render_tsunami_depth_map(df)
    
    with tab2:
        render_ring_of_fire_map(df)
    
    with tab3:
        render_monitoring_quality_map(df)
    
    with tab4:
        render_significant_events_map(df)


# ============================================================================
# MAPA PRINCIPAL
# ============================================================================

def render_main_map(df):
    """Renderiza el mapa principal de distribución global."""
    
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        color_by = st.selectbox(
            "Colorear por:",
            options=['magnitude', 'depth', 'sig', 'tsunami_label'],
            index=0
        )
    
    with col2:
        size_by = st.selectbox(
            "Tamaño por:",
            options=['sig', 'magnitude', 'depth'],
            index=0
        )
    
    with col3:
        projection = st.selectbox(
            "Proyección:",
            options=['natural earth', 'orthographic', 'equirectangular'],
            index=0
        )
    
    # Crear mapa
    if color_by == 'tsunami_label':
        fig = px.scatter_geo(
            df,
            lat='latitude',
            lon='longitude',
            color='tsunami_label',
            size=size_by,
            hover_data=['magnitude', 'depth', 'sig', 'Year'],
            color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
            projection=projection,
            title='Distribución Global de Terremotos'
        )
    else:
        fig = px.scatter_geo(
            df,
            lat='latitude',
            lon='longitude',
            color=color_by,
            size=size_by,
            hover_data=['magnitude', 'depth', 'tsunami', 'sig', 'Year'],
            projection=projection,
            title='Distribución Global de Terremotos',
            color_continuous_scale='Viridis'
        )
    
    fig.update_layout(
        height=700,
        geo=dict(
            showland=True,
            landcolor='lightgray',
            showocean=True,
            oceancolor='lightblue',
            showcountries=True,
            countrycolor='white',
            showcoastlines=True,
            coastlinecolor='white'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Estadísticas del mapa
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Eventos Visibles", f"{len(df):,}")
    
    with col2:
        mag_avg = df['magnitude'].mean()
        st.metric("Magnitud Media", f"{mag_avg:.2f}")
    
    with col3:
        depth_avg = df['depth'].mean()
        st.metric("Profundidad Media", f"{depth_avg:.1f} km")
    
    with col4:
        tsunami_pct = (df['tsunami'].sum() / len(df) * 100) if len(df) > 0 else 0
        st.metric("% con Tsunami", f"{tsunami_pct:.1f}%")


# ============================================================================
# MAPA: TSUNAMIS VS PROFUNDIDAD
# ============================================================================

def render_tsunami_depth_map(df):
    """Mapa de análisis crítico: tsunamis vs profundidad del epicentro."""
    
    st.markdown("""
    **Análisis Crítico:** Relación entre generación de tsunamis y profundidad del terremoto.
    
    🔴 **Puntos rojos** = Eventos con tsunami  
    🔵 **Puntos azules** = Eventos sin tsunami  
    📏 **Tamaño** = Profundidad del epicentro
    """)
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='tsunami_label',
        size='depth',
        hover_data=['magnitude', 'depth', 'sig', 'Year'],
        color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
        title='🌊 Tsunamis vs Profundidad del Epicentro',
        labels={'tsunami_label': 'Tipo', 'depth': 'Profundidad (km)'}
    )
    
    fig.update_layout(
        height=600,
        geo=dict(
            showland=True,
            landcolor='darkgreen',
            showocean=True,
            oceancolor='darkblue',
            showcountries=True,
            countrycolor='gray',
            showcoastlines=True,
            coastlinecolor='white'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Insights
    shallow_tsunami = df[(df['depth'] < 50) & (df['tsunami'] == 1)]
    deep_tsunami = df[(df['depth'] >= 50) & (df['tsunami'] == 1)]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **Tsunamis Superficiales (< 50km):**  
        {len(shallow_tsunami)} eventos ({len(shallow_tsunami)/df['tsunami'].sum()*100:.1f}% del total de tsunamis)
        """)
    
    with col2:
        st.info(f"""
        **Tsunamis Profundos (≥ 50km):**  
        {len(deep_tsunami)} eventos ({len(deep_tsunami)/df['tsunami'].sum()*100:.1f}% del total de tsunamis)
        """)


# ============================================================================
# MAPA: CINTURÓN DE FUEGO
# ============================================================================

def render_ring_of_fire_map(df):
    """Mapa del Cinturón de Fuego del Pacífico."""
    
    st.markdown("""
    **Cinturón de Fuego del Pacífico:** Zona de alta actividad sísmica y volcánica.
    
    🔶 **Diamantes** = Eventos con tsunami  
    🔵 **Círculos** = Eventos sin tsunami  
    🎨 **Color** = Magnitud del evento
    """)
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='magnitude',
        size='sig',
        symbol='tsunami',
        hover_data=['depth', 'Year', 'sig'],
        color_continuous_scale='Viridis',
        symbol_map={0: 'circle', 1: 'diamond'},
        title='🔥 Cinturón de Fuego: Zonas de Alto Riesgo Tsunamigénico',
        labels={'magnitude': 'Magnitud', 'sig': 'Significancia'}
    )
    
    fig.update_layout(
        height=600,
        geo=dict(
            showland=True,
            landcolor='saddlebrown',
            showocean=True,
            oceancolor='navy',
            showcountries=True,
            countrycolor='gray',
            showcoastlines=True,
            coastlinecolor='yellow',
            projection_type='orthographic',
            projection_rotation=dict(lon=-160, lat=0, roll=0)
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Regiones de mayor actividad
    st.markdown("#### 📍 Regiones de Mayor Actividad")
    
    # Definir regiones del cinturón de fuego
    regions = {
        'Pacífico Occidental': (df['longitude'] >= 120) & (df['longitude'] <= 180),
        'Sudamérica': (df['latitude'] < 0) & (df['longitude'] >= -90) & (df['longitude'] <= -60),
        'Centroamérica': (df['latitude'] >= 0) & (df['latitude'] <= 20) & (df['longitude'] >= -110) & (df['longitude'] <= -80),
        'Japón': (df['latitude'] >= 30) & (df['latitude'] <= 45) & (df['longitude'] >= 130) & (df['longitude'] <= 145)
    }
    
    region_stats = []
    for region_name, region_mask in regions.items():
        region_df = df[region_mask]
        if len(region_df) > 0:
            region_stats.append({
                'Región': region_name,
                'Eventos': len(region_df),
                'Tsunamis': region_df['tsunami'].sum(),
                '% Tsunamis': f"{region_df['tsunami'].sum()/len(region_df)*100:.1f}%"
            })
    
    if region_stats:
        import pandas as pd
        stats_df = pd.DataFrame(region_stats)
        st.dataframe(stats_df, use_container_width=True, hide_index=True)


# ============================================================================
# MAPA: CALIDAD DE MONITOREO
# ============================================================================

def render_monitoring_quality_map(df):
    """Mapa de cobertura y calidad del monitoreo sísmico."""
    
    st.markdown("""
    **Evaluación de la cobertura del monitoreo sísmico global:**
    
    🎨 **Color** = Número de estaciones que registraron el evento  
    📏 **Tamaño** = Distancia mínima a una estación (dmin)
    """)
    
    if 'nst' in df.columns and 'dmin' in df.columns:
        fig = px.scatter_geo(
            df,
            lat='latitude',
            lon='longitude',
            color='nst',
            size='dmin',
            hover_data=['magnitude', 'gap', 'sig', 'tsunami'],
            color_continuous_scale='RdYlGn',
            title='🎯 Cobertura de Monitoreo: Estaciones vs Distancia',
            labels={'nst': 'Nº Estaciones', 'dmin': 'Distancia Mín. (°)'}
        )
        
        fig.update_layout(
            height=600,
            geo=dict(
                showland=True,
                landcolor='olive',
                showocean=True,
                oceancolor='teal',
                showcountries=True,
                countrycolor='white',
                showcoastlines=True,
                coastlinecolor='orange'
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Análisis de calidad
        col1, col2, col3 = st.columns(3)
        
        with col1:
            high_quality = df[df['nst'] >= df['nst'].quantile(0.75)]
            st.metric("Alta Cobertura", f"{len(high_quality):,}", 
                     help="Eventos con más estaciones (Q3)")
        
        with col2:
            remote_events = df[df['dmin'] > 5]
            st.metric("Eventos Remotos", f"{len(remote_events):,}",
                     help="Eventos con dmin > 5°")
        
        with col3:
            if 'monitoring_quality' in df.columns:
                avg_quality = df['monitoring_quality'].mean()
                st.metric("Calidad Media", f"{avg_quality:.2f}",
                         help="Índice de calidad de monitoreo (0-1)")
    
    else:
        st.warning("⚠️ No hay datos de monitoreo disponibles (nst, dmin) en el dataset filtrado.")


# ============================================================================
# MAPA: EVENTOS SIGNIFICATIVOS
# ============================================================================

def render_significant_events_map(df):
    """Mapa de eventos significativos por impacto."""
    
    st.markdown("""
    **Análisis de eventos significativos vs su impacto tsunamigénico real:**
    
    ⭐ **Estrellas** = Eventos con tsunami  
    🔵 **Círculos** = Eventos sin tsunami  
    🎨 **Color** = Puntaje de significancia
    """)
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='sig',
        size='impact_level' if 'impact_level' in df.columns else 'sig',
        symbol='tsunami',
        hover_data=['magnitude', 'depth', 'Year'],
        color_continuous_scale='Hot',
        symbol_map={0: 'circle', 1: 'star'},
        title='⚡ Significancia vs Impacto: Eventos Críticos',
        labels={'sig': 'Significancia', 'impact_level': 'Impacto'}
    )
    
    fig.update_layout(
        height=600,
        geo=dict(
            showland=True,
            landcolor='dimgray',
            showocean=True,
            oceancolor='indigo',
            showcountries=True,
            countrycolor='silver',
            showcoastlines=True,
            coastlinecolor='gold'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Top eventos más significativos
    st.markdown("#### 🏆 Top 10 Eventos Más Significativos")
    
    top_events = df.nlargest(10, 'sig')[
        ['Year', 'Month', 'magnitude', 'depth', 'sig', 'tsunami_label', 'latitude', 'longitude']
    ].copy()
    
    top_events.columns = ['Año', 'Mes', 'Magnitud', 'Profundidad', 'Significancia', 'Tsunami', 'Lat', 'Lon']
    
    st.dataframe(
        top_events,
        use_container_width=True,
        hide_index=True
    )
