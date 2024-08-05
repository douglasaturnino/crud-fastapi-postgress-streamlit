"""
Obtem um produto com atributos como nome, descrição, preço, categoria e email do fornecedor.

Methods:
    show_response_message(response): Exibe uma mensagem baseada no status da resposta HTTP.
                                                        Se o status da resposta for 200, exibe uma mensagem de sucesso.
                                                        Caso contrário, exibe uma mensagem de erro com base no conteúdo da resposta.

    mostrar_mensagem_sucesso(): Exibe uma mensagem de sucesso no Streamlit.
                                Utilizado para informar ao usuário que a operação foi realizada com sucesso.

    mostrar_mensagem_erro(response): Exibe uma mensagem de erro no Streamlit baseada na resposta HTTP.
                                                        Se a resposta contiver um erro detalhado, essa função irá extrair e exibir as mensagens de erro.
                                                        Se a resposta não puder ser decodificada, exibe uma mensagem de erro genérica.

    mostrar_erro_detalhado(data): Exibe uma mensagem de erro detalhada no Streamlit.
                                        Se o detalhe do erro for uma lista, exibe cada mensagem de erro em uma nova linha.
                                        Caso contrário, exibe o detalhe do erro diretamente.

    adicionar_produto(name,description,price,categoria,email_fornecedor): Envia uma requisição para adicionar um novo produto.

    visualizar_produtos():  Envia uma requisição para obter a lista de todos os produtos.

    obter_detalhes_do_produto(id_produto):  Envia uma requisição para obter os detalhes de um produto específico.

    deletar_produto(id_produto): Envia uma requisição para deletar um produto específico.

    atualizar_produto(id_produto, dados_atualizados): Envia uma requisição para atualizar um produto específico.

"""

import requests
import streamlit as st


def show_response_message(response: requests.Response) -> None:
    """
    Exibe uma mensagem baseada no status da resposta HTTP.
    Se o status da resposta for 200, exibe uma mensagem de sucesso.
    Caso contrário, exibe uma mensagem de erro com base no conteúdo da resposta.

    Args:
        response (requests.Response): A resposta HTTP da requisição.
    """
    if response.status_code == 200:
        mostrar_mensagem_sucesso()
    else:
        mostrar_mensagem_erro(response)


def mostrar_mensagem_sucesso() -> None:
    """
    Exibe uma mensagem de sucesso no Streamlit.

    Utilizado para informar ao usuário que a operação foi realizada com sucesso.
    """
    st.success("Operação realizada com sucesso!")


def mostrar_mensagem_erro(response: requests.Response) -> None:
    """
    Exibe uma mensagem de erro no Streamlit baseada na resposta HTTP.
    Se a resposta contiver um erro detalhado, essa função irá extrair e exibir as mensagens de erro.
    Se a resposta não puder ser decodificada, exibe uma mensagem de erro genérica.

    Args:
        response (requests.Response): A resposta HTTP da requisição.
    """
    try:
        data = response.json()
        if "detail" in data:
            mostrar_erro_detalhado(data)
    except ValueError:
        st.error("Erro desconhecido. Não foi possível decodificar a resposta.")


def mostrar_erro_detalhado(data: dict) -> None:
    """
    Exibe uma mensagem de erro detalhada no Streamlit.
    Se o detalhe do erro for uma lista, exibe cada mensagem de erro em uma nova linha.
    Caso contrário, exibe o detalhe do erro diretamente.

    Args:
        data (dict): Dados JSON contendo detalhes do erro.
    """
    if isinstance(data["detail"], list):
        errors = "\n".join([error["msg"] for error in data["detail"]])
        st.error(f"Erro: {errors}")
    else:
        st.error(f"Erro: {data['detail']}")


def adicionar_produto(
    name: str,
    description: str,
    price: str,
    categoria: str,
    email_fornecedor: str,
) -> requests.Response:
    """
    Envia uma requisição para adicionar um novo produto.

    Args:
        name (str): Nome do produto.
        description (str): Descrição do produto.
        price (float): Preço do produto.
        categoria (str): Categoria do produto.
        email_fornecedor (str): Email do fornecedor do produto.

    Returns:
        response(requests.Response): A resposta HTTP da requisição.
    """
    response = requests.post(
        "http://backend:8000/products/",
        json={
            "name": name,
            "description": description,
            "price": price,
            "categoria": categoria,
            "email_fornecedor": email_fornecedor,
        },
    )
    return response


def visualizar_produtos() -> requests.Response:
    """
    Envia uma requisição para obter a lista de todos os produtos.

    Returns:
        response(requests.Response): A resposta HTTP da requisição.
    """
    response = requests.get("http://backend:8000/products/")
    return response


def obter_detalhes_do_produto(id_produto: str) -> requests.Response:
    """
    Envia uma requisição para obter os detalhes de um produto específico.

    Args:
        id_produto (str): ID do produto para obter detalhes.

    Returns:
        response(requests.Response): A resposta HTTP da requisição.
    """
    response = requests.get(f"http://backend:8000/products/{id_produto}")
    return response


def deletar_produto(id_produto: str) -> requests.Response:
    """
    Envia uma requisição para deletar um produto específico.

    Args:
        id_produto (str): ID do produto a ser deletado.

    Returns:
        response(requests.Response): A resposta HTTP da requisição.
    """
    response = requests.delete(f"http://backend:8000/products/{id_produto}")
    return response


def atualizar_produto(id_produto: str, dados_atualizados: str) -> requests.Response:
    """
    Envia uma requisição para atualizar um produto específico.

    Args:
        id_produto (str): ID do produto a ser atualizado.
        dados_atualizados (dict): Dicionário com os dados atualizados do produto.

    Returns:
        response (requests.Response): A resposta HTTP da requisição.
    """
    response = requests.put(
        f"http://backend:8000/products/{id_produto}", json=dados_atualizados
    )
    return response
