# 📘 MANUAL DE USUARIO: SOLPRO AI ASSISTANT
**Versión 1.0 — Ecosistema de Orquestación Local**

Este manual detalla cómo operar, integrar y maximizar el potencial de tu nuevo sistema de "3 Cerebros".

---

## 1. INTRODUCCIÓN AL SISTEMA
SolPro AI utiliza un pipeline de procesamiento secuencial diseñado para minimizar errores humanos y técnicos:
1.  **Gemma 4 (26B)**: El "Ingeniero Principal". Crea la lógica compleja.
2.  **Llama 3 (8B)**: El "Arquitecto Revisor". Corrige errores, aplica estándares PEP8 y añade seguridad (try/except).
3.  **Qwen (0.8B)**: El "Editor Corporativo". Traduce los mensajes a un español profesional y limpia el código.

---

## 2. INSTRUCCIONES DE OPERACIÓN

### Cómo iniciar:
1.  Ve a la carpeta `AGENTES IA` en tu escritorio.
2.  Haz doble clic en `Lanzar_Asistente.bat`.
3.  Se abrirá la interfaz gráfica (GUI) con el logo de SolPro.

### Pasos para generar una herramienta:
1.  **Tarea**: Describe lo que necesitas (ej: "Un script que redimensione imágenes en una carpeta").
2.  **Nombre**: Elige un nombre para el archivo final (ej: `procesador_fotos.py`).
3.  **Ejecutar**: Presiona el botón azul. 
    *   *Nota*: El proceso puede tardar entre 2 y 5 minutos dependiendo de la complejidad, ya que Ollama debe intercambiar modelos en la memoria RAM. **No cierres la ventana hasta recibir el aviso de éxito.**

---

## 3. ACOPLAMIENTO CON PROYECTOS (TRABAJANDO CONMIGO)
Cuando estemos desarrollando proyectos grandes juntos aquí en el chat, puedes usar SolPro como tu **"Laboratorio Local"**:

*   **Generación de Módulos Específicos**: Si estamos diseñando un software de gestión, puedes pedirme a mí la arquitectura general y usar a SolPro para generar los scripts individuales de cada módulo (ej: el módulo de cálculo de impuestos).
*   **Refinamiento de Código**: Si te doy un código en el chat y quieres que sea "más profesional" o que tenga un manejo de errores más robusto para tu entorno real, cópialo y pídele a SolPro: *"Toma este código y optimízalo para mi entorno industrial"*.
*   **Pruebas de Privacidad**: Si tienes datos sensibles de tu empresa, no me los pases a mí (en la nube). Usa SolPro para generar scripts que procesen esos datos localmente en tu computadora.

---

## 4. QUÉ PUEDES HACER (CATÁLOGO DE IDEAS)

### 📊 Automatización de Oficina
*   Consolidar 10 archivos Excel en uno solo.
*   Extraer nombres y correos de una lista de documentos.
*   Crear gráficos automáticos a partir de tablas de ventas.

### 🏭 Herramientas Industriales
*   Calculadoras de mermas de papel o tinta para imprentas.
*   Conversores de formatos de archivos técnicos.
*   Generadores de códigos de barras o etiquetas dinámicas.

### 💻 Utilidades de Programador
*   Scripts de copia de seguridad (Backup) automática.
*   Renombrador masivo de archivos.
*   Limpiador de registros o logs antiguos.

---

## 5. SOLUCIÓN DE PROBLEMAS (FAQ)

*   **¿El botón no abre nada?** Asegúrate de que Ollama esté encendido (revisa el icono cerca del reloj de Windows).
*   **¿Se queda en "Procesando" mucho tiempo?** Es normal. Modelos como Gemma 26B requieren mucha memoria. Si pasan más de 10 minutos sin respuesta, reinicia el asistente.
*   **¿El archivo final está vacío?** Esto ocurre si hay un error de conexión con la API. Revisa que el puerto 11434 esté libre.

---

## 4. INTEGRACIÓN AVANZADA Y ANTIGRAVITY

### Con Proyectos Existentes
Puedes usar SolPro para inyectar mejoras en software que ya tienes funcionando:
*   **Refactorización**: Copia el código de un archivo antiguo y pégalo en SolPro con la instrucción: *"Optimiza este código existente"*.
*   **Nuevos Módulos**: Pide a SolPro que cree complementos para tus herramientas actuales. Solo debes mover el archivo generado a la carpeta de tu proyecto.

### Sinergia con Antigravity (IA en la Nube)
La combinación perfecta de poder:
1.  **Antigravity (Estratega)**: Úsame para diseñar la arquitectura, entender errores complejos o planificar grandes cambios en todo tu ecosistema.
2.  **SolPro (Ejecutor)**: Usa a SolPro para "bajar a tierra" mis ideas. Pásale mis sugerencias para que él las convierta en archivos `.py` robustos, documentados y en español corporativo.

*Ejemplo de flujo*:
1.  Antigravity te da un plan para una base de datos.
2.  Tú copias ese plan y se lo das a SolPro.
3.  SolPro genera el código final y lo guarda en tu PC.

---
**Desarrollado por tu Arquitecto de IA — 2026**
