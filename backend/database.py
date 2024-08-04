"""
Módulo de Configuração do Banco de Dados

Este módulo configura a conexão com o banco de dados e fornece uma função para obter uma sessão de banco de dados.

Methods:
    get_db: Função para fornecer uma sessão de banco de dados para ser utilizada dentro de um contexto.
            Garante o gerenciamento adequado da sessão fechando-a após o uso.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> sessionmaker:
    """
    Função para fornecer uma sessão de banco de dados para ser utilizada dentro de um contexto.
            Garante o gerenciamento adequado da sessão fechando-a após o uso.

    Yields:
        db: Uma sessionmaker do SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
