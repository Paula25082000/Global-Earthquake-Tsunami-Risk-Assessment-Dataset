"""
Guía de Desarrollo del Dashboard
=================================

Este documento proporciona información para desarrolladores que deseen
extender o modificar el dashboard.

## Arquitectura

### Estructura Modular

La aplicación está organizada en módulos independientes:

- **main.py**: Punto de entrada y orquestación
- **components/**: Componentes reutilizables (sidebar, filtros)
- **pages/**: Páginas individuales del dashboard
- **utils/**: Utilidades compartidas (carga de datos, estilos)

### Flujo de Datos

1. `main.py` carga los datos usando `utils/data_loader.py`
2. Los datos se pasan al sidebar (`components/sidebar.py`)
3. El sidebar aplica filtros (`components/filters.py`)
4. Los datos filtrados se pasan a la página seleccionada
5. Cada página renderiza visualizaciones específicas

## Añadir una Nueva Página

### Paso 1: Crear el Archivo

Crear un nuevo archivo en `pages/`, por ejemplo `nueva_pagina.py`:

```python
import streamlit as st

def render(df):
    st.header("Nueva Página")
    # Tu código aquí
```

### Paso 2: Importar en main.py

En `main.py`, añadir la importación:

```python
from pages import nueva_pagina
```

### Paso 3: Añadir al Menú

En `components/sidebar.py`, añadir la opción al menú:

```python
pages = [
    "🏠 Inicio",
    # ... otras páginas
    "🆕 Nueva Página"
]
```

### Paso 4: Añadir al Router

En `main.py`, añadir el caso al router:

```python
elif page_selected == "🆕 Nueva Página":
    nueva_pagina.render(df_filtered)
```

## Añadir un Nuevo Filtro

En `components/filters.py`, añadir el control:

```python
def apply_filters(df):
    # ... filtros existentes
    
    # Nuevo filtro
    nuevo_criterio = st.selectbox("Nuevo Criterio:", opciones)
    df_filtered = df_filtered[df_filtered['columna'] == nuevo_criterio]
    
    return df_filtered
```

## Estilos Personalizados

Los estilos CSS se gestionan en `utils/styles.py`. Para añadir nuevos estilos:

```python
def apply_custom_css():
    css = f\"\"\"
    <style>
    /* Tus estilos aquí */
    .mi-clase {{
        color: red;
    }}
    </style>
    \"\"\"
    st.markdown(css, unsafe_allow_html=True)
```

## Visualizaciones

### Plotly Express (Recomendado)

Para gráficos simples, usar Plotly Express:

```python
import plotly.express as px

fig = px.scatter(df, x='magnitude', y='depth')
st.plotly_chart(fig, use_container_width=True)
```

### Plotly Graph Objects (Avanzado)

Para gráficos personalizados:

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y))
st.plotly_chart(fig, use_container_width=True)
```

## Caché de Datos

Para optimizar el rendimiento, usar el decorador de Streamlit:

```python
@st.cache_data
def funcion_costosa(df):
    # Procesamiento pesado
    return resultado
```

## Manejo de Errores

Siempre validar los datos antes de procesarlos:

```python
if df.empty:
    st.warning("No hay datos disponibles")
    return

if 'columna_requerida' not in df.columns:
    st.error("Columna faltante en el dataset")
    return
```

## Testing

Para probar cambios localmente:

```bash
cd app
streamlit run main.py
```

## Deployment

### Streamlit Cloud

1. Subir el código a GitHub
2. Conectar repositorio en streamlit.io
3. Configurar la ruta: `app/main.py`

### Docker (Alternativo)

Crear un `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app/main.py"]
```

## Mejores Prácticas

1. **Documentación**: Comentar código complejo
2. **Modularidad**: Funciones pequeñas y reutilizables
3. **Performance**: Usar caché cuando sea posible
4. **Validación**: Siempre validar inputs del usuario
5. **Responsive**: Usar `use_container_width=True` en gráficos
6. **Accesibilidad**: Colores con buen contraste, textos descriptivos

## Solución de Problemas

### Error: Module not found

```bash
pip install -r requirements.txt
```

### Error: File not found

Verificar que estás en el directorio correcto:

```bash
cd app
streamlit run main.py
```

### Gráficos no se muestran

Verificar que Plotly está instalado:

```bash
pip install plotly
```

## Recursos Adicionales

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

**¡Feliz desarrollo! 🚀**
