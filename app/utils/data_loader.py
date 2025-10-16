"""
Data Loader
===========

Módulo para cargar y preparar los datos del dataset de terremotos.
Incluye funciones de carga, validación y transformación de datos.
"""

import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path


# ============================================================================
# CONSTANTES
# ============================================================================

# Ruta relativa al archivo CSV desde la carpeta app
DATA_PATH = Path(__file__).parent.parent.parent / "data" / "earthquake_data_tsunami.csv"


# ============================================================================
# FUNCIÓN DE CARGA DE DATOS
# ============================================================================

@st.cache_data
def load_data():
    """
    Carga el dataset de terremotos desde el archivo CSV.
    Utiliza caché de Streamlit para optimizar el rendimiento.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de terremotos, o None si hay error
    """
    try:
        # Cargar el CSV
        df = pd.read_csv(DATA_PATH)
        
        # Validar columnas requeridas
        required_columns = [
            'magnitude', 'depth', 'latitude', 'longitude', 
            'tsunami', 'Year', 'Month', 'sig'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"Columnas faltantes en el dataset: {missing_columns}")
            return None
        
        # Transformaciones básicas
        df = prepare_data(df)
        
        return df
    
    except FileNotFoundError:
        st.error(f"❌ No se encontró el archivo: {DATA_PATH}")
        return None
    
    except Exception as e:
        st.error(f"❌ Error al cargar los datos: {str(e)}")
        return None


# ============================================================================
# PREPARACIÓN DE DATOS
# ============================================================================

def prepare_data(df):
    """
    Prepara y transforma el DataFrame para su uso en la aplicación.
    Añade columnas calculadas y limpia datos.
    
    Args:
        df (pd.DataFrame): DataFrame original
        
    Returns:
        pd.DataFrame: DataFrame preparado
    """
    # Crear copia para evitar modificar el original
    df = df.copy()
    
    # Crear columnas de fecha
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))
    
    # Crear columnas binarias de riesgo (según EDA.md)
    df['is_shallow'] = (df['depth'] < 50).astype(int)
    df['high_mag'] = (df['magnitude'] >= 7.0).astype(int)
    df['oceanic_event'] = (df['dmin'] > 5).astype(int) if 'dmin' in df.columns else 0
    
    # Crear etiquetas para tsunami
    df['tsunami_label'] = df['tsunami'].map({0: 'Sin Tsunami', 1: 'Con Tsunami'})
    
    # Crear categorías de magnitud
    df['magnitude_category'] = pd.cut(
        df['magnitude'],
        bins=[0, 6.5, 7.0, 7.5, 10],
        labels=['< 6.5', '6.5-7.0', '7.0-7.5', '> 7.5']
    )
    
    # Crear categorías de profundidad
    df['depth_category'] = pd.cut(
        df['depth'],
        bins=[0, 50, 150, 300, 700],
        labels=['Superficial (0-50km)', 'Intermedia (50-150km)', 
                'Profunda (150-300km)', 'Muy Profunda (>300km)']
    )
    
    # Calcular índice de calidad de monitoreo (si las columnas existen)
    if all(col in df.columns for col in ['nst', 'gap', 'dmin']):
        # Normalizar cada componente (0-1)
        df['nst_norm'] = (df['nst'] - df['nst'].min()) / (df['nst'].max() - df['nst'].min())
        df['gap_norm'] = 1 - ((df['gap'] - df['gap'].min()) / (df['gap'].max() - df['gap'].min()))
        df['dmin_norm'] = 1 - ((df['dmin'] - df['dmin'].min()) / (df['dmin'].max() - df['dmin'].min()))
        
        # Índice combinado (promedio ponderado)
        df['monitoring_quality'] = (
            0.4 * df['nst_norm'] + 
            0.3 * df['gap_norm'] + 
            0.3 * df['dmin_norm']
        )
    else:
        df['monitoring_quality'] = 0.5  # Valor neutral si no hay datos
    
    # Calcular nivel de impacto (si existe CDI)
    if 'cdi' in df.columns:
        df['impact_level'] = df['cdi'].fillna(0)
    else:
        df['impact_level'] = 0
    
    # Ordenar por fecha descendente
    df = df.sort_values('Date', ascending=False)
    
    return df


# ============================================================================
# INFORMACIÓN DEL DATASET
# ============================================================================

def get_data_info(df):
    """
    Extrae información resumida del dataset.
    
    Args:
        df (pd.DataFrame): DataFrame de terremotos
        
    Returns:
        dict: Diccionario con métricas del dataset
    """
    info = {
        'total_events': len(df),
        'tsunami_events': df['tsunami'].sum(),
        'tsunami_percentage': (df['tsunami'].sum() / len(df)) * 100,
        'years_span': f"{df['Year'].min()}-{df['Year'].max()}",
        'magnitude_range': f"{df['magnitude'].min():.1f} - {df['magnitude'].max():.1f}",
        'depth_range': f"{df['depth'].min():.1f} - {df['depth'].max():.1f} km",
    }
    
    return info


# ============================================================================
# DICCIONARIO DE VARIABLES
# ============================================================================

def get_variable_descriptions():
    """
    Retorna un diccionario con descripciones de las variables del dataset.
    
    Returns:
        dict: Diccionario con nombre de variable como clave y descripción como valor
    """
    descriptions = {
        'magnitude': 'Magnitud del terremoto (escala Richter)',
        'depth': 'Profundidad del hipocentro (km)',
        'latitude': 'Latitud del epicentro',
        'longitude': 'Longitud del epicentro',
        'tsunami': 'Indicador binario (1 = generó tsunami, 0 = no)',
        'sig': 'Puntaje de significancia del evento',
        'nst': 'Número de estaciones sismológicas que registraron el evento',
        'dmin': 'Distancia angular mínima a una estación (grados)',
        'gap': 'Brecha azimutal entre estaciones (grados)',
        'mmi': 'Intensidad Mercalli Modificada (instrumental)',
        'cdi': 'Intensidad Mercalli percibida por la comunidad',
        'Year': 'Año del evento',
        'Month': 'Mes del evento',
        'is_shallow': 'Evento superficial (profundidad < 50km)',
        'high_mag': 'Magnitud alta (≥ 7.0)',
        'oceanic_event': 'Evento oceánico (dmin > 5°)',
        'monitoring_quality': 'Índice de calidad de monitoreo (0-1)',
        'impact_level': 'Nivel de impacto en comunidades',
    }
    
    return descriptions
