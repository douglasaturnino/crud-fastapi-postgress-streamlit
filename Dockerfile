FROM squidfunk/mkdocs-material:latest

COPY . .

RUN pip install mkdocs-autorefs mkdocs-gen-files mkdocstrings-python mkdocs-material


