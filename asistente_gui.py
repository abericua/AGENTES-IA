"""
SOLPRO AI - Estacion de Trabajo Multi-Agente
============================================
Servidor HTTP local + GUI en navegador (solpro_ui.html).
Pipeline: ARQUITECTO -> CONSTRUCTOR -> AUDITOR
"""

import http.server
import socketserver
import threading
import webbrowser
import urllib.request
import json
import re
import os
import sys
import io

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── Modelos ───────────────────────────────────────────────────────────────────
MODELO_ARQUITECTO  = "llama3:latest"
MODELO_CONSTRUCTOR = "llama3:latest"
MODELO_AUDITOR     = "qwen3.5:0.8b"
URL_OLLAMA         = "http://127.0.0.1:11434/api/generate"
TIMEOUT_GLOBAL     = 600
PORT               = 7432

# Ruta al HTML (mismo directorio que este script)
HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "solpro_ui.html")


# ── Prompts ───────────────────────────────────────────────────────────────────
def prompt_arquitecto(tarea):
    return (
        "Eres un Arquitecto de Software Senior. Tu unica responsabilidad es PLANIFICAR, "
        "nunca codificar.\n\n"
        "Un cliente tiene esta idea: " + tarea + "\n\n"
        "Produce un PLAN DE ARQUITECTURA con este formato exacto:\n\n"
        "## OBJETIVO\n"
        "Una sola oracion que describe que debe hacer el programa terminado.\n\n"
        "## MODULOS\n"
        "Lista numerada de funciones/clases. Para cada una:\n"
        "  - Nombre, parametros (tipos), que devuelve, que hace en una oracion.\n\n"
        "## FLUJO PRINCIPAL\n"
        "Pasos de ejecucion del inicio al final.\n\n"
        "## CASOS DE ERROR\n"
        "Situaciones que el programa debe manejar con try/except.\n\n"
        "No incluyas codigo. Solo el plan."
    )


def prompt_constructor(tarea, plan):
    return (
        "Eres un Desarrollador Python Senior. Tu trabajo es IMPLEMENTAR un plan de arquitectura.\n\n"
        "Idea original del cliente: " + tarea + "\n\n"
        "Plan del Arquitecto (siguelo al pie de la letra):\n" + plan + "\n\n"
        "INSTRUCCIONES:\n"
        "1. Implementa TODAS las funciones/clases del plan sin omitir ninguna.\n"
        "2. Respeta nombres, parametros y tipos de retorno exactos del plan.\n"
        "3. Implementa TODOS los casos de error con try/except especificos.\n"
        "4. Incluye bloque if __name__ == '__main__': con ejemplo funcional.\n"
        "5. Docstrings en cada funcion (Google Style).\n\n"
        "Entrega UNICAMENTE el codigo en un bloque ```python. Sin explicaciones."
    )


def prompt_auditor(tarea, plan, codigo):
    return (
        "Eres un Auditor de Calidad de Software con vision completa del proyecto.\n\n"
        "IDEA ORIGINAL: " + tarea + "\n\n"
        "PLAN DEL ARQUITECTO:\n" + plan + "\n\n"
        "CODIGO DEL CONSTRUCTOR:\n```python\n" + codigo + "\n```\n\n"
        "AUDITORIA EN TRES PASOS:\n\n"
        "PASO 1 - VERIFICACION: El codigo cumple la idea y el plan? "
        "Lista en max 3 lineas que falta o esta mal.\n\n"
        "PASO 2 - CORRECCIONES: Corrige los problemas. "
        "Si no hay, optimiza sin cambiar logica.\n\n"
        "PASO 3 - ENTREGA FINAL: Mensajes al usuario en espanol corporativo impecable.\n"
        "Entrega el codigo final auditado en un bloque ```python."
    )


# ── Ollama ────────────────────────────────────────────────────────────────────
def call_ollama(modelo, prompt):
    payload = {"model": modelo, "prompt": prompt, "stream": True}
    req = urllib.request.Request(
        URL_OLLAMA,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    tokens = []
    with urllib.request.urlopen(req, timeout=TIMEOUT_GLOBAL) as r:
        for linea in r:
            if not linea.strip():
                continue
            try:
                chunk = json.loads(linea.decode("utf-8"))
                t = chunk.get("response", "")
                if t:
                    tokens.append(t)
                if chunk.get("done", False):
                    break
            except json.JSONDecodeError:
                continue
    return "".join(tokens)


# ── Servidor ──────────────────────────────────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):

    def log_message(self, *args):
        pass  # Silenciar logs del servidor en consola

    def do_GET(self):
        if self.path == "/":
            try:
                with open(HTML_PATH, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                msg = b"Error: no se encontro solpro_ui.html en el mismo directorio."
                self.send_response(500)
                self.send_header("Content-Type", "text/plain")
                self.send_header("Content-Length", str(len(msg)))
                self.end_headers()
                self.wfile.write(msg)

        elif self.path == "/pick-dir":
            folder = ""
            try:
                import tkinter as tk
                from tkinter import filedialog
                r = tk.Tk()
                r.withdraw()
                r.attributes("-topmost", True)
                folder = filedialog.askdirectory(parent=r)
                r.destroy()
            except Exception:
                pass
            self._json({"path": folder})

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path != "/run":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body   = json.loads(self.rfile.read(length))
        fase   = body.get("fase")
        tarea  = body.get("tarea", "")
        plan   = body.get("plan", "")
        codigo = body.get("codigo", "")
        nombre = body.get("nombre", "herramienta_solpro.py")
        dir_p  = body.get("dir", "") or os.getcwd()

        if not nombre.endswith(".py"):
            nombre += ".py"

        if fase == 1:
            modelo = MODELO_ARQUITECTO
            prompt = prompt_arquitecto(tarea)
        elif fase == 2:
            modelo = MODELO_CONSTRUCTOR
            prompt = prompt_constructor(tarea, plan)
        elif fase == 3:
            modelo = MODELO_AUDITOR
            prompt = prompt_auditor(tarea, plan, codigo)
        else:
            self.send_response(400)
            self.end_headers()
            return

        try:
            texto = call_ollama(modelo, prompt)
        except Exception as e:
            self._json({"texto": "[ERROR: " + str(e) + "]", "ok": False})
            return

        # Guardar archivos de auditoria
        try:
            os.makedirs(dir_p, exist_ok=True)
            if fase == 1:
                ruta = os.path.join(dir_p, "audit_plan_" + nombre + ".txt")
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(texto)
            elif fase == 2:
                m = re.search(r"```(?:python)?\s*(.*?)\s*```", texto, re.DOTALL)
                contenido = m.group(1).strip() if m else texto
                ruta = os.path.join(dir_p, "audit_base_" + nombre)
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(contenido)
            elif fase == 3:
                m = re.search(r"```(?:python)?\s*(.*?)\s*```", texto, re.DOTALL)
                contenido = m.group(1).strip() if m else texto
                ruta = os.path.join(dir_p, nombre)
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(contenido)
                print("[OK] Guardado: " + ruta)
        except Exception as e:
            print("[WARN] No se pudo guardar archivo: " + str(e))

        self._json({"texto": texto, "ok": True})

    def _json(self, data):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST,GET,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    url = "http://localhost:" + str(PORT)
    print("=" * 55)
    print("  SOLPRO AI - Estacion de Trabajo Multi-Agente")
    print("  Interfaz: " + url)
    print("=" * 55)

    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("", PORT), Handler)
    threading.Timer(0.9, lambda: webbrowser.open(url)).start()

    print("  Servidor activo. Presiona Ctrl+C para detener.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Detenido. Hasta pronto!")
        server.shutdown()


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    url = "http://localhost:" + str(PORT)
    print("=" * 55)
    print("  SOLPRO AI - Estacion de Trabajo Multi-Agente")
    print("  Interfaz: " + url)
    print("=" * 55)

    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("", PORT), Handler)
    threading.Timer(0.9, lambda: webbrowser.open(url)).start()

    print("  Servidor activo. Presiona Ctrl+C para detener.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Detenido. Hasta pronto!")
        server.shutdown()
