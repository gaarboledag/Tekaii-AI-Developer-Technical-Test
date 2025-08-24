import sqlite3
import os
from contextlib import contextmanager
from datetime import datetime

# Usar variable de entorno o default
DATABASE_URL = os.getenv("DATABASE_URL", "/app/data/kanban.db")

def init_db():
    """Inicializar la base de datos"""
    # Crear directorio si no existe
    db_dir = os.path.dirname(DATABASE_URL)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    with sqlite3.connect(DATABASE_URL) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                estado TEXT NOT NULL DEFAULT 'Creada',
                responsable TEXT NOT NULL,
                fechaCreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insertar datos de ejemplo si la tabla está vacía
        count = conn.execute("SELECT COUNT(*) FROM tareas").fetchone()[0]
        if count == 0:
            sample_data = [
                ("Diseñar interfaz", "Crear el diseño del tablero Kanban", "Juan Henao", "Creada"),
                ("Implementar API", "Desarrollar endpoints REST", "Maria Rodriguez", "En progreso"),
                ("Configurar base de datos", "Setup inicial de SQLite", "Carlos Lopez", "Finalizada"),
            ]
            
            conn.executemany(
                "INSERT INTO tareas (titulo, descripcion, responsable, estado) VALUES (?, ?, ?, ?)",
                sample_data
            )
        
        conn.commit()
        print(f"✅ Base de datos inicializada en: {DATABASE_URL}")

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
