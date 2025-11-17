---
title: Agente Investigador
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
---

# 🤖 Agente Investigador con IA (Gradio + Gemini + Perplexity)efefq

Este es un proyecto de porfolio que demuestra...
# 🤖 Agente Investigador con IA (Gradio + Gemini + Perplexity)

Este es un proyecto de porfolio que demuestra un agente de IA conversacional construido con Python. El agente utiliza un LLM (Gemini) como "cerebro" y tiene acceso a "herramientas" para realizar tareas en el mundo real.

## 🚀 Demo
*(Aquí puedes poner un GIF o un enlace a tu Hugging Face Space una vez desplegado)*

## ✨ Características

* **Procesamiento de Lenguaje Natural:** Utiliza **Google Gemini** para entender y responder a las peticiones del usuario.
* **Búsqueda Web en Tiempo Real:** Integrado con la **API de Perplexity** para obtener información actualizada que el modelo no conoce.
* **Agente Multi-Herramienta:** El agente puede decidir qué herramienta usar (`buscar` o `guardar_pdf`).
* **Creación de Archivos:** Puede generar y guardar resúmenes en archivos PDF bajo demanda.
* **Interfaz Web:** Utiliza **Gradio** para una interfaz de chat interactiva y fácil de usar.

## 🛠️ Tecnologías Utilizadas

* **Python**
* **Google Gemini (API):** El "cerebro" LLM.
* **Perplexity AI (API):** La herramienta de búsqueda.
* **Gradio:** Para la interfaz de usuario web.
* **fpdf2:** Para la creación de PDFs.
* **python-dotenv:** Para la gestión segura de claves API en local.

## Local (Cómo Ejecutarlo Localmente)

1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/tu-usuario/agente-investigador.git](https://github.com/tu-usuario/agente-investigador.git)
    cd agente-investigador
    ```
2.  Crea un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # (o .\venv\Scripts\activate en Windows)
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Crea un archivo `.env` en la raíz del proyecto y añade tus claves API:
    ```env
    GOOGLE_API_KEY="tu_clave_de_google"
    PPLX_API_KEY="tu_clave_de_perplexity"
    ```
5.  Ejecuta la aplicación:
    ```bash
    python app.py
    ```
6.  Abre tu navegador en la dirección `http://127.0.0.1:7860`.
