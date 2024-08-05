"""
Módulo de rotas FastAPI para operações CRUD de produtos.

Este módulo define rotas HTTP para criar, ler, atualizar e deletar produtos
no banco de dados utilizando o framework FastAPI e SQLAlchemy.

Methods:
    create_product_route: Cria um novo produto no banco de dados.
    detele_product: Deleta um produto do banco de dados com base no ID fornecido.
    read_all_products: Retorna todos os produtos presentes no banco de dados.
    read_one_product: Retorna um produto específico com base no ID fornecido.
    update_product_route: Atualiza um produto existente com base no ID fornecido.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()


@router.post("/products/", response_model=ProductResponse)
def create_product_route(
    product: ProductCreate, db: Session = Depends(get_db)
) -> ProductResponse:
    """
    Cria um novo produto no banco de dados.

    Args:
        product (ProductCreate): Dados do produto a ser criado.
        db (Session, optional): Sessão do banco de dados SQLAlchemy. Defaults to Depends(get_db).

    Returns:
        ProductResponse: Objeto representando o produto criado.
    """
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)) -> ProductResponse:
    """
    Retorna todos os produtos presentes no banco de dados.

    Args:
        db (Session, optional): Sessão do banco de dados SQLAlchemy. Defaults to Depends(get_db).

    Returns:
        List[ProductResponse]: Lista de objetos representando todos os produtos no banco de dados.
    """
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    """
    Retorna um produto específico com base no ID fornecido.

    Args:
        product_id (int): ID do produto a ser recuperado.
        db (Session, optional): Sessão do banco de dados SQLAlchemy. Defaults to Depends(get_db).

    Returns:
        ProductResponse: Objeto representando o produto recuperado.

    Raises:
        HTTPException: Se o produto com o ID especificado não for encontrado.
    """
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductResponse)
def detele_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    """
    Deleta um produto do banco de dados com base no ID fornecido.

    Args:
        product_id (int): ID do produto a ser deletado.
        db (Session, optional): Sessão do banco de dados SQLAlchemy. Defaults to Depends(get_db).

    Returns:
        ProductResponse: Objeto representando o produto deletado.

    Raises:
        HTTPException: Se o produto com o ID especificado não for encontrado.
    """
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
) -> ProductResponse:
    """
    Atualiza um produto existente com base no ID fornecido.

    Args:
        product_id (int): ID do produto a ser atualizado.
        product (ProductUpdate): Dados do produto a serem atualizados.
        db (Session, optional): Sessão do banco de dados SQLAlchemy. Defaults to Depends(get_db).

    Returns:
        ProductResponse: Objeto representando o produto atualizado.

    Raises:
        HTTPException: Se o produto com o ID especificado não for encontrado.
    """
    db_product = update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
