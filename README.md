# Projeto saucedemo

Este projeto consiste em usar o Python, Selenium e Pytest para testar algumas funcionalidades do site "https://www.saucedemo.com/", como o login, adicionar item no carrinho e finalizar uma compra.

O que é necessário ter instalado: 
- Python
- Pycharm

Após baixar o projeto e abri-lo no Pycharm, use o comando "python -v venv venv" no terminal para garantir a criação do ambiente virtual (caso ainda não esteja criado), e use o comando "venv\Scripts\Activate.ps1" para entrar no ambiente virtual. A partir disso, faça as seguintes instalações:
- Instale o selenium com o comando "pip install selenium"
- Instale o pytest com o comando "pip install -U pytest"
- Instale o plugin de relatório com o comando "pip install pytest-html"

Agora você já pode rodar os testes. Para isso, use os seguintes comandos: 

- Para testar apenas a funcionalidade de login, acesse o terminal e use o seguinte comando: pytest -v tests/test_login.py
- Para testar apenas a funcionalidade de adicionar ao carrinho, acesse o terminal e use o seguinte comando: pytest -v tests/test_add_to_cart.py
- Para testar a funcionalidade de fechar a compra, acesse o terminal e use o seguinte comando: pytest -v tests/test_finish_order.py::TestCT03

Para gerar o relatório com o resultado de todos os testes, use o comando "pytest --html=report.html". Será gerado um arquivo "report.html" com os resultados na raiz do projeto. 
