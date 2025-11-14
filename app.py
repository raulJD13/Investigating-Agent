import os
import requests
import google.generativeai as genai
import gradio as gr
from fpdf import FPDF
from dotenv import load_dotenv

# --- 1. Cargar Secretos (¡El Modo Profesional!) ---
# Carga las variables del archivo .env en el entorno
load_dotenv() 

try:
    # Lee las claves desde las variables de entorno
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    PPLX_API_KEY = os.environ.get("PPLX_API_KEY")
    
    if not GOOGLE_API_KEY or not PPLX_API_KEY:
        raise ValueError("No se encontraron las claves API. Asegúrate de tener un archivo .env")

    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error al cargar las claves API: {e}")
    exit()

# --- 2. Definición de Herramientas (Igual que antes) ---

def buscar_en_perplexity(query: str) -> dict:
    """Busca en Perplexity para obtener información actualizada y resúmenes."""
    print(f"\n--- 🤖 Herramienta 1: Llamando a Perplexity con consulta: '{query}' ---")
    url = "https://api.perplexity.ai/chat/completions"
    payload = {"model": "sonar-pro", "messages": [{"role": "user", "content": query}]}
    headers = {"accept": "application/json", "content-type": "application/json", "authorization": f"Bearer {PPLX_API_KEY}"}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() 
        api_result = response.json()['choices'][0]['message']['content']
        print(f"--- ✅ Herramienta 1: Respuesta recibida ---")
        return {"resumen_de_perplexity": api_result}
    except Exception as e:
        print(f"Error en API Perplexity: {e}")
        return {"error": str(e)}

def guardar_en_pdf(contenido: str, nombre_archivo: str) -> dict:
    """Guarda una cadena de texto (contenido) en un archivo PDF."""
    print(f"\n--- 🖨️ Herramienta 2: Guardando PDF como: '{nombre_archivo}' ---")
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=contenido.encode('latin-1', 'replace').decode('latin-1'))
        pdf.output(nombre_archivo)
        print(f"--- ✅ Herramienta 2: PDF guardado. ---")
        return {"status": f"PDF guardado exitosamente como '{nombre_archivo}'"}
    except Exception as e:
        print(f"Error al crear PDF: {e}")
        return {"error": f"No se pudo guardar el PDF: {e}"}

# --- 3. Configuración del "Cerebro" (Gemini) ---
tools_para_gemini = [buscar_en_perplexity, guardar_en_pdf]
model = genai.GenerativeModel(model_name="gemini-2.5-pro", tools=tools_para_gemini)
chat = model.start_chat(enable_automatic_function_calling=True)

# --- 4. Función de Interfaz (Igual que antes) ---
def agente_responde(message, history):
    """Función que procesa el input del usuario y devuelve la respuesta del agente."""
    print(f"\n[Usuario]: {message}")
    try:
        response = chat.send_message(message)
        print(f"[Agente]: {response.text}")
        return response.text
    except Exception as e:
        print(f"[Error]: {e}")
        if "429" in str(e):
            return "❌ ERROR: Has superado la cuota de la API de Google (Free Tier). Espera un minuto."
        return f"❌ Ha ocurrido un error: {e}"

# --- 5. Lanzar la Interfaz ---
print("="*50)
print("🤖 Lanzando la Interfaz de Chat... (Modo Local)")
print("="*50)

iface = gr.ChatInterface(
    fn=agente_responde,
    title="🤖 Agente Investigador (Buscar y Guardar PDF)",
    description="Hazme una pregunta y luego pídeme que la guarde en un PDF.",
    examples=["mejores certficaciones para data analytics", "computación neuromórfica en Europa"]
)

# iface.launch() se lanza en una URL local, sin 'share=True'
iface.launch()