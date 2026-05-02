@echo off
title SOLPRO AI - Estacion Multi-Agente
color 0B
cls
echo ============================================================
echo         SOLPRO AI - Estacion de Trabajo Multi-Agente
echo ============================================================
echo.
echo  Iniciando servidor...
echo  La interfaz se abrira en tu navegador en un momento.
echo.
echo  Si no abre automaticamente, ve a:
echo  http://localhost:7432
echo.
echo  IMPORTANTE: Usa Chrome o Edge para mejor experiencia.
echo  Si abre en Antigravity, copia la URL a Chrome/Edge.
echo ============================================================
echo.

REM Intentar abrir con Chrome primero, luego Edge, luego default
start "" "http://localhost:7432"

python asistente_gui.py
echo.
pause
