from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel


def get_product(db: Session, product_id: int) -> ProductModel:
    """
    Retorna um produto específico com base no ID fornecido.

    Esta função consulta o banco de dados para recuperar um único produto com o ID correspondente.

    Args:
        db (Session): A sessão do banco de dados SQLAlchemy utilizada para interagir com o banco de dados.
        product_id (int): O ID do produto a ser recuperado.

    Returns:
        ProductModel: O objeto `ProductModel` que corresponde ao ID fornecido, ou None se não encontrado.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session) -> ProductModel:
    """
    Retorna todos os produtos presentes no banco de dados.

    Esta função consulta o banco de dados para recuperar todos os produtos armazenados.

    Args:
        db (Session): A sessão do banco de dados SQLAlchemy utilizada para interagir com o banco de dados.

    Returns:
        List[ProductModel]: Uma lista de objetos `ProductModel` representando todos os produtos no banco de dados.
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate) -> ProductModel:
    """
    Cria um novo produto e o adiciona ao banco de dados.

    Esta função cria uma instância de `ProductModel` com os dados fornecidos no objeto `ProductCreate`,
    adiciona essa instância à sessão do banco de dados, realiza o commit para persistir as alterações e
    retorna o produto criado.

    Args:
        db (Session): A sessão do banco de dados SQLAlchemy utilizada para interagir com o banco de dados.
        product (ProductCreate): O objeto contendo os dados do novo produto a ser criado.

    Returns:
        ProductModel: O objeto `ProductModel` que representa o produto recém-criado e persistido no banco de dados.
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> ProductModel:
    """
    Deleta um produto do banco de dados com base no ID fornecido.

    Esta função localiza e deleta um produto específico com o ID correspondente no banco de dados.

    Args:
        db (Session): A sessão do banco de dados SQLAlchemy utilizada para interagir com o banco de dados.
        product_id (int): O ID do produto a ser deletado.

    Returns:
        ProductModel: O objeto `ProductModel` que foi deletado, ou None se o produto não foi encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(
    db: Session, product_id: int, product: ProductUpdate
) -> ProductUpdate:
    """
    Atualiza um produto existente com base no ID fornecido.

    Esta função consulta o banco de dados para encontrar o produto com o ID correspondente e atualiza
    seus campos conforme especificado no objeto `ProductUpdate`. Após a atualização, o produto modificado
    é commitado no banco de dados.

    Args:
        db (Session): A sessão do banco de dados SQLAlchemy utilizada para interagir com o banco de dados.
        product_id (int): O ID do produto a ser atualizado.
        product (ProductUpdate): O objeto contendo os campos a serem atualizados no produto.

    Returns:
        ProductModel: O objeto `ProductModel` que foi atualizado, ou None se o produto não foi encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product
