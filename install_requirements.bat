@echo off
REM This script installs all Python packages listed in requirements.txt

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Installation failed!
    exit /b %errorlevel%
)
echo Installation completed successfully. 