from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TareaCreateDTO(BaseModel):
    """DTO para crear una nueva tarea"""
    titulo: str
    descripcion: Optional[str] = None
    estado: Optional[str] = "pendiente"
    responsable: str

class TareaUpdateDTO(BaseModel):
    """DTO para actualizar una tarea existente"""
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    responsable: Optional[str] = None

class TareaResponseDTO(BaseModel):
    """DTO para responder con la información de una tarea"""
    id: int
    titulo: str
    descripcion: Optional[str]
    estado: str
    responsable: str
    fechaCreacion: datetime

    class Config:
        from_attributes = True
