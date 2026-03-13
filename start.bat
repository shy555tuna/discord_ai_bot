@echo off
setlocal enabledelayedexpansion
title ShyNet — Discord AI Bot Manager

echo.
echo ╔══════════════════════════════════════╗
echo ║        ShyNet — AI Discord Bot     ║
echo ╚══════════════════════════════════════╝
echo.

set PYTHON=
for %%p in (python3.12 python3.11 python3 python) do (
    where %%p >nul 2>&1
    if not errorlevel 1 (
        for /f "tokens=*" %%v in ('%%p -c "import sys; print(sys.version_info.major)" 2^>nul') do set MAJOR=%%v
        for /f "tokens=*" %%v in ('%%p -c "import sys; print(sys.version_info.minor)" 2^>nul') do set MINOR=%%v
        if !MAJOR! GEQ 3 if !MINOR! GEQ 11 (
            set PYTHON=%%p
            goto :found_python
        )
    )
)

echo ✗ Python 3.11+ not found.
echo.
echo   Download from: https://www.python.org/downloads/
echo   Make sure to check "Add Python to PATH" during install.
echo.
pause
exit /b 1

:found_python
echo ✓ Found Python !MAJOR!.!MINOR!

if not exist ".venv\" (
    echo.
    echo → Creating virtual environment...
    !PYTHON! -m venv .venv
    echo ✓ Virtual environment created
)

call .venv\Scripts\activate.bat
echo ✓ Virtual environment activated

echo.
echo → Installing dependencies...
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo ✓ Dependencies installed

start "" /b cmd /c "timeout /t 2 >nul && start http://localhost:5000"

echo.
echo ✓ Starting ShyNet at http://localhost:5000
echo   Press Ctrl+C to stop
echo.
python app.py

pause
