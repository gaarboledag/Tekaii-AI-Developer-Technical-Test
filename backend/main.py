from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

from src.infrastructure.database import init_db
from src.application.controllers import tarea_controller

app = FastAPI(
    title="Sistema Kanban API", 
    version="1.0.0",
    description="API REST para gestión de tareas estilo Kanban",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(tarea_controller.router, prefix="/api/tareas", tags=["Tareas"])

@app.on_event("startup")
async def startup_event():
    print("🚀 Iniciando Sistema Kanban API...")
    init_db()
    print("✅ Base de datos inicializada")

@app.get("/")
async def root():
    return {
        "message": "Sistema Kanban API", 
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "kanban-api"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
