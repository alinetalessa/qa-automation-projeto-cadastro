# QA Automation - Projeto Cadastro

## Sobre o projeto

Projeto de automação de testes funcionais de uma aplicação web de cadastro de pessoas, utilizando Python, Pytest e Playwright.

O objetivo é validar os principais fluxos de cadastro e regras de negócio da aplicação.

## Tecnologias utilizadas

- Python
- Pytest
- Playwright
- pytest-html

## Cenários automatizados

- Cadastro de pessoa com dados válidos.
- Impedir cadastro sem nome.
- Impedir cadastro duplicado.
- Impedir cadastro com idade acima do limite permitido.
- Permitir cadastro com idade máxima (150 anos).
- Permitir cadastro com idade zero.

## Como executar o projeto

1. Clone este repositório.
2. Crie e ative um ambiente virtual.
3. Instale as dependências:

   pip install -r requirements.txt

4. Instale o navegador Chromium:

   playwright install chromium

5. Inicie a aplicação web na porta 3000.
6. Execute os testes:

   pytest -v

## Gerar relatório HTML

Execute:

   pytest -v --html=reports/relatorio.html --self-contained-html

O relatório apresenta os resultados da execução dos testes automatizados.
