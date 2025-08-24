const API_BASE_URL = 'http://localhost:8000';

export const api = {
  async getTareas() {
    const res = await fetch(`${API_BASE_URL}/api/tareas`);
    if (!res.ok) throw new Error('Error obteniendo tareas');
    return await res.json();
  },

  async createTarea(tarea) {
    const res = await fetch(`${API_BASE_URL}/api/tareas`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(tarea),
    });
    if (!res.ok) throw new Error('Error creando tarea');
    return await res.json();
  },

  async updateTarea(id, updates) {
    const res = await fetch(`${API_BASE_URL}/api/tareas/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updates),
    });
    if (!res.ok) throw new Error('Error actualizando tarea');
    return await res.json();
  },

  async deleteTarea(id) {
    const res = await fetch(`${API_BASE_URL}/api/tareas/${id}`, { method: 'DELETE' });
    if (!res.ok) throw new Error('Error eliminando tarea');
    return true;
  },
};
