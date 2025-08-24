# 📝 Sistema de Gestión de Tareas (Prueba Técnica Tekaii)

Este proyecto corresponde a una **prueba técnica presentada a Tekaii**.  
Consiste en el desarrollo de un sistema estilo **Kanban**, con un frontend moderno, un backend estructurado y automatizaciones con **n8n**, integrando un **AI Agent** activado mediante un trigger de chat.

---

## 🎯 Objetivo General

Desarrollar un sistema de gestión de tareas estilo Kanban que incluya:

- **Frontend moderno** en React.
- **Backend estructurado** en Python con FastAPI.
- **Automatizaciones** mediante n8n en entorno local.
- **Integración de un AI Agent** a través de un trigger de chat.
- Despliegue mediante **Docker Compose**, siguiendo principios de **arquitectura limpia** y buenas prácticas de codificación.

---

## ⚙️ Arquitectura

El sistema está compuesto por tres servicios principales, orquestados con **Docker Compose**:

- **Frontend (React)** → Interfaz web estilo Kanban.  
- **Backend (FastAPI)** → API REST para la gestión de tareas.  
- **n8n** → Automatizaciones conectadas a la red interna de Docker.  

---

## 🚀 Requisitos

- [Docker](https://www.docker.com/) ≥ 20.x  
- [Docker Compose](https://docs.docker.com/compose/) ≥ 1.29  

---

## ▶️ Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/kanban-tekaii.git
   cd kanban-tekaii

2. Levantar la aplicación:
	docker compose up --build

3. Acceso a los servicios:
	Frontend (React) → http://localhost:3000
	Backend (FastAPI) → http://localhost:8000
	n8n → http://localhost:5678

4. Estructura del proyecto:	kanban-tekaii/
	├─ frontend/        # Aplicación React (Dockerfile incluido)
	├─ backend/         # API FastAPI (Dockerfile incluido)
	├─ docker-compose.yml
	├─ .env             # Variables de entorno (ejemplo)
	└─ README.md
