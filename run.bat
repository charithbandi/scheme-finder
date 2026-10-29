@echo off
title Scheme Finder - Automated Welfare Matching Engine
echo =========================================================================
echo   SCHEME FINDER: Automated Welfare & Scholarship Eligibility Engine
echo   Minor Project-I - Batch 1358
echo   Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Tech
echo =========================================================================
echo.

cd /d "%~dp0"

echo [1/2] Checking Python Virtual Environment...
if exist "..\backend\venv\Scripts\python.exe" (
    set "PYTHON_EXE=..\backend\venv\Scripts\python.exe"
) else (
    set "PYTHON_EXE=python"
)

echo [2/2] Starting Flask Application Server at http://127.0.0.1:5000 ...
echo.
%PYTHON_EXE% app.py

pause
