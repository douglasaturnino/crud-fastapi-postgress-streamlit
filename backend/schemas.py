"""
Este módulo define modelos Pydantic para produtos com categorias e informações básicas.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    PositiveFloat,
    field_validator,
)


class CategoriaBase(Enum):
    """
    Uma enumeração que representa categorias disponíveis para produtos.

    Valores da Enum:

    - categoria1: "Eletrônico".
    - categoria2: "Eletrodoméstico".
    - categoria3: "Móveis".
    - categoria4: "Roupas".
    - categoria5: "Calçados".
    """

    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    """
    Modelo Pydantic base para informações de produto.

    Parameters:
        name (str): O nome do produto.
        description (Optional[str]): Descrição opcional do produto.
        price (PositiveFloat): O preço do produto.
        categoria (CategoriaBase): A categoria do produto.
        email_fornecedor (EmailStr): Email do fornecedor do produto.

    Methods:
        check_categoria(cls, v): Método validador que garante que o valor da categoria seja válido.
    """

    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: CategoriaBase
    email_fornecedor: EmailStr

    @field_validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

    class Config:
        use_enum_values = True


class ProductCreate(ProductBase):
    """
    Modelo Pydantic para criação de novos produtos, que herda de ProductBase.
    """

    pass


class ProductResponse(ProductBase):
    """
    Modelo Pydantic para responder com informações de produto.

    Parameters:
        id (int): O identificador único do produto.
        created_at (datetime): Data e hora de criação do produto.
    """

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    """
    Modelo Pydantic para atualização de informações de produtos existentes.

    Parameters:
        name (Optional[str]): Nome atualizado do produto.
        description (Optional[str]): Descrição atualizada do produto.
        price (Optional[PositiveFloat]): Preço atualizado do produto.
        categoria (Optional[CategoriaBase]): Categoria atualizada do produto.
        email_fornecedor (Optional[EmailStr]): Email do fornecedor atualizado do produto.

    Methods:
        check_categoria(cls, v): Método validador que garante que o valor da categoria seja válido.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[CategoriaBase] = None
    email_fornecedor: Optional[EmailStr] = None

    @field_validator("categoria")
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

    class Config:
        use_enum_values = True
