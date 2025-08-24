from typing import List
from fastapi import HTTPException

class TareaValidator:
    def __init__(self, responsables_validos: List[str]):
        self.responsables_validos = responsables_validos

    def validar_responsable(self, responsable: str):
        if responsable not in self.responsables_validos:
            raise HTTPException(
                status_code=400,
                detail=f"El responsable '{responsable}' no es válido. "
                       f"Responsables permitidos: {', '.join(self.responsables_validos)}"
            )
