from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Aluno as ModelAluno
from schemas import Aluno

alunos_router = APIRouter()


@alunos_router.get(
    "/alunos",
    response_model=List[Aluno],
    summary="Listar todos os alunos",
    description="Retorna uma lista completa de todos os alunos cadastrados no sistema.",
    response_description="Lista de alunos encontrados"
)
def read_alunos(db: Session = Depends(get_db)):
    alunos = db.query(ModelAluno).all()
    return [Aluno.model_validate(aluno) for aluno in alunos]


@alunos_router.get(
    "/alunos/{aluno_id}",
    response_model=Aluno,
    summary="Buscar aluno por ID",
    description="Retorna os detalhes de um aluno específico com base no ID fornecido.",
    responses={
        200: {"description": "Aluno encontrado com sucesso"},
        404: {"description": "Aluno não encontrado"}
    }
)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )
    return Aluno.model_validate(db_aluno)


@alunos_router.post(
    "/alunos",
    response_model=Aluno,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo aluno",
    description="Cria um novo aluno com os dados fornecidos no sistema.",
    response_description="Aluno criado com sucesso"
)
def create_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    db_aluno = ModelAluno(**aluno.model_dump(exclude={"id"}))
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return Aluno.model_validate(db_aluno)


@alunos_router.put(
    "/alunos/{aluno_id}",
    response_model=Aluno,
    summary="Atualizar dados do aluno",
    description="Atualiza os dados de um aluno existente com base no ID fornecido.",
    responses={
        200: {"description": "Aluno atualizado com sucesso"},
        404: {"description": "Aluno não encontrado"}
    }
)
def update_aluno(aluno_id: int, aluno: Aluno, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    for key, value in aluno.model_dump(exclude_unset=True).items():
        setattr(db_aluno, key, value)

    db.commit()
    db.refresh(db_aluno)
    return Aluno.model_validate(db_aluno)


@alunos_router.delete(
    "/alunos/{aluno_id}",
    response_model=Aluno,
    summary="Excluir aluno",
    description="Remove um aluno do sistema com base no ID fornecido.",
    responses={
        200: {"description": "Aluno excluído com sucesso"},
        404: {"description": "Aluno não encontrado"}
    }
)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    aluno_deletado = Aluno.model_validate(db_aluno)
    db.delete(db_aluno)
    db.commit()
    return aluno_deletado


@alunos_router.get(
    "/alunos/nome/{nome_aluno}",
    response_model=Union[Aluno, List[Aluno]],
    summary="Buscar aluno por nome",
    description="Busca alunos pelo nome (parcial ou completo). Retorna um único aluno se houver apenas uma correspondência, ou uma lista se houver várias.",
    responses={
        200: {"description": "Aluno(s) encontrado(s) com sucesso"},
        404: {"description": "Nenhum aluno encontrado com esse nome"}
    }
)
def read_aluno_por_nome(nome_aluno: str, db: Session = Depends(get_db)):
    db_alunos = db.query(ModelAluno).filter(
        ModelAluno.nome.ilike(f"%{nome_aluno}%")
    ).all()

    if not db_alunos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum aluno encontrado com esse nome"
        )

    if len(db_alunos) == 1:
        return Aluno.model_validate(db_alunos[0])

    return [Aluno.model_validate(aluno) for aluno in db_alunos]


@alunos_router.get(
    "/alunos/email/{email_aluno}",
    response_model=Aluno,
    summary="Buscar aluno por email",
    description="Busca um aluno específico através do endereço de email.",
    responses={
        200: {"description": "Aluno encontrado com sucesso"},
        404: {"description": "Nenhum aluno encontrado com esse email"}
    }
)
def read_aluno_por_email(email_aluno: str, db: Session = Depends(get_db)):
    db_aluno = db.query(ModelAluno).filter(ModelAluno.email == email_aluno).first()

    if db_aluno is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum aluno encontrado com esse email"
        )

    return Aluno.model_validate(db_aluno)
