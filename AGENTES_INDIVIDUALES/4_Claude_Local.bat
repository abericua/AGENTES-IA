@echo off
title Cerebro 4 - Claude Code (Local)
set ANTHROPIC_BASE_URL=http://localhost:11434
set ANTHROPIC_AUTH_TOKEN=ollama
echo Inciando Claude Code vinculado a Ollama...
claude --model gemma4:26b
pause
