import requests
import sys
import re

# =============================================================================
# CONFIGURACIÓN DEL ORQUESTADOR DE DOS CEREBROS
# =============================================================================
# Cerebro 1: Genera la lógica base y el código inicial
MODELO_GENERADOR = "gemma4:26b"

# Cerebro 2: Recibe el output del Cerebro 1, lo revisa, optimiza y documenta
MODELO_REVISOR   = "llama3:latest"

# Endpoint de la API local de Ollama
URL_OLLAMA = "http://127.0.0.1:11434/api/generate"

# =============================================================================
# FUNCIÓN DE COMUNICACIÓN CON OLLAMA
# =============================================================================
def llamar_a_ollama(modelo, prompt, fase=""):
    """
    Envía un prompt a un modelo específico en Ollama y retorna la respuesta.

    Args:
        modelo (str): Nombre del modelo a usar (ej. 'gemma4:26b').
        prompt (str): El texto de instrucción a enviar.
        fase  (str): Etiqueta descriptiva para mostrar en consola.

    Returns:
        str | None: La respuesta en texto del modelo, o None si falla.
    """
    print(f"\n{'='*60}")
    print(f"  🧠 [{fase}] Invocando modelo: {modelo}")
    print(f"{'='*60}")

    payload = {
        "model":  modelo,
        "prompt": prompt,
        "stream": False   # Obtenemos toda la respuesta de una vez
    }

    try:
        response = requests.post(URL_OLLAMA, json=payload, timeout=300)
        response.raise_for_status()
        texto = response.json().get("response", "").strip()
        return texto

    except requests.exceptions.ConnectionError:
        print(f"\n❌ [ERROR] No se pudo conectar a Ollama en {URL_OLLAMA}")
        print("   → Asegúrate de que el servidor Ollama esté en ejecución.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"\n❌ [ERROR] El modelo {modelo} tardó demasiado en responder (timeout).")
        return None
    except Exception as e:
        print(f"\n❌ [ERROR] Fallo inesperado: {e}")
        return None


# =============================================================================
# FUNCIÓN DE EXTRACCIÓN DE CÓDIGO
# =============================================================================
def extraer_codigo(texto):
    """
    Extrae bloques de código Python de una respuesta markdown.
    Si no encuentra bloques delimitados, devuelve el texto completo.
    """
    patron = r"```(?:python)?\n?(.*?)\n?```"
    bloques = re.findall(patron, texto, re.DOTALL)
    if bloques:
        # Devuelve el bloque más largo (el código principal, no ejemplos cortos)
        return max(bloques, key=len).strip()
    return texto.strip()


# =============================================================================
# FUNCIÓN DE GUARDADO AUTOMÁTICO
# =============================================================================
def guardar_resultado(codigo, nombre_archivo="resultado_final.py"):
    """
    Guarda el código final revisado en un archivo .py local.

    Args:
        codigo (str): El código a guardar.
        nombre_archivo (str): Nombre del archivo destino.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            # Cabecera informativa al inicio del archivo generado
            f.write("# ============================================================\n")
            f.write(f"# Generado por: {MODELO_GENERADOR}\n")
            f.write(f"# Revisado por: {MODELO_REVISOR}\n")
            f.write("# Orquestador: ollama_bridge.py\n")
            f.write("# ============================================================\n\n")
            f.write(codigo)
        print(f"\n✅ Archivo guardado exitosamente: '{nombre_archivo}'")
    except Exception as e:
        print(f"\n❌ [ERROR] No se pudo guardar el archivo: {e}")


# =============================================================================
# FLUJO PRINCIPAL DEL ORQUESTADOR
# =============================================================================
def orquestador(tarea=None):
    """
    Coordina el pipeline completo:
      Fase 1 (Gemma)  → Generación del código base
      Fase 2 (Llama3) → Revisión, optimización y documentación
      Fase 3          → Guardado automático del resultado final
    """
    print("\n" + "★"*60)
    print("   ORQUESTADOR DE DOS CEREBROS — Ollama Bridge")
    print(f"   Generador : {MODELO_GENERADOR}")
    print(f"   Revisor   : {MODELO_REVISOR}")
    print("★"*60)

    # Entrada de la tarea (interactiva o pasada como argumento)
    if tarea is None:
        tarea = input("\n¿Qué código quieres generar?: ").strip()
        if not tarea:
            print("No ingresaste ninguna tarea. Saliendo.")
            sys.exit(0)

    print(f"\n📋 Tarea recibida:\n   {tarea}")

    # ------------------------------------------------------------------
    # FASE 1: GEMMA4:26B — Generación del código base
    # ------------------------------------------------------------------
    prompt_generador = (
        f"Eres un desarrollador Python experto. Tu tarea es escribir ÚNICAMENTE el código "
        f"Python funcional para el siguiente requerimiento. No expliques nada, solo entrega "
        f"el código dentro de un bloque markdown ```python.\n\n"
        f"Requerimiento: {tarea}"
    )

    codigo_bruto = llamar_a_ollama(MODELO_GENERADOR, prompt_generador, fase="FASE 1 — GEMMA4:26B GENERANDO")

    if not codigo_bruto:
        print("\n❌ Gemma no devolvió código. Abortando.")
        return

    print("\n--- OUTPUT CRUDO DE GEMMA (Código Base) ---")
    print(codigo_bruto)

    # Extraemos el bloque de código limpio para pasarlo al revisor
    codigo_limpio_gemma = extraer_codigo(codigo_bruto)

    # ------------------------------------------------------------------
    # FASE 2: LLAMA3 — Revisión, optimización y documentación
    # ------------------------------------------------------------------
    prompt_revisor = (
        f"Eres un arquitecto de software Senior especializado en Python. "
        f"Tu trabajo es tomar el siguiente código generado por un modelo de IA (Gemma), "
        f"realizar las siguientes tareas y entregar el resultado COMPLETO dentro de un bloque "
        f"markdown ```python:\n\n"
        f"1. Revisa y corrige cualquier error de lógica o sintaxis.\n"
        f"2. Optimiza el código siguiendo PEP 8.\n"
        f"3. Agrega docstrings completos a funciones y al módulo.\n"
        f"4. Añade comentarios explicativos en las partes clave.\n"
        f"5. Asegúrate de que el manejo de errores (try/except) sea robusto.\n\n"
        f"CÓDIGO ORIGINAL DE GEMMA:\n"
        f"```python\n{codigo_limpio_gemma}\n```"
    )

    respuesta_revisor = llamar_a_ollama(MODELO_REVISOR, prompt_revisor, fase="FASE 2 — LLAMA3 REVISANDO")

    if not respuesta_revisor:
        print("\n❌ Llama3 no devolvió respuesta. Guardando el código base de Gemma.")
        guardar_resultado(codigo_limpio_gemma)
        return

    # ------------------------------------------------------------------
    # FASE 3: LIMPIEZA Y GUARDADO AUTOMÁTICO
    # ------------------------------------------------------------------
    codigo_final = extraer_codigo(respuesta_revisor)

    print("\n" + "="*60)
    print("  📄 RESULTADO FINAL — Revisado y Optimizado por LLAMA3")
    print("="*60)
    print(codigo_final)
    print("="*60)

    guardar_resultado(codigo_final)
    print("\n🎉 Pipeline completado con éxito.\n")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    # Si se pasa la tarea como argumento de línea de comandos, se usa directamente
    # Ejemplo: python ollama_bridge.py "Crea una función que calcule el IVA"
    tarea_cli = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    orquestador(tarea=tarea_cli)
