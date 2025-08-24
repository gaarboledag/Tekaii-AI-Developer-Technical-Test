from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.tarea import Tarea, TareaCreate, TareaUpdate, EstadoTarea

class TareaRepository(ABC):
    @abstractmethod
    def crear(self, tarea: TareaCreate) -> Tarea:
        pass
    
    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Tarea]:
        pass
    
    @abstractmethod
    def obtener_todas(self) -> List[Tarea]:
        pass
    
    @abstractmethod
    def obtener_por_estado(self, estado: EstadoTarea) -> List[Tarea]:
        pass
    
    @abstractmethod
    def actualizar(self, id: int, tarea_update: TareaUpdate) -> Optional[Tarea]:
        pass
    
    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass
