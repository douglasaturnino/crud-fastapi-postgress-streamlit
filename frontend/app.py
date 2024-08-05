"""
Aplicação Streamlit para gerenciamento de produtos.
Utiliza o Streamlit para criar uma interface de usuário interativa
para adicionar, visualizar, atualizar e deletar produtos em um backend.
"""

import pandas as pd
import streamlit as st
from produto import (
    adicionar_produto,
    atualizar_produto,
    deletar_produto,
    obter_detalhes_do_produto,
    show_response_message,
    visualizar_produtos,
)


def configurar_pagina():
    """
    Configura a página do Streamlit, incluindo o layout e a imagem do cabeçalho.
    Define o título da página como "Gerenciamento de Produtos".
    """
    st.set_page_config(layout="wide")
    st.image("logo.png", width=200)
    st.title("Gerenciamento de Produtos")


def adicionar_novo_produto():
    """
    Exibe um formulário para adicionar um novo produto.
    Coleta informações do produto, como nome, descrição, preço, categoria e email do fornecedor.
    Ao enviar o formulário, chama a função `adicionar_produto` e exibe uma mensagem de resposta.
    """
    with st.expander("Adicionar um Novo Produto"):
        with st.form("new_product"):
            name = st.text_input("Nome do Produto")
            description = st.text_area("Descrição do Produto")
            price = st.number_input("Preço", min_value=0.01, format="%f")
            categoria = st.selectbox(
                "Categoria",
                ["Eletrônico", "Eletrodoméstico", "Móveis", "Roupas", "Calçados"],
            )
            email_fornecedor = st.text_input("Email do Fornecedor")
            submit_button = st.form_submit_button("Adicionar Produto")

            if submit_button:
                response = adicionar_produto(
                    name, description, price, categoria, email_fornecedor
                )
                show_response_message(response)


def visualizar_todos_produtos():
    """
    Exibe todos os produtos em um formato tabular.
    Ao clicar no botão "Exibir Todos os Produtos", chama a função `visualizar_produtos`.
    Se a resposta for bem-sucedida, converte a resposta em um DataFrame do Pandas e a exibe.
    """
    with st.expander("Visualizar Produtos"):
        if st.button("Exibir Todos os Produtos"):
            response = visualizar_produtos()
            if response.status_code == 200:
                product = response.json()
                df = pd.DataFrame(product)
                df = df[
                    [
                        "id",
                        "name",
                        "description",
                        "price",
                        "categoria",
                        "email_fornecedor",
                        "created_at",
                    ]
                ]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)


def obter_detalhes_produto():
    """
    Exibe detalhes de um produto específico baseado no ID fornecido.
    Coleta o ID do produto do usuário e chama a função `obter_detalhes_do_produto`.
    Se a resposta for bem-sucedida, converte a resposta em um DataFrame do Pandas e a exibe.
    """
    with st.expander("Obter Detalhes de um Produto"):
        get_id = st.number_input("ID do Produto", min_value=1, format="%d")
        if st.button("Buscar Produto"):
            response = obter_detalhes_do_produto(get_id)
            if response.status_code == 200:
                product = response.json()
                df = pd.DataFrame([product])
                df = df[
                    [
                        "id",
                        "name",
                        "description",
                        "price",
                        "categoria",
                        "email_fornecedor",
                        "created_at",
                    ]
                ]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)


def deletar_produto_funcao():
    """
    Exibe um formulário para deletar um produto baseado no ID fornecido.
    Coleta o ID do produto do usuário e chama a função `deletar_produto`.
    Exibe uma mensagem de resposta após a tentativa de deleção.
    """
    with st.expander("Deletar Produto"):
        delete_id = st.number_input(
            "ID do Produto para Deletar", min_value=1, format="%d"
        )
        if st.button("Deletar Produto"):
            response = deletar_produto(delete_id)
            show_response_message(response)


def atualizar_produto_funcao():
    """
    Exibe um formulário para atualizar um produto existente.
    Coleta informações do produto, como ID, novo nome, nova descrição, novo preço, nova categoria e novo email do fornecedor.
    Ao enviar o formulário, chama a função `atualizar_produto` com os dados fornecidos e exibe uma mensagem de resposta.
    """
    with st.expander("Atualizar Produto"):
        with st.form("update_product"):
            update_id = st.number_input("ID do Produto", min_value=1, format="%d")
            new_name = st.text_input("Novo Nome do Produto")
            new_description = st.text_area("Nova Descrição do Produto")
            new_price = st.number_input(
                "Novo Preço",
                min_value=0.01,
                format="%f",
            )
            new_categoria = st.selectbox(
                "Nova Categoria",
                ["Eletrônico", "Eletrodoméstico", "Móveis", "Roupas", "Calçados"],
            )
            new_email = st.text_input("Novo Email do Fornecedor")

            update_button = st.form_submit_button("Atualizar Produto")

            if update_button:
                update_data = {}
                if new_name:
                    update_data["name"] = new_name
                if new_description:
                    update_data["description"] = new_description
                if new_price > 0:
                    update_data["price"] = new_price
                if new_email:
                    update_data["email_fornecedor"] = new_email
                if new_categoria:
                    update_data["categoria"] = new_categoria

                if update_data:
                    response = atualizar_produto(update_id, update_data)
                    show_response_message(response)
                else:
                    st.error("Nenhuma informação fornecida para atualização")


def main():
    """
    Função principal que organiza a execução das funcionalidades da aplicação.
    Configura a página e chama as funções para adicionar, visualizar, obter detalhes, deletar e atualizar produtos.
    """
    configurar_pagina()
    adicionar_novo_produto()
    visualizar_todos_produtos()
    obter_detalhes_produto()
    deletar_produto_funcao()
    atualizar_produto_funcao()


if __name__ == "__main__":
    main()
