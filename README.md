# 🐢 TurtleSteps — To-Do List

Aplicação web de lista de tarefas com sistema de cadastro e login de usuários, desenvolvida com Python e Flask.

## 📋 Funcionalidades

- Cadastro de usuário com email e senha
- Login com autenticação segura (senha criptografada)
- Sessão de usuário — cada pessoa vê apenas suas próprias tarefas
- Adicionar tarefas com título, descrição e data limite
- Marcar tarefa como concluída ou reabrir
- Deletar tarefa
- Contador de tarefas pendentes e concluídas
- Logout

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Flask** — framework web
- **SQLite** — banco de dados
- **Werkzeug** — criptografia de senhas
- **Jinja2** — templates HTML
- **HTML + CSS** — interface

## 📁 Estrutura do projeto

```
projetoSite/
├── main.py                  # Rotas e lógica principal
├── Procfile                 # Configuração para deploy
├── requirements.txt         # Dependências do projeto
├── database.db              # Banco de dados SQLite
├── models/
│   ├── user.py              # Model de usuários
│   └── task.py              # Model de tarefas
├── templates/
│   ├── index.html           # Página inicial / cadastro
│   ├── login.html           # Tela de login
│   └── tarefas.html         # Tela principal de tarefas
└── static/
    ├── css/style.css        # Estilos
    └── img/                 # Imagens
```

## ▶️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Rode a aplicação**
```bash
python main.py
```

**5. Acesse no navegador**
```
http://localhost:5000
```

## 👨‍💻 Autor

Desenvolvido por Miguel Perino — projeto de aprendizado com Python e Flask.
