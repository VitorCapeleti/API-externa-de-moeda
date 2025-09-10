# 🪙 ConsumirAPI - Dashboard de Criptomoedas

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31-orange?style=for-the-badge)

Um dashboard web simples desenvolvido em Python com o micro-framework Flask. A aplicação consome em tempo real os dados de uma API externa de criptomoedas e os exibe de forma organizada e amigável.

![Print da Aplicação](httpsd://i.imgur.com/link-para-seu-print.png)

---

### 📋 Índice

-   [✨ Funcionalidades](#-funcionalidades)
-   [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
-   [📂 Estrutura do Projeto](#-estrutura-do-projeto)
-   [🚀 Como Executar o Projeto](#-como-executar-o-projeto)
-   [📝 Arquitetura](#-arquitetura)
-   [📜 Licença](#-licença)

---

### ✨ Funcionalidades

-   **Consumo de API Externa:** Busca dados atualizados de criptomoedas.
-   **Interface Web Dinâmica:** Exibe as informações em uma tabela limpa e organizada.
-   **Estrutura MVC-like:** Código organizado em camadas (Model, View, Controller) para fácil manutenção.
-   **Ambiente Virtual:** Utiliza um ambiente virtual para isolar as dependências do projeto.

---

### 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

-   **[Python 3.10](https://www.python.org/)**: Linguagem principal do back-end.
-   **[Flask](https://flask.palletsprojects.com/)**: Micro-framework web para criação da aplicação e rotas.
-   **[Requests](https://requests.readthedocs.io/)**: Biblioteca para realizar as requisições HTTP para a API externa.
-   **[Jinja2](https://jinja.palletsprojects.com/)**: Motor de templates para renderizar o HTML (integrado ao Flask).
-   **HTML5** e **CSS3**: Para a estrutura e estilização da interface.

---

### 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma para manter a separação de responsabilidades:

```
├── app.py                # Ponto de entrada da aplicação Flask
├── views.py              # (Controller) Define as rotas e a lógica de apresentação
├── controller/
│   └── listInfos.py      # Orquestra a busca de dados
├── api/
│   └── dataCoin.py       # (Model) Lógica de acesso e consumo da API externa
├── templates/
│   └── index.html        # (View) Template HTML que exibe os dados
├── static/
│   └── style.css         # Arquivo de estilos da aplicação
├── venv/                 # Ambiente virtual (ou bin/, lib/, etc.)
└── requirements.txt      # Lista de dependências para instalação
```

---

### 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em seu ambiente local.

#### Pré-requisitos

-   Python 3.10 ou superior
-   Git (para clonar o repositório)

#### Passos para Instalação

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/seu-usuario/ConsumirAPI.git](https://github.com/seu-usuario/ConsumirAPI.git)
    cd ConsumirAPI
    ```
    *(Lembre-se de substituir `seu-usuario` pelo seu nome de usuário no GitHub)*

2.  **Crie e ative um ambiente virtual:**
    *É uma boa prática criar um novo ambiente virtual em vez de usar o que está no repositório.*
    ```sh
    # Criar o ambiente
    python -m venv venv

    # Ativar no Linux/macOS
    source venv/bin/activate

    # Ativar no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    *O arquivo `requirements.txt` contém todas as bibliotecas necessárias.*
    ```sh
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```sh
    flask run
    ```
    *Alternativamente, você pode executar diretamente o arquivo principal:*
    ```sh
    python app.py
    ```

5.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:5000](http://localhost:5000).

---

### 📝 Arquitetura

A aplicação segue um fluxo de dados inspirado no padrão Model-View-Controller (MVC):

1.  **Requisição do Usuário:** O navegador acessa a rota principal (`/`).
2.  **View (`views.py`):** O `views.py` (atuando como **Controller**) intercepta a requisição. Ele não contém a lógica de busca de dados, apenas orquestra a chamada.
3.  **Controller (`controller/listInfos.py`):** A função em `views.py` chama o `controller`, que por sua vez solicita os dados.
4.  **Model (`api/dataCoin.py`):** O `dataCoin.py` (atuando como **Model**) é o responsável por fazer a chamada real à API externa, tratar os dados brutos e retorná-los de forma estruturada.
5.  **Renderização:** Com os dados em mãos, a função em `views.py` os envia para o template `index.html` (**View**), que os renderiza para o usuário final.

---

### 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
> Desenvolvido por [Vitor Capeleti Gomes]