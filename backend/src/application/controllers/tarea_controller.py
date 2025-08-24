from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.application.services.tarea_service import TareaService
from src.domain.repositories.tarea_repository import TareaRepository
from src.infrastructure.repositories.sqlite_tarea_repository import SQLiteTareaRepository
from src.application.dto.tarea_dto import TareaCreateDTO, TareaUpdateDTO, TareaResponseDTO
from src.domain.entities.tarea import EstadoTarea

router = APIRouter(prefix="", tags=["Tareas"])

# Dependencias
def get_tarea_repository() -> TareaRepository:
    return SQLiteTareaRepository()

def get_tarea_service(repo: TareaRepository = Depends(get_tarea_repository)) -> TareaService:
    return TareaService(repo)

# Endpoints
@router.post("/", response_model=TareaResponseDTO)
async def crear_tarea(tarea: TareaCreateDTO, service: TareaService = Depends(get_tarea_service)):
    return service.crear_tarea(tarea)

@router.get("/", response_model=List[TareaResponseDTO])
async def obtener_tareas(service: TareaService = Depends(get_tarea_service)):
    return service.obtener_todas_tareas()

@router.get("/{tarea_id}", response_model=TareaResponseDTO)
async def obtener_tarea(tarea_id: int, service: TareaService = Depends(get_tarea_service)):
    tarea = service.obtener_tarea_por_id(tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.put("/{tarea_id}", response_model=TareaResponseDTO)
async def actualizar_tarea(tarea_id: int, tarea_update: TareaUpdateDTO, service: TareaService = Depends(get_tarea_service)):
    tarea = service.actualizar_tarea(tarea_id, tarea_update)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.delete("/{tarea_id}")
async def eliminar_tarea(tarea_id: int, service: TareaService = Depends(get_tarea_service)):
    eliminada = service.eliminar_tarea(tarea_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada exitosamente"}

@router.get("/estado/{estado}", response_model=List[TareaResponseDTO])
async def obtener_tareas_por_estado(estado: EstadoTarea, service: TareaService = Depends(get_tarea_service)):
    return service.obtener_tareas_por_estado(estado)
