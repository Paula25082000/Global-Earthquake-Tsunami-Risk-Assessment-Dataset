"""
Styles Module
=============

Módulo para aplicar estilos CSS personalizados a la aplicación de Streamlit.
Define colores, tipografías y componentes visuales.
"""

import streamlit as st


# ============================================================================
# CONSTANTES DE ESTILO
# ============================================================================

# Paleta de colores principal
COLORS = {
    'primary': '#1f77b4',      # Azul principal
    'secondary': '#ff7f0e',    # Naranja
    'danger': '#d62728',       # Rojo (tsunamis)
    'success': '#2ca02c',      # Verde
    'info': '#17becf',         # Cyan
    'warning': '#ff9f1c',      # Amarillo/naranja
    'dark': '#2c2c2c',         # Gris oscuro
    'light': '#f0f0f0',        # Gris claro
    'tsunami': '#ff4444',      # Rojo intenso para tsunamis
    'no_tsunami': '#4488ff',   # Azul para no tsunamis
}


# ============================================================================
# FUNCIÓN PRINCIPAL DE ESTILOS
# ============================================================================

def apply_custom_css():
    """
    Aplica estilos CSS personalizados a la aplicación de Streamlit.
    Mejora la apariencia visual y la experiencia de usuario.
    """
    
    css = f"""
    <style>
    
    /* ===== ESTILOS GENERALES ===== */
    
    /* Fuentes y tipografía */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* Fondo de la aplicación */
    .stApp {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }}
    
    /* Contenedor principal */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }}
    
    /* ===== TÍTULOS Y ENCABEZADOS ===== */
    
    h1 {{
        color: {COLORS['primary']};
        font-weight: 700;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 3px solid {COLORS['primary']};
    }}
    
    h2 {{
        color: {COLORS['dark']};
        font-weight: 600;
        margin-top: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid {COLORS['light']};
    }}
    
    h3 {{
        color: {COLORS['secondary']};
        font-weight: 600;
    }}
    
    /* ===== SIDEBAR ===== */
    
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }}
    
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stMultiSelect label {{
        color: white !important;
        font-weight: 600;
    }}
    
    /* ===== MÉTRICAS ===== */
    
    [data-testid="stMetricValue"] {{
        font-size: 2rem;
        font-weight: 700;
        color: {COLORS['primary']};
    }}
    
    [data-testid="stMetricLabel"] {{
        font-size: 1rem;
        color: {COLORS['dark']};
        font-weight: 600;
    }}
    
    /* ===== BOTONES ===== */
    
    .stButton>button {{
        background: linear-gradient(90deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }}
    
    /* ===== CAJAS DE INFORMACIÓN ===== */
    
    .stAlert {{
        border-radius: 8px;
        border-left: 4px solid;
        padding: 1rem;
    }}
    
    /* Info box */
    .stInfo {{
        background-color: rgba(23, 190, 207, 0.1);
        border-left-color: {COLORS['info']};
    }}
    
    /* Warning box */
    .stWarning {{
        background-color: rgba(255, 159, 28, 0.1);
        border-left-color: {COLORS['warning']};
    }}
    
    /* Success box */
    .stSuccess {{
        background-color: rgba(44, 160, 44, 0.1);
        border-left-color: {COLORS['success']};
    }}
    
    /* Error box */
    .stError {{
        background-color: rgba(214, 39, 40, 0.1);
        border-left-color: {COLORS['danger']};
    }}
    
    /* ===== EXPANDERS ===== */
    
    .streamlit-expanderHeader {{
        background-color: {COLORS['light']};
        border-radius: 8px;
        font-weight: 600;
        color: {COLORS['dark']};
    }}
    
    /* ===== DATAFRAMES ===== */
    
    [data-testid="stDataFrame"] {{
        border-radius: 8px;
        overflow: hidden;
    }}
    
    /* ===== TABS ===== */
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: {COLORS['light']};
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(90deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        color: white !important;
    }}
    
    /* ===== CUSTOM CLASSES ===== */
    
    /* Card container */
    .custom-card {{
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }}
    
    /* Highlight box */
    .highlight-box {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }}
    
    /* Risk indicator */
    .risk-high {{
        color: {COLORS['danger']};
        font-weight: 700;
        font-size: 1.2rem;
    }}
    
    .risk-medium {{
        color: {COLORS['warning']};
        font-weight: 700;
        font-size: 1.2rem;
    }}
    
    .risk-low {{
        color: {COLORS['success']};
        font-weight: 700;
        font-size: 1.2rem;
    }}
    
    /* ===== ANIMACIONES ===== */
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .animate-fade-in {{
        animation: fadeIn 0.6s ease-out;
    }}
    
    /* ===== RESPONSIVE ===== */
    
    @media (max-width: 768px) {{
        .main .block-container {{
            padding: 1rem;
        }}
        
        h1 {{
            font-size: 1.8rem;
        }}
    }}
    
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)


# ============================================================================
# COMPONENTES DE ESTILO REUTILIZABLES
# ============================================================================

def create_card(content, title=None):
    """
    Crea una tarjeta estilizada con contenido.
    
    Args:
        content (str): Contenido HTML de la tarjeta
        title (str, optional): Título de la tarjeta
    """
    title_html = f"<h3>{title}</h3>" if title else ""
    
    card_html = f"""
    <div class="custom-card animate-fade-in">
        {title_html}
        {content}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def create_highlight_box(content):
    """
    Crea una caja destacada con gradiente.
    
    Args:
        content (str): Contenido de la caja
    """
    box_html = f"""
    <div class="highlight-box animate-fade-in">
        {content}
    </div>
    """
    
    st.markdown(box_html, unsafe_allow_html=True)


def get_risk_indicator(risk_level):
    """
    Retorna un indicador visual de riesgo.
    
    Args:
        risk_level (str): 'alto', 'medio', o 'bajo'
        
    Returns:
        str: HTML del indicador de riesgo
    """
    icons = {
        'alto': '🔴',
        'medio': '🟡',
        'bajo': '🟢'
    }
    
    classes = {
        'alto': 'risk-high',
        'medio': 'risk-medium',
        'bajo': 'risk-low'
    }
    
    labels = {
        'alto': 'RIESGO ALTO',
        'medio': 'RIESGO MEDIO',
        'bajo': 'RIESGO BAJO'
    }
    
    icon = icons.get(risk_level.lower(), '⚪')
    css_class = classes.get(risk_level.lower(), 'risk-medium')
    label = labels.get(risk_level.lower(), 'RIESGO DESCONOCIDO')
    
    return f'<span class="{css_class}">{icon} {label}</span>'
