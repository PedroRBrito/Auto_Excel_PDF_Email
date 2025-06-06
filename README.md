# Gerador de Relatórios PDF com Envio de E-mail

Este projeto é uma aplicação desktop desenvolvida em Python para automatizar a geração de relatórios em PDF a partir de planilhas Excel e enviá-los por e-mail.

O programa utiliza uma interface gráfica construída com PySide2, facilitando a interação do usuário e eliminando a necessidade de operar via linha de comando.

---

## Funcionalidades

* **Carregar Planilhas Excel:** Permite carregar arquivos `.xlsx` para extrair os dados.
    * **Nota:** O sistema é otimizado para planilhas pequenas e bem formatadas.
* **Gerar Relatórios PDF:** Cria um relatório em PDF com base nos dados da planilha e em um texto principal fornecido pelo usuário.
* **Enviar E-mail com PDF:** Anexa o relatório gerado a um e-mail e o envia para um destinatário especificado.
* **Histórico de Envios:** Exibe um registro dos relatórios enviados.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface Gráfica:** PySide2 (Qt for Python)
* **Manipulação de Dados:** Pandas & Openpyxl
* **Geração de PDF:** ReportLab
* **Gerenciamento de Dependências:** Poetry
* **Variáveis de Ambiente:** Python-Dotenv

---

## Pré-requisitos e Instalação

1.  **Python:** Certifique-se de que o [Python 3.10](https://www.python.org/downloads/) ou superior está instalado.
2.  **Poetry:** Instale o Poetry, que gerenciará as dependências do projeto.
    ```bash
    pip install poetry
    ```
3.  **Instalar Dependências:** Clone este repositório e, dentro da pasta do projeto, execute o comando abaixo para instalar todas as bibliotecas necessárias.
    ```bash
    poetry install
    ```
---

## Configuração e Uso

### 1. Configuração do E-mail

**⚠️ ATENÇÃO: A autenticação do Google mudou!**

O método de "Acesso a apps menos seguros" foi descontinuado pelo Google. Para que o envio de e-mail funcione, você **precisa** usar uma **"Senha de App"**.

1.  **Ative a Verificação em Duas Etapas** na sua Conta do Google.
2.  Acesse a seção [Senhas de app](https://myaccount.google.com/apppasswords) da sua conta.
3.  Gere uma nova senha. Selecione "E-mail" como o app e "Computador Windows/Mac" como o dispositivo.
4.  O Google fornecerá uma senha de 16 caracteres. Copie esta senha.

### 2. Crie o Arquivo `.env`

Na pasta raiz do projeto, crie um arquivo chamado `.env` e adicione as seguintes informações:

```env
EMAIL_REMETENTE="seuemail@gmail.com"
SENHA_REMETENTE="sua_senha_de_app_de_16_caracteres"
```
## Como Usar o Programa

1.  **Configurar Credenciais:**
    * Crie um arquivo com nome `.env` na pasta raiz, fora de `/src`, com a seguinte estrutura:
    ```
    EMAIL_REMETENTE=seuemail@gmail.com
    SENHA_REMETENTE=suasenha
    ```
    * No arquivo `.env`, substitua `seuemail@gmail.com` pelo seu endereço do Gmail.
    * Substitua `sua_senha_de_app_de_16_caracteres` pela senha de aplicativo de 16 caracteres gerada na sua conta Google.

2.  **Execução e Passos:**
    * Execute o arquivo principal do projeto: `main.py`.
    * **Carregar Arquivo:** Clique no botão e selecione a planilha Excel desejada.
    * **Escrever Relatório:** Insira o texto principal do relatório no campo de texto fornecido.
    * **Configurar E-mail:** Preencha os campos com o e-mail do destinatário, o título e o corpo da mensagem.
    * **Enviar Relatório:** Clique em "Enviar E-mail com PDF" para concluir a operação.

---

## Estrutura do Projeto

O código-fonte é modularizado para facilitar a manutenção e o desenvolvimento, com cada arquivo tendo uma responsabilidade clara:
```
rpa_excel_pdf_email/
├── src/
│   ├── main.py             # Ponto de entrada da aplicação
│   ├── main_window.py      # Lógica da janela principal
│   ├── interface.py        # Configuração da UI (elementos visuais)
│   ├── excel_utils.py      # Funções para manipulação do Excel
│   ├── pdf_utils.py        # Funções para criação do PDF
│   └── email_utils.py      # Funções para envio do e-mail
├── pyproject.toml          # Definições do projeto e dependências (Poetry)
└── README.md               # Documentação principal
```
