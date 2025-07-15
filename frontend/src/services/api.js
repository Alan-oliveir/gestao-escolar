import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Serviços para Alunos
export const alunosService = {
  getAll: () => api.get('/alunos'),
  getById: (id) => api.get(`/alunos/${id}`),
  getByName: (nome) => api.get(`/alunos/nome/${nome}`),
  getByEmail: (email) => api.get(`/alunos/email/${email}`),
  create: (aluno) => api.post('/alunos', aluno),
  update: (id, aluno) => api.put(`/alunos/${id}`, aluno),
  delete: (id) => api.delete(`/alunos/${id}`),
};

// Serviços para Cursos
export const cursosService = {
  getAll: () => api.get('/cursos'),
  getByCodigo: (codigo) => api.get(`/cursos/${codigo}`),
  create: (curso) => api.post('/cursos', curso),
  update: (codigo, curso) => api.put(`/cursos/${codigo}`, curso),
};

// Serviços para Matrículas
export const matriculasService = {
  create: (matricula) => api.post('/matriculas', matricula),
  getByAluno: (nome) => api.get(`/matriculas/aluno/${nome}`),
  getByCurso: (codigo) => api.get(`/matriculas/curso/${codigo}`),
};

export default api;