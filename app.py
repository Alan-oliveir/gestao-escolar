from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from database import engine, Base
from routers.alunos import alunos_router
from routers.cursos import cursos_router
from routers.matriculas import matriculas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestão Escolar",
    description="""
        Esta API fornece endpoints para gerenciar alunos, cursos e turmas, em uma instituição de ensino.  

        Permite realizar diferentes operações em cada uma dessas entidades.
    """,
    version="1.0.0",
    docs_url=None,  # Desabilita o Swagger UI padrão
    redoc_url=None,  # Desabilita o ReDoc padrão
)

app.include_router(alunos_router, tags=["alunos"])
app.include_router(cursos_router, tags=["cursos"])
app.include_router(matriculas_router, tags=["matriculas"])


@app.get("/docs", include_in_schema=False)
async def scalar_docs():
    return get_scalar_api_reference(
        openapi_url="/openapi.json",
        title="API de Gestão Escolar",
    )
