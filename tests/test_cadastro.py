
# ==========================================
# IMPORTAÇÕES
# ==========================================

from playwright.sync_api import expect
import uuid


# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================

def preencher_formulario(page, nome, idade, data_nascimento):
    page.locator("#nome").fill(nome)
    page.locator("#idade").fill(idade)
    page.locator("#dataNascimento").fill(data_nascimento)


def aceitar_alerta(page):
    page.on("dialog", lambda dialog: dialog.accept())


# ==========================================
# TESTE 1 - CADASTRO COM DADOS VÁLIDOS
# ==========================================

def test_cadastrar_pessoa_com_dados_validos(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Gera um nome exclusivo para o teste
    nome = f"Teste QA {uuid.uuid4().hex[:8]}"

    # Preenche os campos usando a função auxiliar
    preencher_formulario(page, nome, "30", "1995-05-15")

    # Configura a aceitação automática do alerta
    aceitar_alerta(page)

    # Clica no botão salvar
    page.locator("#botaoSalvar").click()

    # Verifica se o nome aparece na tabela
    expect(page.locator("#tabelaPessoas")).to_contain_text(nome)


# ==========================================
# TESTE 2 - IMPEDIR CADASTRO SEM NOME
# ==========================================

def test_impedir_cadastro_sem_nome(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Conta os registros existentes antes da tentativa
    quantidade_inicial = page.locator("#tabelaPessoas tr").count()

    # Preenche os campos, deixando o nome vazio
    preencher_formulario(page, "", "30", "1995-05-15")

    # Configura a aceitação automática do alerta
    aceitar_alerta(page)

    # Tenta salvar
    page.locator("#botaoSalvar").click()

    # Conta os registros depois da tentativa
    quantidade_final = page.locator("#tabelaPessoas tr").count()

    # Verifica se nenhum registro foi criado
    assert quantidade_final == quantidade_inicial


# ==========================================
# TESTE 3 - IMPEDIR CADASTRO DUPLICADO
# ==========================================

def test_impedir_cadastro_duplicado(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Gera um nome exclusivo para o teste
    nome = f"Duplicado QA {uuid.uuid4().hex[:8]}"

    # Primeiro cadastro: deve ser permitido
    preencher_formulario(page, nome, "32", "1994-07-20")
    aceitar_alerta(page)

    page.locator("#botaoSalvar").click()

    # Confirma que o primeiro cadastro foi realizado
    expect(page.locator("#tabelaPessoas")).to_contain_text(nome)

    # Guarda a quantidade de registros
    quantidade_inicial = page.locator("#tabelaPessoas tr").count()

    # Segunda tentativa: mesmos dados
    preencher_formulario(page, nome, "32", "1994-07-20")

    page.locator("#botaoSalvar").click()

    # Conta novamente os registros
    quantidade_final = page.locator("#tabelaPessoas tr").count()

    # Verifica se a duplicidade foi impedida
    assert quantidade_final == quantidade_inicial

# ==========================================
# TESTE 4 - IMPEDIR CADASTRO COM IDADE INVÁLIDA
# ==========================================

def test_impedir_cadastro_com_idade_acima_do_limite(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Conta os registros antes da tentativa
    quantidade_inicial = page.locator("#tabelaPessoas tr").count()

    # Preenche o formulário com idade inválida
    nome = f"Idade QA {uuid.uuid4().hex[:8]}"
    preencher_formulario(page, nome, "200", "1995-05-15")

    # Configura a aceitação automática do alerta
    aceitar_alerta(page)

    # Tenta salvar
    page.locator("#botaoSalvar").click()

    # Conta os registros depois da tentativa
    quantidade_final = page.locator("#tabelaPessoas tr").count()

    # Verifica se o cadastro foi impedido
    assert quantidade_final == quantidade_inicial


# ==========================================
# TESTE 5 - PERMITIR CADASTRO COM IDADE MÁXIMA
# ==========================================

def test_permitir_cadastro_com_idade_maxima(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Gera um nome exclusivo
    nome = f"Limite QA {uuid.uuid4().hex[:8]}"

    # Preenche o formulário com idade 150
    preencher_formulario(page, nome, "150", "1995-05-15")

    # Configura a aceitação automática do alerta
    aceitar_alerta(page)

    # Tenta salvar
    page.locator("#botaoSalvar").click()

    # Verifica se o cadastro foi realizado
    expect(page.locator("#tabelaPessoas")).to_contain_text(nome)


# ==========================================
# TESTE 6 - PERMITIR CADASTRO COM IDADE ZERO
# ==========================================

def test_permitir_cadastro_com_idade_zero(page):

    # Acessa a aplicação
    page.goto("http://localhost:3000")

    # Gera um nome exclusivo
    nome = f"Idade Zero QA {uuid.uuid4().hex[:8]}"

    # Preenche o formulário com idade zero
    preencher_formulario(page, nome, "0", "2026-01-15")

    # Configura a aceitação automática do alerta
    aceitar_alerta(page)

    # Tenta salvar
    page.locator("#botaoSalvar").click()

    # Verifica se o cadastro foi realizado
    expect(page.locator("#tabelaPessoas")).to_contain_text(nome)
