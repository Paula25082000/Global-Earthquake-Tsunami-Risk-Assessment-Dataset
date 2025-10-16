"""
Página de Exploración de Datos
===============================

Análisis exploratorio: distribuciones, correlaciones y estadísticas descriptivas.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy import stats


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def render(df):
    """
    Renderiza la página de exploración de datos.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos (filtrado)
    """
    
    st.header("📊 Exploración de Datos")
    st.markdown("Análisis de distribuciones, correlaciones y estadísticas descriptivas.")
    st.markdown("---")
    
    # ===== TABS PRINCIPALES =====
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Distribuciones",
        "🔗 Correlaciones",
        "📊 Comparaciones",
        "📋 Estadísticas"
    ])
    
    # ===== TAB 1: DISTRIBUCIONES =====
    with tab1:
        render_distributions(df)
    
    # ===== TAB 2: CORRELACIONES =====
    with tab2:
        render_correlations(df)
    
    # ===== TAB 3: COMPARACIONES =====
    with tab3:
        render_comparisons(df)
    
    # ===== TAB 4: ESTADÍSTICAS =====
    with tab4:
        render_statistics(df)


# ============================================================================
# SECCIÓN: DISTRIBUCIONES
# ============================================================================

def render_distributions(df):
    """Renderiza análisis de distribuciones de variables."""
    
    st.subheader("📈 Distribuciones de Variables")
    
    # Seleccionar variables numéricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Excluir algunas columnas
    exclude_cols = ['Year', 'Month', 'tsunami', 'is_shallow', 'high_mag', 'oceanic_event']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    # Selector de variables
    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_vars = st.multiselect(
            "Selecciona variables para visualizar:",
            options=numeric_cols,
            default=numeric_cols[:4] if len(numeric_cols) >= 4 else numeric_cols
        )
    
    with col2:
        plot_type = st.radio(
            "Tipo de gráfico:",
            options=["Histograma", "Box Plot", "Violin Plot"]
        )
    
    if not selected_vars:
        st.warning("⚠️ Selecciona al menos una variable para visualizar.")
        return
    
    # Crear visualizaciones
    n_cols = 2
    n_rows = int(np.ceil(len(selected_vars) / n_cols))
    
    for i, var in enumerate(selected_vars):
        if i % n_cols == 0:
            cols = st.columns(n_cols)
        
        with cols[i % n_cols]:
            if plot_type == "Histograma":
                fig = px.histogram(
                    df,
                    x=var,
                    nbins=30,
                    title=f"Distribución de {var}",
                    marginal="box",
                    color_discrete_sequence=['#1f77b4']
                )
            
            elif plot_type == "Box Plot":
                fig = px.box(
                    df,
                    y=var,
                    title=f"Box Plot de {var}",
                    color_discrete_sequence=['#1f77b4']
                )
            
            else:  # Violin Plot
                fig = px.violin(
                    df,
                    y=var,
                    box=True,
                    title=f"Violin Plot de {var}",
                    color_discrete_sequence=['#1f77b4']
                )
            
            fig.update_layout(
                height=400,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Test de normalidad
            if len(df[var].dropna()) > 3:
                data_sample = df[var].dropna().sample(min(5000, len(df[var].dropna())))
                stat, p_value = stats.shapiro(data_sample)
                
                if p_value > 0.05:
                    st.success(f"✅ Probablemente normal (p={p_value:.4f})")
                else:
                    st.info(f"ℹ️ Probablemente no normal (p={p_value:.4f})")


# ============================================================================
# SECCIÓN: CORRELACIONES
# ============================================================================

def render_correlations(df):
    """Renderiza análisis de correlaciones."""
    
    st.subheader("🔗 Matriz de Correlaciones")
    
    # Opciones de correlación
    col1, col2 = st.columns(2)
    
    with col1:
        method = st.selectbox(
            "Método de correlación:",
            options=["spearman", "pearson", "kendall"],
            index=0,
            help="Spearman es recomendado para datos no normales"
        )
    
    with col2:
        include_tsunami = st.checkbox(
            "Incluir variable 'tsunami'",
            value=False,
            help="Incluir la variable objetivo en la matriz"
        )
    
    # Seleccionar columnas numéricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Excluir algunas columnas
    exclude_cols = ['Year', 'Month', 'is_shallow', 'high_mag', 'oceanic_event']
    if not include_tsunami:
        exclude_cols.append('tsunami')
    
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    # Calcular correlación
    corr_matrix = df[numeric_cols].corr(method=method)
    
    # Crear heatmap
    fig = px.imshow(
        corr_matrix,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        zmin=-1,
        zmax=1,
        title=f'Matriz de Correlación ({method.capitalize()})'
    )
    
    fig.update_layout(
        height=600,
        xaxis_title='',
        yaxis_title=''
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlaciones más fuertes
    st.markdown("#### 🔝 Top 10 Correlaciones Más Fuertes")
    
    # Extraer correlaciones únicas (sin duplicados ni diagonal)
    corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            corr_pairs.append({
                'Variable 1': corr_matrix.columns[i],
                'Variable 2': corr_matrix.columns[j],
                'Correlación': corr_matrix.iloc[i, j]
            })
    
    corr_df = pd.DataFrame(corr_pairs)
    corr_df['Correlación Abs'] = corr_df['Correlación'].abs()
    corr_df = corr_df.sort_values('Correlación Abs', ascending=False).head(10)
    
    # Formatear y mostrar
    display_df = corr_df[['Variable 1', 'Variable 2', 'Correlación']].copy()
    display_df['Correlación'] = display_df['Correlación'].round(3)
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================================
# SECCIÓN: COMPARACIONES
# ============================================================================

def render_comparisons(df):
    """Renderiza comparaciones entre grupos (tsunami vs no tsunami)."""
    
    st.subheader("📊 Comparaciones: Con Tsunami vs Sin Tsunami")
    
    # Seleccionar variable para comparar
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude_cols = ['Year', 'Month', 'tsunami', 'is_shallow', 'high_mag', 'oceanic_event']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    selected_var = st.selectbox(
        "Selecciona una variable para comparar:",
        options=numeric_cols,
        index=numeric_cols.index('magnitude') if 'magnitude' in numeric_cols else 0
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Box plot comparativo
        fig1 = px.box(
            df,
            x='tsunami_label',
            y=selected_var,
            color='tsunami_label',
            color_discrete_map={'Sin Tsunami': '#4488ff', 'Con Tsunami': '#ff4444'},
            title=f'Comparación de {selected_var}',
            labels={'tsunami_label': 'Tipo de Evento'}
        )
        
        fig1.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Histograma superpuesto
        fig2 = go.Figure()
        
        fig2.add_trace(go.Histogram(
            x=df[df['tsunami'] == 0][selected_var],
            name='Sin Tsunami',
            marker_color='#4488ff',
            opacity=0.7,
            nbinsx=30
        ))
        
        fig2.add_trace(go.Histogram(
            x=df[df['tsunami'] == 1][selected_var],
            name='Con Tsunami',
            marker_color='#ff4444',
            opacity=0.7,
            nbinsx=30
        ))
        
        fig2.update_layout(
            barmode='overlay',
            title=f'Distribución de {selected_var}',
            xaxis_title=selected_var,
            yaxis_title='Frecuencia',
            height=400
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Estadísticas comparativas
    st.markdown("#### 📋 Estadísticas Comparativas")
    
    stats_comparison = pd.DataFrame({
        'Métrica': ['Media', 'Mediana', 'Desv. Estándar', 'Mínimo', 'Máximo'],
        'Sin Tsunami': [
            df[df['tsunami'] == 0][selected_var].mean(),
            df[df['tsunami'] == 0][selected_var].median(),
            df[df['tsunami'] == 0][selected_var].std(),
            df[df['tsunami'] == 0][selected_var].min(),
            df[df['tsunami'] == 0][selected_var].max()
        ],
        'Con Tsunami': [
            df[df['tsunami'] == 1][selected_var].mean(),
            df[df['tsunami'] == 1][selected_var].median(),
            df[df['tsunami'] == 1][selected_var].std(),
            df[df['tsunami'] == 1][selected_var].min(),
            df[df['tsunami'] == 1][selected_var].max()
        ]
    })
    
    stats_comparison['Diferencia'] = stats_comparison['Con Tsunami'] - stats_comparison['Sin Tsunami']
    
    st.dataframe(
        stats_comparison.round(3),
        use_container_width=True,
        hide_index=True
    )
    
    # Test estadístico
    st.markdown("#### 🧪 Test de Significancia")
    
    group1 = df[df['tsunami'] == 0][selected_var].dropna()
    group2 = df[df['tsunami'] == 1][selected_var].dropna()
    
    if len(group1) > 0 and len(group2) > 0:
        # Mann-Whitney U test (no paramétrico)
        stat, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')
        
        if p_value < 0.05:
            st.success(
                f"✅ **Diferencia estadísticamente significativa** (p={p_value:.4e})\n\n"
                f"Los eventos con y sin tsunami tienen distribuciones diferentes de '{selected_var}'."
            )
        else:
            st.info(
                f"ℹ️ **No hay diferencia significativa** (p={p_value:.4f})\n\n"
                f"No se puede afirmar que las distribuciones sean diferentes."
            )


# ============================================================================
# SECCIÓN: ESTADÍSTICAS
# ============================================================================

def render_statistics(df):
    """Renderiza estadísticas descriptivas detalladas."""
    
    st.subheader("📋 Estadísticas Descriptivas Completas")
    
    # Estadísticas por grupo
    st.markdown("#### Por Tipo de Evento")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude_cols = ['Year', 'Month', 'tsunami', 'is_shallow', 'high_mag', 'oceanic_event']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    # Crear tabs para cada grupo
    tab1, tab2 = st.tabs(["🔵 Sin Tsunami", "🔴 Con Tsunami"])
    
    with tab1:
        st.dataframe(
            df[df['tsunami'] == 0][numeric_cols].describe().T,
            use_container_width=True
        )
    
    with tab2:
        st.dataframe(
            df[df['tsunami'] == 1][numeric_cols].describe().T,
            use_container_width=True
        )
    
    st.markdown("---")
    
    # Resumen general
    st.markdown("#### 📊 Resumen General del Dataset Filtrado")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Eventos", f"{len(df):,}")
    
    with col2:
        st.metric("Con Tsunami", f"{df['tsunami'].sum():,}")
    
    with col3:
        st.metric("Sin Tsunami", f"{(df['tsunami'] == 0).sum():,}")
    
    with col4:
        tsunami_pct = (df['tsunami'].sum() / len(df) * 100) if len(df) > 0 else 0
        st.metric("% Tsunamis", f"{tsunami_pct:.1f}%")
