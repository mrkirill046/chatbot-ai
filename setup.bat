@echo off
chcp 65001 >nul

echo Только для Windows
echo Только для Windows
echo Только для Windows

set "MYPATH=%~dp0bin"

if not exist "%MYPATH%" (
    echo Ошибка: Папка bin не найдена: %MYPATH%
    pause
    exit /b
)

for /f "tokens=*" %%A in ('powershell -command "[System.Environment]::GetEnvironmentVariable('Path', 'User')"') do set "CURRENTPATH=%%A"
echo %CURRENTPATH% | find /i "%MYPATH%" >nul || (
    reg add "HKCU\Environment" /v Path /d "%MYPATH%;%CURRENTPATH%" /f
)

echo Путь добавлен. Перезапустите компьютер
pause
