import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { api } from '../../services/apiService';

export const fetchTareas = createAsyncThunk('tareas/fetch', async () => {
  return await api.getTareas();
});

const tareasSlice = createSlice({
  name: 'tareas',
  initialState: { tareas: [], loading: false, error: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTareas.pending, (state) => { state.loading = true; state.error = null; })
      .addCase(fetchTareas.fulfilled, (state, action) => { state.loading = false; state.tareas = action.payload; })
      .addCase(fetchTareas.rejected, (state, action) => { state.loading = false; state.error = action.error.message; });
  },
});

export default tareasSlice.reducer;
