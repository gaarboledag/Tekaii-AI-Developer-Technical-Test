from typing import List, Optional
from datetime import datetime

from ...domain.entities.tarea import Tarea, TareaCreate, TareaUpdate, EstadoTarea
from ...domain.repositories.tarea_repository import TareaRepository
from ..database import get_db_connection

class SQLiteTareaRepository(TareaRepository):
    
    def crear(self, tarea: TareaCreate) -> Tarea:
        with get_db_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO tareas (titulo, descripcion, responsable, estado)
                   VALUES (?, ?, ?, ?)""",
                (tarea.titulo, tarea.descripcion, tarea.responsable, EstadoTarea.CREADA.value)
            )
            tarea_id = cursor.lastrowid
            conn.commit()
            
            return self.obtener_por_id(tarea_id)
    
    def obtener_por_id(self, id: int) -> Optional[Tarea]:
        with get_db_connection() as conn:
            row = conn.execute(
                "SELECT * FROM tareas WHERE id = ?", (id,)
            ).fetchone()
            
            if row:
                return self._row_to_tarea(row)
            return None
    
    def obtener_todas(self) -> List[Tarea]:
        with get_db_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM tareas ORDER BY fechaCreacion DESC"
            ).fetchall()
            
            return [self._row_to_tarea(row) for row in rows]
    
    def obtener_por_estado(self, estado: EstadoTarea) -> List[Tarea]:
        with get_db_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM tareas WHERE estado = ? ORDER BY fechaCreacion DESC",
                (estado.value,)
            ).fetchall()
            
            return [self._row_to_tarea(row) for row in rows]
    
    def actualizar(self, id: int, tarea_update: TareaUpdate) -> Optional[Tarea]:
        tarea_actual = self.obtener_por_id(id)
        if not tarea_actual:
            return None
        
        updates = []
        params = []
        
        if tarea_update.titulo is not None:
            updates.append("titulo = ?")
            params.append(tarea_update.titulo)
        
        if tarea_update.descripcion is not None:
            updates.append("descripcion = ?")
            params.append(tarea_update.descripcion)
            
        if tarea_update.estado is not None:
            updates.append("estado = ?")
            params.append(tarea_update.estado.value)
        
        if tarea_update.responsable is not None:
            updates.append("responsable = ?")
            params.append(tarea_update.responsable)
        
        if not updates:
            return tarea_actual
        
        params.append(id)
        query = f"UPDATE tareas SET {', '.join(updates)} WHERE id = ?"
        
        with get_db_connection() as conn:
            conn.execute(query, params)
            conn.commit()
            
        return self.obtener_por_id(id)
    
    def eliminar(self, id: int) -> bool:
        with get_db_connection() as conn:
            cursor = conn.execute("DELETE FROM tareas WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def _row_to_tarea(self, row) -> Tarea:
        fecha_str = row["fechaCreacion"]
        # Manejar diferentes formatos de fecha
        try:
            if 'T' in fecha_str:
                fecha = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
            else:
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        except:
            fecha = datetime.now()
        
        return Tarea(
            id=row["id"],
            titulo=row["titulo"],
            descripcion=row["descripcion"],
            estado=EstadoTarea(row["estado"]),
            responsable=row["responsable"],
            fechaCreacion=fecha
        )
