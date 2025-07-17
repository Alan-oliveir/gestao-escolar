from typing import List

from pydantic import BaseModel, EmailStr, Field


class Matricula(BaseModel):
    """
    Modelo para representar uma matrícula, vinculando um aluno a um curso.
    """
    aluno_id: int = Field(
        description="ID único do aluno",
        example=1,
        gt=0
    )

    curso_id: int = Field(
        description="ID único do curso",
        example=1,
        gt=0
    )

    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "aluno_id": 1,
                "curso_id": 1
            }
        }


Matriculas = List[Matricula]


class Aluno(BaseModel):
    """
    Modelo para representar um aluno no sistema.
    """
    nome: str = Field(
        description="Nome completo do aluno",
        example="João Silva Santos",
        min_length=2,
        max_length=100
    )

    email: EmailStr = Field(
        description="Endereço de email válido do aluno",
        example="joao.silva@email.com"
    )

    telefone: str = Field(
        description="Número de telefone do aluno",
        example="(11) 99999-9999",
        min_length=10,
        max_length=20
    )

    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "nome": "João Silva Santos",
                "email": "joao.silva@email.com",
                "telefone": "(11) 99999-9999"
            }
        }






Alunos = List[Aluno]


class Curso(BaseModel):
    """
    Modelo para representar um curso no sistema.
    """
    nome: str = Field(
        description="Nome do curso",
        example="Desenvolvimento Web com FastAPI",
        min_length=3,
        max_length=150
    )

    codigo: str = Field(
        description="Código único do curso",
        example="DW001",
        min_length=3,
        max_length=20
    )

    descricao: str = Field(
        description="Descrição detalhada do curso",
        example="Curso completo de desenvolvimento web usando FastAPI, cobrindo desde conceitos básicos até tópicos avançados.",
        min_length=10,
        max_length=500
    )

    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "nome": "Desenvolvimento Web com FastAPI",
                "codigo": "DW001",
                "descricao": "Curso completo de desenvolvimento web usando FastAPI, cobrindo desde conceitos básicos até tópicos avançados."
            }
        }


Cursos = List[Curso]
