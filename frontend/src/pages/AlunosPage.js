import React, { useState, useEffect } from 'react';
import {
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Box,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  IconButton,
  Alert,
  Snackbar
} from '@mui/material';
import { Add, Edit, Delete, Search } from '@mui/icons-material';
import { alunosService } from '../services/api';

const AlunosPage = () => {
  const [alunos, setAlunos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [openDialog, setOpenDialog] = useState(false);
  const [editingAluno, setEditingAluno] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [notification, setNotification] = useState({ open: false, message: '', severity: 'success' });
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    telefone: ''
  });

  useEffect(() => {
    fetchAlunos();
  }, []);

  const fetchAlunos = async () => {
    try {
      const response = await alunosService.getAll();
      setAlunos(response.data);
    } catch (error) {
      showNotification('Erro ao carregar alunos', 'error');
    } finally {
      setLoading(false);
    }
  };

  const showNotification = (message, severity = 'success') => {
    setNotification({ open: true, message, severity });
  };

  const handleSubmit = async () => {
    try {
      if (editingAluno) {
        await alunosService.update(editingAluno.id, formData);
        showNotification('Aluno atualizado com sucesso!');
      } else {
        await alunosService.create(formData);
        showNotification('Aluno criado com sucesso!');
      }
      setOpenDialog(false);
      setFormData({ nome: '', email: '', telefone: '' });
      setEditingAluno(null);
      fetchAlunos();
    } catch (error) {
      showNotification('Erro ao salvar aluno', 'error');
    }
  };

  const handleEdit = (aluno) => {
    setEditingAluno(aluno);
    setFormData({
      nome: aluno.nome,
      email: aluno.email,
      telefone: aluno.telefone
    });
    setOpenDialog(true);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Tem certeza que deseja excluir este aluno?')) {
      try {
        await alunosService.delete(id);
        showNotification('Aluno excluído com sucesso!');
        fetchAlunos();
      } catch (error) {
        showNotification('Erro ao excluir aluno', 'error');
      }
    }
  };

  const filteredAlunos = alunos.filter(aluno =>
    aluno.nome.toLowerCase().includes(searchTerm.toLowerCase()) ||
    aluno.email.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) return <Typography>Carregando...</Typography>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Gerenciamento de Alunos
      </Typography>

      <Box sx={{ mb: 3, display: 'flex', gap: 2, alignItems: 'center' }}>
        <TextField
          placeholder="Buscar aluno..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          InputProps={{
            startAdornment: <Search />,
          }}
          size="small"
        />
        <Button
          variant="contained"
          startIcon={<Add />}
          onClick={() => setOpenDialog(true)}
        >
          Novo Aluno
        </Button>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nome</TableCell>
              <TableCell>Email</TableCell>
              <TableCell>Telefone</TableCell>
              <TableCell>Ações</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredAlunos.map((aluno) => (
              <TableRow key={aluno.id}>
                <TableCell>{aluno.id}</TableCell>
                <TableCell>{aluno.nome}</TableCell>
                <TableCell>{aluno.email}</TableCell>
                <TableCell>{aluno.telefone}</TableCell>
                <TableCell>
                  <IconButton onClick={() => handleEdit(aluno)} color="primary">
                    <Edit />
                  </IconButton>
                  <IconButton onClick={() => handleDelete(aluno.id)} color="error">
                    <Delete />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>
          {editingAluno ? 'Editar Aluno' : 'Novo Aluno'}
        </DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Nome"
            fullWidth
            variant="outlined"
            value={formData.nome}
            onChange={(e) => setFormData({ ...formData, nome: e.target.value })}
          />
          <TextField
            margin="dense"
            label="Email"
            type="email"
            fullWidth
            variant="outlined"
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          />
          <TextField
            margin="dense"
            label="Telefone"
            fullWidth
            variant="outlined"
            value={formData.telefone}
            onChange={(e) => setFormData({ ...formData, telefone: e.target.value })}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">
            {editingAluno ? 'Atualizar' : 'Criar'}
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar
        open={notification.open}
        autoHideDuration={6000}
        onClose={() => setNotification({ ...notification, open: false })}
      >
        <Alert severity={notification.severity} onClose={() => setNotification({ ...notification, open: false })}>
          {notification.message}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default AlunosPage;