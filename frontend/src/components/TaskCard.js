import React from 'react';
import Edit2Icon from './icons/Edit2Icon';
import Trash2Icon from './icons/Trash2Icon';
import UserIcon from './icons/UserIcon';
import CalendarIcon from './icons/CalendarIcon';

const TaskCard = ({ tarea, columnas, onEdit, onDelete, onStatusChange }) => {
  const formatDate = (dateString) => {
    try {
      return new Date(dateString).toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
      });
    } catch {
      return 'Fecha inválida';
    }
  };

  return (
    <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 mb-3 group hover:shadow-md transition-shadow">
      <div className="flex justify-between items-start mb-2">
        <h3 className="font-semibold text-gray-800 text-sm">{tarea.titulo}</h3>
        <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
          <button onClick={() => onEdit(tarea)} className="p-1 text-gray-500 hover:text-blue-600">
            <Edit2Icon />
          </button>
          <button onClick={() => onDelete(tarea.id)} className="p-1 text-gray-500 hover:text-red-600">
            <Trash2Icon />
          </button>
        </div>
      </div>

      <p className="text-gray-600 text-xs mb-3 line-clamp-2">{tarea.descripcion}</p>

      <div className="flex items-center gap-2 text-xs text-gray-500 mb-2">
        <UserIcon />
        <span>{tarea.responsable}</span>
      </div>

      <div className="flex items-center gap-2 text-xs text-gray-500">
        <CalendarIcon />
        <span>{formatDate(tarea.fechaCreacion)}</span>
      </div>

      <select
        value={tarea.estado}
        onChange={(e) => onStatusChange(tarea.id, e.target.value)}
        className="mt-2 w-full text-xs border border-gray-300 rounded px-2 py-1 bg-white"
      >
        {columnas.map(col => (
          <option key={col.id} value={col.id}>{col.titulo}</option>
        ))}
      </select>
    </div>
  );
};

export default TaskCard;
