@echo off
chcp 65001 >nul

setlocal
cd /d "%~dp0"

where python >nul 2>nul || (
    echo Python не найден. Пожалуйста, установите его.
    exit /b
)

cd /d "%~dp0.."

python main.py %*
