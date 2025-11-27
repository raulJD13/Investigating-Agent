---
title: Agente Investigador
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
---


# Agente Investigador con Inteligencia Artificial

Este proyecto presenta un agente conversacional desarrollado en Python que integra un modelo de lenguaje avanzado y un conjunto de herramientas para ejecutar tareas del mundo real, incluyendo búsquedas web en tiempo real y generación de documentos PDF. Su propósito es servir como pieza demostrativa dentro de un portafolio profesional orientado a ingeniería de software e inteligencia artificial.

![Image](https://github.com/user-attachments/assets/4d1b0c5e-4020-4f7f-985e-7fb58d282437)

## Descripción General

El agente combina un modelo de lenguaje de última generación con funciones externas que amplían sus capacidades. La arquitectura está diseñada bajo un enfoque modular: el modelo recibe la instrucción del usuario, determina si es necesario invocar una herramienta y gestiona la devolución del resultado final. La aplicación se ejecuta sobre una interfaz web desarrollada con Gradio.

## Funcionalidades Principales

* **Modelo de Lenguaje Avanzado**: Procesa instrucciones, mantiene contexto conversacional y selecciona acciones apropiadas.
* **Búsqueda en Tiempo Real**: Acceso a información actualizada mediante una herramienta de consulta externa.
* **Generación Automática de Documentos**: Posibilidad de crear y almacenar resúmenes o textos en formato PDF.
* **Ejecución Automática de Herramientas**: El agente determina cuándo activar cada herramienta disponible.
* **Interfaz Web Interactiva**: Sistema conversacional accesible vía navegador.

## Arquitectura del Sistema

1. **Capa de LLM**: Gestiona la conversación y decide el flujo de acción.
2. **Capa de Herramientas**: Conjunto de funciones que el modelo puede invocar de forma automática.
3. **Capa de Integración**: Coordina las llamadas entre el modelo, las herramientas y la interfaz de usuario.
4. **Interfaz de Usuario**: Construida con Gradio, permite comunicación directa con el agente.

## Instalación

### Requisitos Previos

* Python 3.10 o superior
* Claves API para los servicios utilizados

### Pasos de Instalación

1. Clonar el repositorio

   ```bash
   git clone https://github.com/tu-usuario/agente-investigador.git
   cd agente-investigador
   ```
2. Crear un entorno virtual

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instalar dependencias

   ```bash
   pip install -r requirements.txt
   ```
4. Configurar variables de entorno en `.env`

   ```env
   GOOGLE_API_KEY="tu_clave_api"
   PPLX_API_KEY="tu_clave_api"
   ```
5. Ejecutar la aplicación

   ```bash
   python app.py
   ```

## Estructura del Proyecto

```
├── app.py
├── requirements.txt
├── .env (no incluido)
├── README.md
└── assets/
```

## Flujo de Funcionamiento del Agente

1. El usuario envía una solicitud mediante la interfaz.
2. El modelo procesa la petición y analiza si requiere una herramienta.
3. En caso necesario, el modelo activa la herramienta correspondiente mediante llamadas automáticas.
4. Se devuelve al usuario una respuesta basada en datos actualizados o en procesos ejecutados.

## Seguridad y Gestión de Secretos

Las claves API se almacenan en un archivo `.env` y se cargan mediante `python-dotenv`. Este archivo no debe compartirse ni incluirse en controles de versión.

## Posibles Mejoras Futuras

* Incorporación de soporte para nuevas herramientas.
* Registro persistente de interacciones.
* Sistema avanzado de logs y métricas.
* Despliegue en plataformas en la nube.

## Autoría

Raúl Jiménez.
Desarrollado como parte del portafolio profesional orientado a ingeniería de software, inteligencia artificial y sistemas autónomos.
