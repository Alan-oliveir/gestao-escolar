from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Curso as ModelCurso
from schemas import Curso

cursos_router = APIRouter()


@cursos_router.get(
    "/cursos",
    response_model=List[Curso],
    summary="Listar todos os cursos",
    description="Retorna uma lista completa de todos os cursos disponíveis no sistema.",
    response_description="Lista de cursos encontrados"
)
def read_cursos(db: Session = Depends(get_db)):
    cursos = db.query(ModelCurso).all()
    return [Curso.model_validate(curso) for curso in cursos]


@cursos_router.post(
    "/cursos",
    response_model=Curso,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo curso",
    description="Cria um novo curso com os dados fornecidos no sistema.",
    response_description="Curso criado com sucesso"
)
def create_curso(curso: Curso, db: Session = Depends(get_db)):
    db_curso = ModelCurso(**curso.model_dump(exclude={"id"}))
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return Curso.model_validate(db_curso)


@cursos_router.put(
    "/cursos/{codigo_curso}",
    response_model=Curso,
    summary="Atualizar dados do curso",
    description="Atualiza os dados de um curso existente com base no código fornecido.",
    responses={
        200: {"description": "Curso atualizado com sucesso"},
        404: {"description": "Curso não encontrado"}
    }
)
def update_curso(codigo_curso: str, curso: Curso, db: Session = Depends(get_db)):
    db_curso = db.query(ModelCurso).filter(ModelCurso.codigo == codigo_curso).first()
    if db_curso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )

    for key, value in curso.model_dump(exclude_unset=True, exclude={"id"}).items():
        setattr(db_curso, key, value)

    db.commit()
    db.refresh(db_curso)
    return Curso.model_validate(db_curso)


@cursos_router.get(
    "/cursos/{codigo_curso}",
    response_model=Curso,
    summary="Buscar curso por código",
    description="Retorna os detalhes de um curso específico com base no código fornecido.",
    responses={
        200: {"description": "Curso encontrado com sucesso"},
        404: {"description": "Nenhum curso encontrado com esse código"}
    }
)
def read_curso_por_codigo(codigo_curso: str, db: Session = Depends(get_db)):
    db_curso = db.query(ModelCurso).filter(ModelCurso.codigo == codigo_curso).first()
    if db_curso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum curso encontrado com esse código"
        )
    return Curso.model_validate(db_curso)

# Não buscar um curso pelo ID nem deletar em nenhuma hipótese

# @cursos_router.get("/cursos/{curso_id}", response_model=Curso)
# def read_curso(curso_id: int, db: Session = Depends(get_db)):
#     db_curso = db.query(ModelCurso).filter(ModelCurso.id == curso_id).first()
#     if db_curso is None:
#         raise HTTPException(status_code=404, detail="Curso não encontrado")
#     return Curso.from_orm(db_curso)


# @cursos_router.delete("/cursos/{curso_id}", response_model=Curso)
# def delete_curso(curso_id: int, db: Session = Depends(get_db)):
#     db_curso = db.query(ModelCurso).filter(ModelCurso.id == curso_id).first()
#     if db_curso is None:
#         raise HTTPException(status_code=404, detail="Curso não encontrado")

#     curso_deletado = Curso.from_orm(db_curso)

#     db.delete(db_curso)
#     db.commit()
#     return curso_deletado
