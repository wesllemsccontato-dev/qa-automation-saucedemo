# QA Automation - SauceDemo

Projeto de automação de testes utilizando Python, Selenium WebDriver e Pytest.

## Objetivo

Demonstrar conhecimentos em:

- Estrutura baseada em Page Object Model (POM)
- Automação de cenários funcionais, negativos e de segurança
- Controle de sessão e autenticação
- Organização de dados de teste em módulos reutilizáveis
- Integração com Git e GitHub
- Execução automatizada de suíte de testes com Pytest

## Aplicação Testada

https://www.saucedemo.com/

## Cenários Automatizados

Autenticação
-  CT-001 - Login válido
- CT-002 - Login inválido
- CT-003 - Usuário inválido
- CT-013 - Campos obrigatórios vazios
- CT-018 - Sensibilidade da senha (case sensitive)
- CT-056 - Login pressionando ENTER

Controle de Sessão
- CT-040 - Acesso sem autenticação
- T-042 - Botão voltar após logout
- CT-046 - URL direta após logout
- CT-115 - Atualizar página logado

Segurança
- CT-053 - Scripts maliciosos (XSS)

## Tecnologias

- Python
- Selenium
- Pytest
- Git
- GitHub



## Estatísticas do Projeto

Total de testes automatizados: 11
Testes aprovados: 11
Taxa de sucesso: 100%
Framework: Pytest
Automação: Selenium WebDriver
Linguagem: Python
Padrão de projeto: Page Object Model (POM)

## Autor

Wesllem S. Campos
