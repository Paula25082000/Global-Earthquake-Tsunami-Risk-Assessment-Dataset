# EDA Global Earthquake & Tsunami — Guía Narrativa y Técnica

Autor: Demetrio • Fecha: 2025-10-16

---

## 1) Resumen ejecutivo (para no técnicos)

Este estudio explora miles de terremotos recientes para responder una pregunta clave: ¿qué condiciones hacen más probable que un terremoto genere un tsunami? Analizamos magnitud, profundidad, intensidad, localización y calidad de monitoreo. Hallamos que:

- Los tsunamis se asocian a terremotos de mayor magnitud y poco profundos.
- Muchos eventos con tsunami ocurren en mar abierto, lejos de estaciones sismológicas.
- No hay estacionalidad clara; el riesgo se distribuye durante todo el año.
- El “puntaje de significancia” del evento refleja la magnitud y el impacto, pero es redundante para el modelado.

Esto nos permite proponer un “perfil de riesgo” práctico para alertas tempranas y sentar las bases de un panel de inteligencia.

---

## 2) Objetivo del análisis y preguntas guía

- Identificar señales tempranas de eventos tsunamigénicos a partir de variables sísmicas y de contexto.
- Entender relaciones entre magnitud, profundidad, intensidad (MMI/CDI), localización y monitoreo (nst, dmin, gap).
- Traducir hallazgos en componentes de un futuro dashboard operativo.

---

## 3) Datos y diccionario mínimo

Fuente: `data/earthquake_data_tsunami.csv` (2001–2022).

- magnitude: intensidad del terremoto (escala Richter).
- depth (km): profundidad del hipocentro.
- mmi/cdi: intensidades instrumental y percibida.
- sig: “significance score” del evento.
- nst: número de estaciones que registraron el evento.
- dmin (°): distancia angular mínima a una estación.
- gap (°): brecha azimutal entre estaciones.
- latitude/longitude: localización del epicentro.
- Year/Month: marca temporal del evento.
- tsunami: 1 si generó tsunami, 0 en caso contrario.

---

## 4) Metodología

- Análisis exploratorio con Python (pandas, seaborn, plotly).
- Distribuciones por variable y prueba de normalidad (Shapiro–Wilk).
- Correlaciones de Spearman (no paramétricas) entre variables numéricas.
- Exploración geoespacial y temporal con mapas interactivos y gráficas animadas.
- Análisis multivariable (3D scatter y coordenadas paralelas).

---

## 5) Hallazgos por bloque

### 5.1 Distribuciones y normalidad

- La mayoría de variables no siguen distribución normal (Shapiro < 0.05), justificando Spearman.
- Magnitude se concentra entre 6.5 y 7.5; profundidad presenta colas largas (eventos muy profundos).
- mmi/cdi muestran asimetría: impactos intensos son menos frecuentes pero muy informativos.

### 5.2 Correlaciones (Spearman, sin incluir la etiqueta tsunami en la matriz)

| Relación | Señal | Interpretación | Acción práctica |
|---|---|---|---|
| magnitude ↔ sig | alta positiva | sig recoge en gran parte la magnitud | Evitar usar ambas; priorizar magnitude |
| nst ↔ dmin | alta negativa | más lejos de estaciones → menos estaciones reportando | Crear indicador de “calidad/entorno de monitoreo” |
| Year ↔ dmin | positiva | más reciente ≈ mayor cobertura remota | Cuidar sesgos temporales |
| cdi ↔ mmi | moderada positiva | dos caras de la intensidad | Mantener al menos una |
| gap ↔ mmi | débil negativa | mayor brecha, menor MMI observado | Considerar en el índice de monitoreo |

Notas con la etiqueta tsunami (del análisis previo):
- magnitude y sig correlacionan positivamente con tsunami.
- depth correlación negativa: eventos más superficiales son más tsunamigénicos.
- dmin (+) y nst (–) con tsunami: muchos tsunamis ocurren lejos de estaciones (eventos oceánicos).

### 5.3 Geoespacial: ¿Dónde ocurren los eventos críticos?

- Concentración en el Cinturón de Fuego del Pacífico.
- Eventos con mayor magnitude y sig se distribuyen en bordes de placas, cerca de fosas oceánicas.
- Los tsunamis se agrupan en litorales expuestos y mar abierto, reforzando el patrón “dmin alto + nst bajo”.

### 5.4 Temporal: ¿Cuándo ocurren?

- No se observa estacionalidad: los tsunamis aparecen a lo largo del año.
- Variabilidad anual más asociada a actividad tectónica puntual que a tendencias de largo plazo.

### 5.5 Multivariable: combinación de factores

- En 3D (magnitude–depth–sig), los casos con tsunami tienden a: magnitudes altas, profundidades bajas y alta sig.
- En coordenadas paralelas, el “camino típico” de riesgo combina: magnitude alta, depth baja, sig alta, nst bajo, dmin alto.

---

## 6) Implicaciones operativas y reglas de “alerta temprana”

Reglas heurísticas iniciales (para priorización operativa, no deterministas):

- Magnitud ≥ 7.0 y profundidad < 50 km → Alto riesgo tsunamigénico.
- Magnitud ≥ 7.5 o sig muy alto → Revisar inmediatamente boletas de alerta.
- dmin > 5° y nst bajo → Probable evento oceánico; elevar vigilancia costera.
- MMI ≥ 5 o CDI ≥ 4 cerca de costa → Riesgo de impactos locales severos.

---

## 7) Recomendaciones para modelado predictivo

- Variables prioritarias: magnitude, depth, mmi/cdi (elegir una), nst, dmin, gap.
- Evitar multicolinealidad: considerar descartar `sig` (redundante con magnitude).
- Engineering sugerido:
  - is_shallow = depth < 50 (binaria)
  - oceanic_event = dmin > 5 (binaria)
  - high_mag = magnitude ≥ 7.0 (binaria)
  - monitoring_quality = f(nst, gap, dmin)
- Validación temporal (train/test por tiempo) para evitar fuga de información.

---

## 8) Blueprint de Dashboard de Inteligencia

Páginas/sheets propuestas y KPIs:

1. Situación Global (Mapa)
   - Mapa mundial con puntos por evento, color por magnitude y símbolo por tsunami.
   - Filtros: año, rango de magnitud, profundidad, región.
   - KPI: eventos totales, % con tsunami, magnitud máxima.

2. Riesgo Inmediato (Alerta)
   - Tarjetas de eventos recientes con reglas heurísticas aplicadas.
   - Indicador de riesgo (bajo/medio/alto) por evento.

3. Patrones y Tendencias
   - Series por año/mes: frecuencia de tsunamis, magnitud media, profundidad media.
   - Histograma comparativo: magnitud con vs sin tsunami.

4. Calidad de Monitoreo
   - Mapa/calor por `nst`, `dmin`, `gap`.
   - Índice de cobertura y áreas ciegas.

5. Analítica Multivariable
   - Scatter 3D magnitude–depth–sig (o PCA) con color por tsunami.
   - Coordenadas paralelas para perfiles de riesgo.

---

## 9) Limitaciones y consideraciones

- `sig` depende de otras variables (no es independiente), riesgo de “doble conteo”.
- Sesgos de observación: variaciones en redes de estaciones por año/región.
- Coordenadas (lat/lon) sin contexto tectónico: enriquecer con capas (fosas, placas, distancia a costa).
- Etiqueta `tsunami` no distingue tamaño/alcance; para impacto se requiere intensidad del tsunami.

---

## 10) Próximos pasos

- Incorporar metadatos tectónicos (zonas de subducción, distancia a trinchera oceánica).
- Calibrar umbrales de reglas heurísticas con validaciones históricas.
- Entrenar modelos (árboles/gradient boosting) con validación por tiempo; explicar con SHAP.
- Diseñar PoC del dashboard (en Plotly Dash o Power BI) con las páginas propuestas.

---

## 11) Glosario rápido

- MMI/CDI: medidas de intensidad (instrumental vs percibida).
- nst/dmin/gap: métricas de cobertura y geometría de estaciones.
- Spearman: correlación no paramétrica (variables no normales o monotónicas).

---

## 12) Reproducibilidad mínima

- Notebook fuente: `notebooks/EDA_ Demetrio.ipynb`.
- Dataset: `data/earthquake_data_tsunami.csv`.
- Librerías clave: pandas, numpy, seaborn, plotly, scipy.

