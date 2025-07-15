import React from 'react';
import {
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Box
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import PeopleIcon from '@mui/icons-material/People';
import MenuBookIcon from '@mui/icons-material/MenuBook';
import AssignmentIcon from '@mui/icons-material/Assignment';

const Home = () => {
  const navigate = useNavigate();

  const cards = [
    {
      title: 'Alunos',
      description: 'Gerencie alunos, cadastre novos e mantenha dados atualizados.',
      icon: <PeopleIcon sx={{ fontSize: 40 }} />,
      path: '/alunos',
      color: '#1976d2'
    },
    {
      title: 'Cursos',
      description: 'Administre cursos disponíveis e suas informações.',
      icon: <MenuBookIcon sx={{ fontSize: 40 }} />,
      path: '/cursos',
      color: '#388e3c'
    },
    {
      title: 'Matrículas',
      description: 'Gerencie matrículas e vincule alunos aos cursos.',
      icon: <AssignmentIcon sx={{ fontSize: 40 }} />,
      path: '/matriculas',
      color: '#f57c00'
    }
  ];

  return (
    <Box>
      <Typography variant="h3" component="h1" gutterBottom align="center" color="primary">
        Sistema de Gestão Escolar
      </Typography>
      <Typography variant="h6" component="p" gutterBottom align="center" color="text.secondary" sx={{ mb: 4 }}>
        Gerencie alunos, cursos e matrículas de forma simples e eficiente
      </Typography>

      <Grid container spacing={3} justifyContent="center">
        {cards.map((card, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                transition: 'transform 0.2s',
                '&:hover': {
                  transform: 'scale(1.05)',
                }
              }}
            >
              <CardContent sx={{ flexGrow: 1, textAlign: 'center' }}>
                <Box sx={{ color: card.color, mb: 2 }}>
                  {card.icon}
                </Box>
                <Typography variant="h5" component="h2" gutterBottom>
                  {card.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {card.description}
                </Typography>
              </CardContent>
              <CardActions sx={{ justifyContent: 'center', pb: 2 }}>
                <Button
                  size="small"
                  variant="contained"
                  onClick={() => navigate(card.path)}
                  sx={{ bgcolor: card.color }}
                >
                  Acessar
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Home;