# Script de inicio rápido para Windows PowerShell
# Ejecutar con: .\run.ps1

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Panel de Inteligencia: Earthquake & Tsunami   " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "Verificando instalación de Python..." -ForegroundColor Yellow
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonVersion = python --version
    Write-Host "✓ Python encontrado: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python no encontrado. Por favor instala Python 3.8+" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Verificar/Instalar dependencias
Write-Host "Verificando dependencias..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependencias desde requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Dependencias instaladas correctamente" -ForegroundColor Green
    } else {
        Write-Host "✗ Error al instalar dependencias" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✗ Archivo requirements.txt no encontrado" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Verificar datos
Write-Host "Verificando datos..." -ForegroundColor Yellow
$dataPath = "..\data\earthquake_data_tsunami.csv"
if (Test-Path $dataPath) {
    Write-Host "✓ Dataset encontrado" -ForegroundColor Green
} else {
    Write-Host "⚠ Dataset no encontrado en $dataPath" -ForegroundColor Yellow
    Write-Host "  La aplicación podría no funcionar correctamente" -ForegroundColor Yellow
}

Write-Host ""

# Iniciar aplicación
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Iniciando aplicación Streamlit...              " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "La aplicación se abrirá en tu navegador." -ForegroundColor Yellow
Write-Host "Presiona Ctrl+C para detener el servidor." -ForegroundColor Yellow
Write-Host ""

streamlit run main.py
