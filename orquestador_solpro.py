"""
orquestador_solpro.py - Asistente de Desarrollo Continuo Autónomo
================================================================
Pipeline de 3 Cerebros con interacción continua y archivos dinámicos.

Roles:
1. Generación: llama3:latest (Modo Rápido)
2. Revisión: llama3:latest
3. Pulido: qwen3.5:0.8b
"""

import urllib.request
import json
import re
import sys
import io
import os

# Configuración de salida para evitar errores de codificación en Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# --- CONFIGURACIÓN GLOBAL (MODO ALTA VELOCIDAD) ---
MODELO_GENERADOR = "llama3:latest"
MODELO_REVISOR   = "llama3:latest"
MODELO_PULIDOR   = "qwen3.5:0.8b"
URL_OLLAMA       = "http://127.0.0.1:11434/api/generate"
TIMEOUT_GLOBAL   = 600  # 10 minutos para permitir swap de modelos pesados

def llamar_ollama(modelo, prompt, etiqueta):
    """Realiza la petición a Ollama con timeout extendido."""
    print(f"\n[CEREBRO: {etiqueta}] Invocando {modelo}...")
    
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        req = urllib.request.Request(
            URL_OLLAMA, 
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        with urllib.request.urlopen(req, timeout=TIMEOUT_GLOBAL) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("response", "").strip()
            
    except Exception as e:
        print(f"!!! [FALLO] Error en {etiqueta}: {e}")
        return None

def extraer_codigo(texto):
    """Limpia el código de etiquetas markdown."""
    patron = r"```(?:python)?\s*(.*?)\s*```"
    bloque = re.search(patron, texto, re.DOTALL)
    if bloque:
        return bloque.group(1).strip()
    return texto.strip()

def guardar_archivo(nombre, contenido, fase):
    """Guarda el código limpio en un archivo .py."""
    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"--- [OK] Guardado {fase} en: {nombre}")
    except Exception as e:
        print(f"!!! [ERROR] No se pudo guardar {nombre}: {e}")

def ejecutar_pipeline(tarea_usuario, nombre_archivo):
    """Ejecuta las 3 fases del pipeline para una tarea específica."""
    print("\n" + "="*60)
    print(f"TRABAJANDO EN: {nombre_archivo}")
    print("="*60)

    # --- FASE 1: GENERADOR ---
    prompt_1 = f"Actúa como desarrollador Python Senior. {tarea_usuario}. Devuelve solo el código en un bloque markdown."
    res_1 = llamar_ollama(MODELO_GENERADOR, prompt_1, "FASE 1 - GENERACION (Llama 3)")
    
    if not res_1:
        print("Fase 1 falló. No se puede continuar.")
        return
        
    codigo_base = extraer_codigo(res_1)
    # Guardamos auditoría base
    guardar_archivo(f"audit_1_{nombre_archivo}", codigo_base, "Base (Llama 3)")

    # --- FASE 2: REVISOR ---
    prompt_2 = (
        "Revisa este código. Aplica PEP8 estrictamente, añade docstrings profesionales y manejo de errores robusto. "
        "Devuelve solo el código corregido en markdown:\n\n" + codigo_base
    )
    res_2 = llamar_ollama(MODELO_REVISOR, prompt_2, "FASE 2 - REVISION")
    
    if res_2:
        codigo_revisado = extraer_codigo(res_2)
    else:
        print("Fase 2 falló. Usando código de Fase 1.")
        codigo_revisado = codigo_base
        
    guardar_archivo(f"audit_2_{nombre_archivo}", codigo_revisado, "Revisión (Llama 3)")

    # --- FASE 3: PULIDOR ---
    prompt_3 = (
        "Toma este código y asegura que todos los mensajes al usuario sean en un español corporativo impecable. "
        "Limpia el formato y optimiza. Devuelve solo el código final en markdown:\n\n" + codigo_revisado
    )
    res_3 = llamar_ollama(MODELO_PULIDOR, prompt_3, "FASE 3 - PULIDO")
    
    if res_3:
        codigo_final = extraer_codigo(res_3)
        print(">>> [PULIDO] Fase 3 completada con éxito.")
    else:
        print(">>> [FALLBACK] Fase 3 falló. Usando versión de Fase 2 como final.")
        codigo_final = codigo_revisado

    # GUARDADO FINAL
    guardar_archivo(nombre_archivo, codigo_final, "Resultado Final")
    print("\n" + "="*60)
    print(f"¡HECHO! Tu herramienta está lista: {nombre_archivo}")
    print("="*60 + "\n")

def main():
    print("*"*65)
    print(" BIENVENIDO AL ASISTENTE DE DESARROLLO CONTINUO SOLPRO (3 CEREBROS)")
    print("*"*65)
    
    while True:
        print("\n[MENU PRINCIPAL]")
        tarea = input("¿Qué herramienta o automatización necesitas que programemos hoy?\n(Escribe 'salir' para terminar): ").strip()
        
        if tarea.lower() == 'salir':
            print("\nFinalizando asistente. ¡Buen día, Arquitecto!")
            break
            
        if not tarea:
            continue
            
        nombre = input("\n¿Qué nombre quieres darle al script final? (ej: mi_herramienta.py): ").strip()
        
        # Validar y corregir extensión .py
        if not nombre:
            nombre = "herramienta_generada.py"
        if not nombre.lower().endswith(".py"):
            nombre += ".py"
            
        # Ejecutar el pipeline para esta tarea
        try:
            ejecutar_pipeline(tarea, nombre)
        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Volviendo al menú principal...")
            continue
        except Exception as e:
            print(f"\nOcurrió un error inesperado durante el pipeline: {e}")

if __name__ == "__main__":
    main()
