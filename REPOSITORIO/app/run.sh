#!/bin/bash
# Script de inicio rápido para Linux/Mac
# Ejecutar con: ./run.sh

echo "=================================================="
echo "  Panel de Inteligencia: Earthquake & Tsunami   "
echo "=================================================="
echo ""

# Verificar Python
echo "Verificando instalación de Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Python encontrado: $PYTHON_VERSION"
else
    echo "✗ Python no encontrado. Por favor instala Python 3.8+"
    exit 1
fi

echo ""

# Verificar/Instalar dependencias
echo "Verificando dependencias..."
if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias desde requirements.txt..."
    python3 -m pip install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        echo "✓ Dependencias instaladas correctamente"
    else
        echo "✗ Error al instalar dependencias"
        exit 1
    fi
else
    echo "✗ Archivo requirements.txt no encontrado"
    exit 1
fi

echo ""

# Verificar datos
echo "Verificando datos..."
DATA_PATH="../data/earthquake_data_tsunami.csv"
if [ -f "$DATA_PATH" ]; then
    echo "✓ Dataset encontrado"
else
    echo "⚠ Dataset no encontrado en $DATA_PATH"
    echo "  La aplicación podría no funcionar correctamente"
fi

echo ""

# Iniciar aplicación
echo "=================================================="
echo "  Iniciando aplicación Streamlit...              "
echo "=================================================="
echo ""
echo "La aplicación se abrirá en tu navegador."
echo "Presiona Ctrl+C para detener el servidor."
echo ""

streamlit run main.py
