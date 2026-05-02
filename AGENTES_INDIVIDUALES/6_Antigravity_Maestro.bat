@echo off
title Cerebro 6 - Antigravity (Master AI Assistant)
color 0D
cls
echo ============================================================
echo      ANTIGRAVITY - ORQUESTADOR MAESTRO (GOOGLE DEEPMIND)
echo ============================================================
echo.
echo  Estado del Sistema: VINCULADO A GITHUB
echo  Repositorio: https://github.com/abericua/AGENTES-IA
echo.
echo  Rol: Orquestacion, Gestion de Codigo y Sincronizacion Git.
echo.
echo ============================================================
echo.
echo  Presiona cualquier tecla para abrir el repositorio en GitHub...
pause > nul
start https://github.com/abericua/AGENTES-IA
echo.
echo  Sincronizando cambios locales...
& "C:\Program Files\Git\cmd\git.exe" pull origin master
echo.
echo  Listo. Sistema Antigravity habilitado.
pause
