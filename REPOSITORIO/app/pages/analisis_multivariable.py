"""
Página de Análisis Multivariable
=================================

Análisis de relaciones complejas entre múltiples variables.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def render(df):
    """
    Renderiza la página de análisis multivariable.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos (filtrado)
    """
    
    st.header("🔬 Análisis Multivariable")
    st.markdown("Exploración de relaciones complejas entre múltiples variables.")
    st.markdown("---")
    
    # ===== TABS =====
    tab1, tab2, tab3 = st.tabs([
        "📊 Scatter 3D",
        "📉 Coordenadas Paralelas",
        "🔄 Análisis de Pares"
    ])
    
    with tab1:
        render_3d_scatter(df)
    
    with tab2:
        render_parallel_coordinates(df)
    
    with tab3:
        render_pairwise_analysis(df)


# ============================================================================
# SCATTER 3D
# ============================================================================

def render_3d_scatter(df):
    """Visualización 3D interactiva."""
    
    st.subheader("📊 Análisis 3D: Magnitud, Profundidad y Significancia")
    
    st.markdown("""
    Explora la relación entre tres variables clave en un espacio tridimensional.
    🔴 **Rojo** = Eventos con tsunami | 🔵 **Azul** = Eventos sin tsunami
    """)
    
    # Controles
    col1, col2, col3 = st.columns(3)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude_cols = ['Year', 'Month', 'tsunami', 'is_shallow', 'high_mag', 'oceanic_event']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    with col1:
        x_var = st.selectbox("Eje X:", numeric_cols, 
                            index=numeric_cols.index('magnitude') if 'magnitude' in numeric_cols else 0)
    
    with col2:
        y_var = st.selectbox("Eje Y:", numeric_cols, 
                            index=numeric_cols.index('depth') if 'depth' in numeric_cols else 1)
    
    with col3:
        z_var = st.selectbox("Eje Z:", numeric_cols, 
                            index=numeric_cols.index('sig') if 'sig' in numeric_cols else 2)
    
    # Crear gráfico 3D
    fig = px.scatter_3d(
        df,
        x=x_var,
        y=y_var,
        z=z_var,
        color='tsunami_label',
        size='sig' if 'sig' in df.columns else x_var,
        hover_data=['latitude', 'longitude', 'Year'],
        color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
        title=f'Análisis 3D: {x_var} vs {y_var} vs {z_var}',
        labels={'tsunami_label': 'Tipo'}
    )
    
    fig.update_layout(
        height=700,
        scene=dict(
            xaxis_title=x_var,
            yaxis_title=y_var,
            zaxis_title=z_var
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Insights
    st.markdown("#### 💡 Observaciones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tsunami_df = df[df['tsunami'] == 1]
        st.info(f"""
        **Eventos con Tsunami:**
        - {x_var} medio: {tsunami_df[x_var].mean():.2f}
        - {y_var} medio: {tsunami_df[y_var].mean():.2f}
        - {z_var} medio: {tsunami_df[z_var].mean():.2f}
        """)
    
    with col2:
        no_tsunami_df = df[df['tsunami'] == 0]
        st.info(f"""
        **Eventos sin Tsunami:**
        - {x_var} medio: {no_tsunami_df[x_var].mean():.2f}
        - {y_var} medio: {no_tsunami_df[y_var].mean():.2f}
        - {z_var} medio: {no_tsunami_df[z_var].mean():.2f}
        """)


# ============================================================================
# COORDENADAS PARALELAS
# ============================================================================

def render_parallel_coordinates(df):
    """Gráfico de coordenadas paralelas."""
    
    st.subheader("📉 Coordenadas Paralelas")
    
    st.markdown("""
    Visualiza múltiples variables simultáneamente para identificar patrones.
    Cada línea representa un evento sísmico.
    """)
    
    # Limitar cantidad de datos para rendimiento
    sample_size = st.slider(
        "Número de eventos a mostrar:",
        min_value=100,
        max_value=min(1000, len(df)),
        value=min(500, len(df)),
        step=100,
        help="Muestras más grandes pueden ser más lentas"
    )
    
    df_sample = df.sample(min(sample_size, len(df)))
    
    # Seleccionar dimensiones
    dimensions = ['magnitude', 'depth', 'sig']
    
    if 'nst' in df.columns:
        dimensions.append('nst')
    if 'dmin' in df.columns:
        dimensions.append('dmin')
    
    # Crear gráfico de coordenadas paralelas
    fig = px.parallel_coordinates(
        df_sample,
        color='tsunami',
        dimensions=dimensions,
        color_continuous_scale=[(0, '#4488ff'), (1, '#ff4444')],
        labels={col: col for col in dimensions},
        title='Análisis de Coordenadas Paralelas'
    )
    
    fig.update_layout(height=600)
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Cómo interpretar:**
    - Las líneas **rojas** representan eventos con tsunami
    - Las líneas **azules** representan eventos sin tsunami
    - Busca patrones donde las líneas rojas se agrupan en rangos específicos
    """)


# ============================================================================
# ANÁLISIS DE PARES
# ============================================================================

def render_pairwise_analysis(df):
    """Análisis de pares de variables."""
    
    st.subheader("🔄 Análisis de Relaciones entre Pares de Variables")
    
    # Seleccionar variables
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude_cols = ['Year', 'Month', 'tsunami', 'is_shallow', 'high_mag', 'oceanic_event']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    col1, col2 = st.columns(2)
    
    with col1:
        var1 = st.selectbox(
            "Variable 1:",
            numeric_cols,
            index=numeric_cols.index('magnitude') if 'magnitude' in numeric_cols else 0
        )
    
    with col2:
        var2 = st.selectbox(
            "Variable 2:",
            numeric_cols,
            index=numeric_cols.index('depth') if 'depth' in numeric_cols else 1
        )
    
    # Scatter plot
    fig1 = px.scatter(
        df,
        x=var1,
        y=var2,
        color='tsunami_label',
        size='sig' if 'sig' in df.columns else var1,
        hover_data=['magnitude', 'depth', 'Year'],
        color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
        title=f'{var1} vs {var2}',
        trendline='ols',
        opacity=0.6
    )
    
    fig1.update_layout(height=500)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Density contour
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = px.density_contour(
            df[df['tsunami'] == 0],
            x=var1,
            y=var2,
            title=f'Densidad: Sin Tsunami ({var1} vs {var2})',
            color_discrete_sequence=['#4488ff']
        )
        fig2.update_traces(contours_coloring='fill', contours_showlabels=True)
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        fig3 = px.density_contour(
            df[df['tsunami'] == 1],
            x=var1,
            y=var2,
            title=f'Densidad: Con Tsunami ({var1} vs {var2})',
            color_discrete_sequence=['#ff4444']
        )
        fig3.update_traces(contours_coloring='fill', contours_showlabels=True)
        fig3.update_layout(height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    # Matriz de correlación para variables seleccionadas
    st.markdown("#### 🔗 Correlaciones entre Variables Seleccionadas")
    
    selected_vars = st.multiselect(
        "Selecciona variables para matriz de correlación:",
        numeric_cols,
        default=numeric_cols[:5] if len(numeric_cols) >= 5 else numeric_cols
    )
    
    if selected_vars:
        corr_matrix = df[selected_vars].corr()
        
        fig4 = px.imshow(
            corr_matrix,
            text_auto='.2f',
            aspect='auto',
            color_continuous_scale='RdBu_r',
            zmin=-1,
            zmax=1,
            title='Matriz de Correlación'
        )
        
        fig4.update_layout(height=500)
        st.plotly_chart(fig4, use_container_width=True)
