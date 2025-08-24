from typing import List, Optional
from src.domain.entities.tarea import Tarea, TareaCreate, TareaUpdate, EstadoTarea
from src.domain.repositories.tarea_repository import TareaRepository
from src.application.dto.tarea_dto import TareaCreateDTO, TareaUpdateDTO, TareaResponseDTO
from src.application.validators.tarea_validator import TareaValidator


class TareaService:
    def __init__(self, tarea_repository: TareaRepository):
        self.tarea_repository = tarea_repository
        self.validator = TareaValidator(["Gerson Gomez", "Guillermo Arboleda", "Nicolas Murillo", "Juan Henao"])

    def crear_tarea(self, tarea_dto: TareaCreateDTO) -> TareaResponseDTO:
        self.validator.validar_responsable(tarea_dto.responsable)

        tarea_entidad = TareaCreate(**tarea_dto.dict())
        tarea = self.tarea_repository.crear(tarea_entidad)

        return TareaResponseDTO.from_orm(tarea)

    def obtener_tarea_por_id(self, tarea_id: int) -> Optional[TareaResponseDTO]:
        tarea = self.tarea_repository.obtener_por_id(tarea_id)
        return TareaResponseDTO.from_orm(tarea) if tarea else None

    def obtener_todas_tareas(self) -> List[TareaResponseDTO]:
        tareas = self.tarea_repository.obtener_todas()
        return [TareaResponseDTO.from_orm(t) for t in tareas]

    def obtener_tareas_por_estado(self, estado: EstadoTarea) -> List[TareaResponseDTO]:
        tareas = self.tarea_repository.obtener_por_estado(estado)
        return [TareaResponseDTO.from_orm(t) for t in tareas]

    def actualizar_tarea(self, tarea_id: int, tarea_update_dto: TareaUpdateDTO) -> Optional[TareaResponseDTO]:
        if tarea_update_dto.responsable:
            self.validator.validar_responsable(tarea_update_dto.responsable)

        tarea_update = TareaUpdate(**tarea_update_dto.dict(exclude_unset=True))
        tarea = self.tarea_repository.actualizar(tarea_id, tarea_update)
        return TareaResponseDTO.from_orm(tarea) if tarea else None

    def eliminar_tarea(self, tarea_id: int) -> bool:
        return self.tarea_repository.eliminar(tarea_id)
