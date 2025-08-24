import warnings
import pytest
from fastapi.testclient import TestClient
from main import app
from src.domain.entities.tarea import EstadoTarea


# ------------------------------------------------------
# Fixture que ejecuta startup/shutdown y usa TestClient
# ------------------------------------------------------
@pytest.fixture(scope="function")
def client():
    # Inicializa la app y la DB como en producción
    from src.infrastructure.database import init_db
    init_db()
    with TestClient(app) as c:
        yield c

# ------------------------
# Tests del CRUD de Tareas
# ------------------------
def test_create_tarea(client):
    payload = {
        "titulo": "Nueva tarea",
        "descripcion": "Descripción de la tarea",
        "responsable": "Gerson Gomez"
    }
    response = client.post("/api/tareas", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == payload["titulo"]
    assert data["responsable"] == payload["responsable"]
    assert data["estado"] == EstadoTarea.CREADA

def test_list_tareas(client):
    response = client.get("/api/tareas")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_tarea(client):
    payload = {
        "titulo": "Editar tarea",
        "descripcion": "Antes de editar",
        "responsable": "Gerson Gomez"
    }
    create_res = client.post("/api/tareas", json=payload)
    tarea_id = create_res.json()["id"]

    update_payload = {
        "titulo": "Editar tarea",
        "descripcion": "Después de editar",
        "estado": EstadoTarea.FINALIZADA,
        "responsable": "Gerson Gomez"
    }
    response = client.put(f"/api/tareas/{tarea_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["descripcion"] == "Después de editar"
    assert data["estado"] == EstadoTarea.FINALIZADA
    assert data["responsable"] == payload["responsable"]

def test_delete_tarea(client):
    payload = {
        "titulo": "Eliminar tarea",
        "descripcion": "Se va a borrar",
        "responsable": "Gerson Gomez"
    }
    create_res = client.post("/api/tareas", json=payload)
    tarea_id = create_res.json()["id"]

    response = client.delete(f"/api/tareas/{tarea_id}")
    assert response.status_code == 200

    assert response.json()["message"] == "Tarea eliminada exitosamente"

    get_res = client.get(f"/api/tareas/{tarea_id}")
    assert get_res.status_code == 404
