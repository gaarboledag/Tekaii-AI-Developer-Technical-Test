from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class EstadoTarea(str, Enum):
    CREADA = "Creada"
    EN_PROGRESO = "En progreso"
    BLOQUEADA = "Bloqueada"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"

class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200, description="Título de la tarea")
    descripcion: str = Field(..., min_length=1, max_length=1000, description="Descripción detallada")
    responsable: str = Field(..., min_length=1, max_length=100, description="Persona responsable")


class TareaCreate(TareaBase):
    fechaCreacion: datetime = Field(default_factory=datetime.utcnow)

class TareaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=1, max_length=1000)
    estado: Optional[EstadoTarea] = None
    responsable: Optional[str] = Field(None, min_length=1, max_length=100)

class Tarea(TareaBase):
    id: int
    estado: EstadoTarea
    fechaCreacion: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
