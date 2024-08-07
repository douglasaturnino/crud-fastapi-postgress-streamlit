# CRUD FASTAPI POSTGRES STREAMLIT

## Instalação via Docker

Para iniciar o projeto, você pode usar Docker. Execute o seguinte comando para construir e iniciar os containers:

```bash
docker-compose up -d --build
```

### Uso

- **Frontend**: Acesse a aplicação Streamlit no endereço [http://localhost:8501](http://localhost:8501).
- **Backend**: Acesse a documentação da API FastAPI em [http://localhost:8000/docs](http://localhost:8000/docs).
- **Documentação**: Acesse a documentação do projeto em [[http://localhost:8081](http://localhost:8081)]

## Estrutura de Pastas e Arquivos

```
.
├── backend
│   ├── crud.py
│   ├── database.py
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
├── docker-compose.yml
├── docs
│   ├── backend
│   │   ├── crud.md
│   │   ├── database.md
│   │   ├── models.md
│   │   ├── router.md
│   │   └── schemas.md
│   ├── Dockerfile
│   ├── frontend
│   │   ├── app.md
│   │   └── produto.md
│   ├── gen_home_page.py
│   └── uso.md
├── frontend
│   ├── app.py
│   ├── Dockerfile
│   ├── logo.png
│   ├── produto.py
│   └── requirements.txt
├── mkdocs.yml
├── overrides
│   └── extra.css
├── poetry.lock
├── pyproject.toml
└── README.md
```

### `backend/`

Esta pasta contém todos os arquivos relacionados ao backend da aplicação, construído com FastAPI e SQLAlchemy.

- **`crud.py`**: Define as funções de CRUD (Criar, Ler, Atualizar, Deletar) para interagir com o banco de dados usando SQLAlchemy.
- **`database.py`**: Configura a conexão e a sessão do banco de dados, usando SQLAlchemy. Inclui a definição da URL de conexão e a criação de sessões.
- **`Dockerfile`**: Define a configuração do Docker para o backend, incluindo a instalação de dependências e a configuração do ambiente.
- **`main.py`**: Inicializa a aplicação FastAPI e configura o servidor Uvicorn. Define o ponto de entrada para o backend.
- **`models.py`**: Contém a definição dos modelos do SQLAlchemy, que representam as tabelas do banco de dados.
- **`requirements.txt`**: Lista as dependências Python necessárias para o backend, que serão instaladas durante a construção do Docker.
- **`router.py`**: Define as rotas da API usando FastAPI. Mapeia as URLs para funções que manipulam as requisições.
- **`schemas.py`**: Define os schemas Pydantic usados para validação e serialização dos dados da API.

### `docker-compose.yml`

Arquivo de configuração para Docker Compose, que define os serviços necessários para a aplicação, incluindo o backend, frontend e o banco de dados PostgreSQL.

### `docs/`

Esta pasta contém documentação e scripts relacionados ao projeto.

- **`backend/crud.md`**: Documentação específica sobre as operações CRUD implementadas no backend.
- **`backend/databese.md`**: Documentação específica sobre do Banco de Dados.
- **`backend/models.md`**: Documentação específica sobre SQLAlchemy para a entidade de produtos.
- **`backend/router.md`**: Documentação específica sobre as rotas FastAPI para operações CRUD de produtos.
- **`backend/schemas.md`**: Documentação específica sobre modelos Pydantic para produtos com categorias e informações básicas.
- **`frontend/app.md`**: Documentação específica sobre aplicação Streamlit
- **`frontend/produto.md`**:Documentação específica sobre o backend do produto
- **`gen_home_page.py`**: Script para gerar uma página inicial para a documentação.
- **`uso.md`**: Documentação específica para o uso do projeto.

### `frontend/`

Contém arquivos relacionados ao frontend da aplicação, desenvolvido com Streamlit.

- **`app.py`**: O ponto de entrada da aplicação Streamlit, que define a interface do usuário.
- **`produto.py`**: Módulo que interage com o backend do produto.
- **`Dockerfile`**: Define a configuração do Docker para o frontend, incluindo a instalação de dependências e configuração do ambiente.
- **`logo.png`**: Imagem do logotipo usada na interface do usuário.
- **`requirements.txt`**: Lista as dependências Python necessárias para o frontend, que serão instaladas durante a construção do Docker.

### `mkdocs.yml`

Arquivo de configuração para MkDocs, uma ferramenta para criar documentação estática de sites. Define a estrutura e o conteúdo da documentação gerada.

### `overrides/`

Contém arquivos de personalização para a documentação.

- **`extra.css`**: Arquivo CSS adicional para estilizar a documentação gerada pelo MkDocs.

### `poetry.lock`

Arquivo gerado pelo Poetry que bloqueia as versões exatas das dependências do projeto, garantindo a consistência do ambiente.

### `pyproject.toml`

Arquivo de configuração do Poetry que define as dependências do projeto, configurações e informações sobre o projeto.

### `README.md`

Documento principal do projeto que fornece uma visão geral do projeto, instruções de instalação, uso e informações adicionais.

