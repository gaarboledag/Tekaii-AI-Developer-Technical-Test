import React, { useEffect, useState } from 'react';
import TaskCard from '../components/TaskCard';
import PlusIcon from '../components/icons/PlusIcon';
import { api } from '../services/apiService';

const KanbanBoard = () => {
  const [tareas, setTareas] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [formData, setFormData] = useState({ titulo: '', descripcion: '', responsable: 'Juan Henao' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const responsables = ['Juan Henao','Nicolas Murillo','Gerson Gomez','Guillermo Arboleda'];
  const columnas = [
    { id: 'Creada', titulo: 'Creada', color: 'bg-blue-50' },
    { id: 'En progreso', titulo: 'En Progreso', color: 'bg-yellow-50' },
    { id: 'Bloqueada', titulo: 'Bloqueada', color: 'bg-red-50' },
    { id: 'Finalizada', titulo: 'Finalizada', color: 'bg-green-50' },
    { id: 'Cancelada', titulo: 'Cancelada', color: 'bg-gray-50' }
  ];

  const loadTareas = async () => {
    try { setLoading(true); setError(null); const data = await api.getTareas(); setTareas(data); }
    catch { setError('Error cargando tareas'); } 
    finally { setLoading(false); }
  };

  useEffect(() => { loadTareas(); }, []);

  const handleEdit = (tarea) => { setEditingTask(tarea); setFormData(tarea); setShowModal(true); };
  const handleDelete = async (id) => { if(window.confirm('Eliminar tarea?')) { await api.deleteTarea(id); loadTareas(); } };
  const handleStatusChange = async (id, estado) => { await api.updateTarea(id, { estado }); loadTareas(); };
  const handleSubmit = async (e) => { 
    e.preventDefault(); 
    if(editingTask) await api.updateTarea(editingTask.id, formData); 
    else await api.createTarea(formData); 
    setShowModal(false); 
    setEditingTask(null); 
    setFormData({ titulo:'',descripcion:'',responsable:'Juan Henao' }); 
    loadTareas(); 
  };

  if (loading) return <div className="flex justify-center items-center h-screen text-lg">⏳ Cargando...</div>;

  return (
    <div className="min-h-screen p-6 bg-gray-100">
      {/* Header */}
      <div className="flex flex-col gap-4 md:flex-row md:justify-between md:items-center mb-8">
        <div>
          <h1 className="text-4xl font-extrabold text-gray-800">Sistema Kanban Interactivo</h1>
          <p className="text-gray-600">App Tablero Kanban integrado a un agente conversacional. Backend: Python + FastAPI, Frontend: React.</p>
          <p className="text-sm text-gray-500">Presentado por Guillermo Andrés Arboleda como prueba técnica para Tekaii.</p>
        </div>
        <button 
          onClick={() => setShowModal(true)} 
          className="flex items-center gap-2 bg-gray-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl shadow-md transition"
        >
          <PlusIcon /> Nueva Tarea
        </button>
      </div>

      {/* Columnas */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
        {columnas.map(columna => (
          <div key={columna.id} className={`${columna.color} p-4 rounded-xl shadow-sm`}>
            <h2 className="font-semibold text-lg mb-3 text-gray-800">{columna.titulo}</h2>
            <div className="flex flex-col gap-3">
              {tareas.filter(t => t.estado === columna.id).map(t => (
                <TaskCard 
                  key={t.id} 
                  tarea={t} 
                  columnas={columnas} 
                  onEdit={handleEdit} 
                  onDelete={handleDelete} 
                  onStatusChange={handleStatusChange} 
                />
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
          <div className="bg-white rounded-2xl shadow-xl p-6 w-full max-w-md">
            <h3 className="text-xl font-bold mb-4">{editingTask ? '✏️ Editar Tarea' : '🆕 Nueva Tarea'}</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
              <input 
                className="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-400 outline-none" 
                placeholder="Título" 
                value={formData.titulo} 
                onChange={e => setFormData({...formData,titulo:e.target.value})} 
                required 
              />
              <textarea 
                className="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-400 outline-none" 
                placeholder="Descripción" 
                value={formData.descripcion} 
                onChange={e => setFormData({...formData,descripcion:e.target.value})} 
                required 
              />
              <select 
                className="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-400 outline-none" 
                value={formData.responsable} 
                onChange={e => setFormData({...formData,responsable:e.target.value})}
              >
                {responsables.map(r => <option key={r} value={r}>{r}</option>)}
              </select>
              <div className="flex justify-end gap-3 mt-4">
                <button 
                  type="button" 
                  onClick={() => { setShowModal(false); setEditingTask(null); setFormData({ titulo:'',descripcion:'',responsable:'Juan Henao' }); }}
                  className="px-4 py-2 rounded-lg border hover:bg-gray-100"
                >
                  Cancelar
                </button>
                <button 
                  type="submit" 
                  className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 shadow"
                >
                  {editingTask ? 'Actualizar' : 'Crear'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default KanbanBoard;
