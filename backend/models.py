from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base
from enum import Enum


class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductModel(Base):
    """
    Modelo SQLAlchemy para a entidade de produtos.

    Esta classe representa um produto armazenado no banco de dados.

    Parameters:
        id (int): Identificador único do produto.
        name (str): Nome do produto.
        description (str): Descrição do produto.
        price (float): Preço do produto.
        categoria (str): Categoria do produto, escolhida a partir de `CategoriaBase`.
        email_fornecedor (str): E-mail do fornecedor do produto.
        created_at (DateTime): Data e hora de criação do registro, definido automaticamente.

    Methods:
        __repr__():
            Retorna uma representação de string do objeto `ProductModel`.
    """

    __tablename__ = "products"  # esse será o nome da tabela
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"<Product(categoria={self.categoria})>"
