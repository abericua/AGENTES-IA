import urllib.request
import json
import sys
import os

def call_ollama(model, prompt):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        with urllib.request.urlopen(req) as response:
            full_response = ""
            for line in response:
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    token = chunk.get("response", "")
                    print(token, end="", flush=True)
                    full_response += token
                    if chunk.get("done"):
                        break
            return full_response
    except Exception as e:
        print(f"\n[ERROR] No se pudo conectar con Ollama: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python engine.py <modelo>")
        return

    model = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else model

    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print(f"  CHAT INDIVIDUAL: {name}")
    print(f"  Modelo activo: {model}")
    print("  Escribe 'salir' para finalizar")
    print("="*60)

    while True:
        prompt = input("\n\n>>> Tú: ").strip()
        if prompt.lower() in ['salir', 'exit', 'quit']:
            break
        
        if not prompt:
            continue

        print(f"\n🧠 {name}: ", end="")
        call_ollama(model, prompt)
        print("\n" + "-"*30)

if __name__ == "__main__":
    main()
