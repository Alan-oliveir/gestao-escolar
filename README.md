# 🎓 API de Gestão Escolar - Imersão DevOps

Esta é uma API RESTful moderna desenvolvida com **FastAPI** para gerenciar alunos, cursos e matrículas de uma instituição de ensino. O projeto demonstra práticas de DevOps, incluindo containerização com Docker, documentação interativa com Scalar, e deploy na nuvem com Google Cloud Run.

## 🚀 Características

- ✅ **API RESTful** completa com FastAPI
- ✅ **Documentação interativa** moderna com Scalar
- ✅ **Containerização** com Docker
- ✅ **Deploy na nuvem** com Google Cloud Run
- ✅ **Banco de dados** SQLite com SQLAlchemy
- ✅ **Validação de dados** com Pydantic
- ✅ **Estrutura modular** com routers separados

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para Python
- **[Pydantic](https://pydantic.dev/)** - Validação de dados
- **[Scalar](https://scalar.com/)** - Documentação interativa moderna
- **[Docker](https://www.docker.com/)** - Containerização
- **[Google Cloud Run](https://cloud.google.com/run)** - Deploy serverless
- **[SQLite](https://www.sqlite.org/)** - Banco de dados leve

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **[Python 3.10+](https://www.python.org/downloads/)**
- **[Git](https://git-scm.com/downloads)**
- **[Docker](https://www.docker.com/get-started/)** (opcional, para containerização)
- **[Google Cloud CLI](https://cloud.google.com/sdk/docs/install)** (para deploy na nuvem)

## 🏃‍♂️ Executando o Projeto

### Opção 1: Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone <seu-repositorio>
   cd api-gestao-escolar
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   # Criar ambiente virtual
   python3 -m venv venv
   
   # Ativar no Linux/Mac
   source venv/bin/activate
   
   # Ativar no Windows
   # Primeiro, execute como administrador:
   Set-ExecutionPolicy RemoteSigned
   # Depois ative:
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   uvicorn app:app --reload
   ```

5. **Acesse a documentação:**
   - **Documentação Scalar (moderna):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **API Base:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Opção 2: Executar com Docker

1. **Construa a imagem Docker:**
   ```bash
   docker build -t api-gestao-escolar .
   ```

2. **Execute o container:**
   ```bash
   docker run -p 8000:8000 api-gestao-escolar
   ```

3. **Acesse a aplicação:**
   - **Documentação:** [http://localhost:8000/docs](http://localhost:8000/docs)

## ☁️ Deploy no Google Cloud

### Configuração Inicial

1. **Autentique no Google Cloud:**
   ```bash
   gcloud auth login
   gcloud config set project SEU_PROJECT_ID
   ```

2. **Deploy direto no Cloud Run:**
   ```bash
   gcloud run deploy api-gestao-escolar \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8000
   ```

### Deploy via Docker (Alternativo)

1. **Configure o Docker para o Google Cloud:**
   ```bash
   gcloud auth configure-docker
   ```

2. **Construa e envie a imagem:**
   ```bash
   docker build -t gcr.io/SEU_PROJECT_ID/api-gestao-escolar .
   docker push gcr.io/SEU_PROJECT_ID/api-gestao-escolar
   ```

3. **Deploy no Cloud Run:**
   ```bash
   gcloud run deploy api-gestao-escolar \
     --image gcr.io/SEU_PROJECT_ID/api-gestao-escolar \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8000
   ```

## 📁 Estrutura do Projeto

```
api-gestao-escolar/
│
├── app.py                  # Aplicação principal FastAPI
├── database.py             # Configuração do banco SQLite
├── models.py               # Modelos SQLAlchemy
├── schemas.py              # Schemas Pydantic com validação
├── requirements.txt        # Dependências Python
├── Dockerfile             # Configuração Docker
├── .dockerignore          # Arquivos ignorados pelo Docker
├── README.md              # Documentação do projeto
│
└── routers/               # Módulos de rotas
    ├── alunos.py          # Endpoints de alunos
    ├── cursos.py          # Endpoints de cursos
    └── matriculas.py      # Endpoints de matrículas
```

## 🔗 Endpoints da API

### 👨‍🎓 Alunos
- `GET /alunos` - Listar todos os alunos
- `POST /alunos` - Criar novo aluno
- `GET /alunos/{id}` - Buscar aluno por ID
- `PUT /alunos/{id}` - Atualizar aluno
- `DELETE /alunos/{id}` - Excluir aluno
- `GET /alunos/nome/{nome}` - Buscar por nome
- `GET /alunos/email/{email}` - Buscar por email

### 📚 Cursos
- `GET /cursos` - Listar todos os cursos
- `POST /cursos` - Criar novo curso
- `GET /cursos/{codigo}` - Buscar curso por código
- `PUT /cursos/{codigo}` - Atualizar curso

### 📋 Matrículas
- `POST /matriculas` - Criar nova matrícula
- `GET /matriculas/aluno/{nome}` - Listar cursos do aluno
- `GET /matriculas/curso/{codigo}` - Listar alunos do curso

## 🎯 Funcionalidades Principais

### Gestão de Alunos
- Cadastro completo com validação de email
- Busca por nome (parcial) e email
- Atualização e exclusão de registros

### Gestão de Cursos
- Cadastro com código único
- Busca por código do curso
- Atualização de informações

### Sistema de Matrículas
- Vinculação entre alunos e cursos
- Consulta de cursos por aluno
- Consulta de alunos por curso

## 💾 Banco de Dados

O projeto utiliza **SQLite** como banco de dados, que é:
- **Leve e portável** - Perfeito para desenvolvimento e demonstração
- **Sem configuração** - Criado automaticamente na primeira execução
- **Arquivo único** - Armazenado como `escola.db`

### Reiniciar o Banco
Para reiniciar o banco de dados (⚠️ **apaga todos os dados**):
```bash
rm escola.db
```

## 🧪 Testando a API

### Usando a Documentação Interativa
1. Acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Explore os endpoints disponíveis
3. Teste diretamente na interface Scalar

### Usando curl (exemplos)
```bash
# Criar um aluno
curl -X POST "http://127.0.0.1:8000/alunos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao@email.com",
    "telefone": "(11) 99999-9999"
  }'

# Listar alunos
curl -X GET "http://127.0.0.1:8000/alunos"

# Criar um curso
curl -X POST "http://127.0.0.1:8000/cursos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "FastAPI para Iniciantes",
    "codigo": "FAST001",
    "descricao": "Curso introdutório de FastAPI"
  }'
```

## 🔧 Desenvolvimento

### Executar em Modo de Desenvolvimento
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Instalar Dependências de Desenvolvimento
```bash
pip install -r requirements.txt
```

## 🚀 Sobre a Imersão DevOps

Este projeto foi desenvolvido durante a **Imersão Cloud DevOps da Alura e Google Cloud**, onde aprendemos:

- **Fundamentos do DevOps** - Cultura e práticas que unem desenvolvimento e operações
- **Automação de Processos** - Pipelines eficientes e deploy contínuo
- **Containerização** - Docker para ambientes consistentes
- **Deploy na Nuvem** - Google Cloud Run para aplicações escaláveis
- **Monitoramento e Observabilidade** - Práticas para aplicações em produção

### Por que DevOps?
- ✅ **Redução de falhas** em produção
- ✅ **Escalabilidade** com segurança
- ✅ **Entrega contínua** de valor ao cliente
- ✅ **Automação** de processos repetitivos

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ❤️ Agradecimentos e Créditos 

**Este projeto foi adaptado da Imersão Cloud DevOps**

- **Alura:** [https://www.alura.com.br](https://www.alura.com.br)
- **Google Cloud:** [https://cloud.google.com](https://cloud.google.com)

## 📞 Contato

Desenvolvido por Alan de O. Gonçalves baseado no projeto feito durante a imersão.

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alan-oliveir)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alan-ogoncalves)
---

⭐ **Se este projeto te ajudou, considere dar uma estrela no repositório!**
