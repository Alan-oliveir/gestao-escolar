import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import SchoolIcon from '@mui/icons-material/School';

const Header = () => {
  const navigate = useNavigate();

  const menuItems = [
    { label: 'Início', path: '/' },
    { label: 'Alunos', path: '/alunos' },
    { label: 'Cursos', path: '/cursos' },
    { label: 'Matrículas', path: '/matriculas' },
  ];

  return (
    <AppBar position="static">
      <Toolbar>
        <SchoolIcon sx={{ mr: 2 }} />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Gestão Escolar
        </Typography>
        <Box sx={{ display: 'flex', gap: 2 }}>
          {menuItems.map((item) => (
            <Button
              key={item.path}
              color="inherit"
              onClick={() => navigate(item.path)}
            >
              {item.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;