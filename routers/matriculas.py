from typing import List, Dict, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Matricula as ModelMatricula, Aluno as ModelAluno, Curso as ModelCurso
from schemas import Matricula

matriculas_router = APIRouter()


@matriculas_router.post(
    "/matriculas",
    response_model=Matricula,
    status_code=status.HTTP_201_CREATED,
    summary="Criar nova matrícula",
    description="Cria uma nova matrícula vinculando um aluno a um curso específico.",
    responses={
        201: {"description": "Matrícula criada com sucesso"},
        404: {"description": "Aluno ou Curso não encontrado"}
    }
)
def create_matricula(matricula: Matricula, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.id == matricula.aluno_id).first()
    db_curso = db.query(ModelCurso).filter(ModelCurso.id == matricula.curso_id).first()

    if db_aluno is None or db_curso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno ou Curso não encontrado"
        )

    db_matricula = ModelMatricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return Matricula.model_validate(db_matricula)


@matriculas_router.get(
    "/matriculas/aluno/{nome_aluno}",
    response_model=Dict[str, Union[str, List[str]]],
    summary="Listar cursos do aluno",
    description="Retorna todos os cursos em que um aluno está matriculado, buscando pelo nome.",
    responses={
        200: {"description": "Lista de cursos do aluno"},
        404: {"description": "Aluno não encontrado ou sem matrículas"}
    }
)
def read_matriculas_por_nome_aluno(nome_aluno: str, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.nome.ilike(f"%{nome_aluno}%")).first()

    if not db_aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    cursos_matriculados = []
    for matricula in db_aluno.matriculas:
        curso = matricula.curso
        if curso:
            cursos_matriculados.append(curso.nome)

    if not cursos_matriculados:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O aluno '{nome_aluno}' não possui matrículas cadastradas."
        )

    return {"aluno": db_aluno.nome, "cursos": cursos_matriculados}


@matriculas_router.get(
    "/matriculas/curso/{codigo_curso}",
    response_model=Dict[str, Union[str, List[str]]],
    summary="Listar alunos do curso",
    description="Retorna todos os alunos matriculados em um curso específico, buscando pelo código do curso.",
    responses={
        200: {"description": "Lista de alunos matriculados no curso"},
        404: {"description": "Curso não encontrado ou sem alunos matriculados"}
    }
)
def read_alunos_matriculados_por_codigo_curso(codigo_curso: str, db: Session = Depends(get_db)):
    db_curso = db.query(ModelCurso).filter(ModelCurso.codigo == codigo_curso).first()

    if not db_curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )

    alunos_matriculados = []
    for matricula in db_curso.matriculas:
        aluno = matricula.aluno
        if aluno:
            alunos_matriculados.append(aluno.nome)

    if not alunos_matriculados:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nenhum aluno matriculado no curso '{db_curso.nome}'."
        )

    return {"curso": db_curso.nome, "alunos": alunos_matriculados}
