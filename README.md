# Sistema Kanban de Gestión de Tareas (Prueba Técnica Tekaii)

Este proyecto corresponde a una prueba técnica presentada a Tekaii.  
Consiste en el desarrollo de un sistema estilo Kanban, con un frontend y un backend estructurados, junto con automatizaciones en n8n e integración de un AI Agent activado mediante un trigger de chat.

## Objetivo General

Desarrollar un sistema de gestión de tareas estilo Kanban que incluya:

- Frontend moderno en React.  
- Backend estructurado en Python con FastAPI.  
- Automatizaciones mediante n8n en entorno local.  
- Integración de un AI Agent a través de un trigger de chat.  
- Despliegue mediante Docker Compose, siguiendo principios de arquitectura limpia y buenas prácticas de codificación.  

## Arquitectura

El sistema está compuesto por tres servicios principales, orquestados con Docker Compose:

- **Frontend (React):** Interfaz web estilo Kanban.  
- **Backend (FastAPI):** API REST para la gestión de tareas.  
- **n8n:** Automatizaciones conectadas a la red interna de Docker.  

## Requisitos

- **Docker:** versión ≥ 20.x  
- **Docker Compose:** versión ≥ 1.29  

## Ejecución con Docker Compose (todos los módulos)

Clonar el repositorio:

    git clone https://github.com/TU-USUARIO/kanban-tekaii.git
    cd kanban-tekaii

Levantar toda la aplicación:

    docker compose up --build

Acceso a los servicios:

- Frontend (React): http://localhost:5173  
- Backend (FastAPI): http://localhost:8000
- n8n: http://localhost:5678  

## Ejecución de cada módulo por separado

### Backend (FastAPI)

    cd backend
    uvicorn main:app --reload --port 8000

Acceso: http://localhost:8000

### Frontend (React)

    cd frontend
    npm install
    npm start

Acceso: http://localhost:5173

### Automatizaciones (n8n con Docker)

Crear volumen para persistencia de datos:

    docker volume create n8n_data

Levantar n8n con Docker:

    docker run -it --rm \
      --name n8n \
      -p 5678:5678 \
      -v n8n_data:/home/node/.n8n \
      n8nio/n8n

En este proyecto, n8n ya está configurado en el archivo `docker-compose.yml`, por lo que normalmente basta con:

    docker compose up n8n

Acceso: http://localhost:5678

## Pruebas del Flujo y del AI Agent

### Flujo Kanban

1. Crear una tarea en el frontend.  
2. Verificar que aparece en el tablero.  
3. Mover la tarea entre columnas y confirmar que el backend actualiza el estado.  

### Automatización con n8n

1. Abrir http://localhost:5678.  
2. Importar el workflow ubicado en `n8n_data/workflows`.  
3. Activar el workflow.  

### AI Agent (trigger de chat)

1. Enviar un mensaje al trigger configurado en n8n.  
2. El AI Agent procesará la entrada y responderá según la lógica definida.  
3. Verificar que la respuesta aparece en el flujo de n8n.  

## Pruebas

El sistema cuenta con dos niveles de validación: pruebas automatizadas (unitarias) y pruebas manuales de flujo (end-to-end).  

### Pruebas Automatizadas (Unitarias)

Implementadas con **pytest**, cubren las operaciones CRUD del backend.  

Ejecución:

    cd backend
    pytest -v

Validan que los endpoints de FastAPI funcionan correctamente para:

- Crear tareas.  
- Listar tareas.  
- Actualizar tareas.  
- Eliminar tareas.  

### Pruebas de Flujo (End-to-End Manuales)

Permiten validar el funcionamiento del sistema completo: **Frontend + Backend + n8n + AI Agent**.  

1. **Flujo Kanban**  
   - Crear tarea en el frontend → debe aparecer en la columna Pendiente.  
   - Consultar en el backend (`/tareas`) → debe reflejar la tarea creada.  
   - Mover la tarea → debe actualizarse en el backend.  

2. **Automatización con n8n**  
   - Importar el workflow `n8n_data/workflows/kanban-workflow.json`.  
   - Activar el workflow.  
   - Crear o actualizar una tarea según el trigger configurado.  
   - Confirmar ejecución en el *Execution Log* de n8n.  

3. **AI Agent (Trigger de Chat)**  
   - Enviar mensaje de prueba al trigger (ejemplo: “¿Qué tareas tengo pendientes?”).  
   - Verificar en el flujo de n8n:  
     - El mensaje activa el trigger.  
     - El AI Agent procesa la entrada.  
     - Se devuelve una respuesta (ejemplo: “Tienes 3 tareas en la columna Pendiente”).  

## Estructura del Proyecto

    kanban-tekaii/
    │── backend/         # FastAPI (API REST)
    │── frontend/        # React (UI Kanban)
    │── n8n_data/        # Workflows de n8n
    │── docker-compose.yml
    │── README.md
