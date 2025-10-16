"""
Página de Análisis Temporal
============================

Análisis de tendencias, evolución y patrones temporales.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def render(df):
    """
    Renderiza la página de análisis temporal.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos (filtrado)
    """
    
    st.header("📅 Análisis Temporal")
    st.markdown("Exploración de tendencias y patrones en el tiempo.")
    st.markdown("---")
    
    # ===== TABS =====
    tab1, tab2, tab3 = st.tabs([
        "📈 Evolución Anual",
        "📊 Análisis Mensual",
        "🎬 Animaciones Temporales"
    ])
    
    with tab1:
        render_yearly_analysis(df)
    
    with tab2:
        render_monthly_analysis(df)
    
    with tab3:
        render_temporal_animations(df)


# ============================================================================
# ANÁLISIS ANUAL
# ============================================================================

def render_yearly_analysis(df):
    """Análisis de tendencias anuales."""
    
    st.subheader("📈 Evolución Anual de Eventos")
    
    # Agregación por año
    yearly_stats = df.groupby('Year').agg({
        'magnitude': ['count', 'mean', 'max'],
        'tsunami': 'sum',
        'depth': 'mean',
        'sig': 'mean'
    }).reset_index()
    
    yearly_stats.columns = ['Year', 'event_count', 'mag_mean', 'mag_max', 
                            'tsunami_count', 'depth_mean', 'sig_mean']
    
    # Gráfico de líneas: eventos por año
    fig1 = go.Figure()
    
    fig1.add_trace(go.Scatter(
        x=yearly_stats['Year'],
        y=yearly_stats['event_count'],
        name='Total de Eventos',
        line=dict(color='#1f77b4', width=3),
        mode='lines+markers'
    ))
    
    fig1.add_trace(go.Scatter(
        x=yearly_stats['Year'],
        y=yearly_stats['tsunami_count'],
        name='Eventos con Tsunami',
        line=dict(color='#ff4444', width=3),
        mode='lines+markers'
    ))
    
    fig1.update_layout(
        title='Evolución Anual de Eventos Sísmicos',
        xaxis_title='Año',
        yaxis_title='Número de Eventos',
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Gráfico de barras: magnitud promedio por año
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = px.bar(
            yearly_stats,
            x='Year',
            y='mag_mean',
            title='Magnitud Promedio por Año',
            labels={'mag_mean': 'Magnitud Media'},
            color='mag_mean',
            color_continuous_scale='Viridis'
        )
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        fig3 = px.bar(
            yearly_stats,
            x='Year',
            y='tsunami_count',
            title='Tsunamis por Año',
            labels={'tsunami_count': 'Número de Tsunamis'},
            color='tsunami_count',
            color_continuous_scale='Reds'
        )
        fig3.update_layout(height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    # Tabla de estadísticas anuales
    st.markdown("#### 📋 Estadísticas Anuales")
    st.dataframe(
        yearly_stats.round(2),
        use_container_width=True,
        hide_index=True
    )


# ============================================================================
# ANÁLISIS MENSUAL
# ============================================================================

def render_monthly_analysis(df):
    """Análisis de patrones mensuales y estacionalidad."""
    
    st.subheader("📊 Análisis Mensual y Estacionalidad")
    
    # Agregación por mes (promedio entre años)
    monthly_stats = df.groupby('Month').agg({
        'magnitude': ['count', 'mean'],
        'tsunami': 'sum',
        'depth': 'mean'
    }).reset_index()
    
    monthly_stats.columns = ['Month', 'event_count', 'mag_mean', 'tsunami_count', 'depth_mean']
    
    # Nombres de meses
    month_names = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                   'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    monthly_stats['Month_Name'] = monthly_stats['Month'].apply(lambda x: month_names[x-1])
    
    # Gráfico de barras: eventos por mes
    fig1 = px.bar(
        monthly_stats,
        x='Month_Name',
        y='event_count',
        title='Distribución Mensual de Eventos',
        labels={'Month_Name': 'Mes', 'event_count': 'Número de Eventos'},
        color='event_count',
        color_continuous_scale='Blues'
    )
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Gráficos en columnas
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico radial: tsunamis por mes
        fig2 = go.Figure(data=go.Scatterpolar(
            r=monthly_stats['tsunami_count'],
            theta=monthly_stats['Month_Name'],
            fill='toself',
            line=dict(color='#ff4444'),
            marker=dict(size=8)
        ))
        
        fig2.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, monthly_stats['tsunami_count'].max() * 1.1])
            ),
            title='Tsunamis por Mes (Gráfico Radial)',
            height=400
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Magnitud promedio por mes
        fig3 = px.line(
            monthly_stats,
            x='Month_Name',
            y='mag_mean',
            title='Magnitud Promedio por Mes',
            labels={'Month_Name': 'Mes', 'mag_mean': 'Magnitud Media'},
            markers=True
        )
        fig3.update_layout(height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    # Conclusión sobre estacionalidad
    max_month = monthly_stats.loc[monthly_stats['event_count'].idxmax(), 'Month_Name']
    min_month = monthly_stats.loc[monthly_stats['event_count'].idxmin(), 'Month_Name']
    
    st.info(f"""
    **📊 Observación sobre Estacionalidad:**
    
    El mes con más eventos es **{max_month}** ({monthly_stats['event_count'].max()} eventos), 
    y el mes con menos eventos es **{min_month}** ({monthly_stats['event_count'].min()} eventos).
    
    La variación es **{((monthly_stats['event_count'].max() - monthly_stats['event_count'].min()) / monthly_stats['event_count'].mean() * 100):.1f}%** 
    respecto a la media, lo que sugiere que **no hay una estacionalidad fuerte** en la ocurrencia de terremotos.
    """)


# ============================================================================
# ANIMACIONES TEMPORALES
# ============================================================================

def render_temporal_animations(df):
    """Visualizaciones animadas temporales."""
    
    st.subheader("🎬 Evolución Temporal Animada")
    
    st.markdown("""
    Explora cómo han evolucionado los eventos sísmicos a lo largo del tiempo.
    Usa los controles de reproducción para ver la animación.
    """)
    
    # Preparar datos agregados por año y mes
    monthly_data = df.groupby(['Year', 'Month', 'tsunami_label']).agg({
        'magnitude': ['mean', 'max', 'count'],
        'depth': 'mean',
        'sig': 'mean'
    }).reset_index()
    
    monthly_data.columns = ['Year', 'Month', 'tsunami_label', 'mag_mean', 
                            'mag_max', 'event_count', 'depth_mean', 'sig_mean']
    
    monthly_data['Date'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(day=1))
    
    # Gráfico animado: magnitud promedio por año
    fig = px.bar(
        monthly_data,
        x='Date',
        y='mag_mean',
        color='tsunami_label',
        animation_frame='Year',
        color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
        hover_data=['mag_max', 'event_count', 'depth_mean'],
        title='📊 Evolución de Magnitud Promedio por Año (Animado)',
        labels={
            'mag_mean': 'Magnitud Promedio',
            'Date': 'Fecha',
            'tsunami_label': 'Tipo'
        },
        range_y=[monthly_data['mag_mean'].min() * 0.95, monthly_data['mag_mean'].max() * 1.05]
    )
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Mapa animado temporal
    st.markdown("#### 🗺️ Mapa Temporal de Eventos")
    
    # Preparar datos para mapa animado
    df_map = df.copy()
    df_map = df_map.sort_values('Year')
    
    fig_map = px.scatter_geo(
        df_map,
        lat='latitude',
        lon='longitude',
        color='tsunami_label',
        size='magnitude',
        animation_frame='Year',
        hover_data=['magnitude', 'depth', 'Month'],
        color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
        projection='natural earth',
        title='Evolución Geoespacial de Eventos por Año'
    )
    
    fig_map.update_layout(
        height=600,
        geo=dict(
            showland=True,
            landcolor='lightgray',
            showocean=True,
            oceancolor='lightblue',
            showcountries=True,
            showcoastlines=True
        )
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Distribución anual de tsunamis
    st.markdown("#### 🌊 Distribución Anual de Tsunamis")
    
    tsunami_yearly = df[df['tsunami'] == 1].groupby('Year').size().reset_index(name='count')
    
    fig_tsunami = px.bar(
        tsunami_yearly,
        x='Year',
        y='count',
        title='Número de Tsunamis por Año',
        labels={'count': 'Número de Tsunamis', 'Year': 'Año'},
        color='count',
        color_continuous_scale='Reds'
    )
    
    fig_tsunami.update_layout(height=400)
    st.plotly_chart(fig_tsunami, use_container_width=True)
