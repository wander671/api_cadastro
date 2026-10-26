# API de Cadastro

API REST de cadastro de usuários, feita em Python com Flask e PostgreSQL.

## Tecnologias

- Python 3.14
- Flask 3.0.2
- PostgreSQL 18
- psycopg2-binary 2.9.13
- python-dotenv 1.0.1

## Como rodar

1. Crie e ative o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Instale as dependências:

```powershell
pip install -r requirements.txt
```

3. Copie `.env.example` para `.env` e preencha com seus dados.

4. Crie o banco `api_cadastro_db` e a tabela `usuarios` no PostgreSQL.

5. Teste a conexão:

```powershell
python teste_conexao.py
```

6. Ligue o servidor:

```powershell
python app.py
```

A API fica disponível em `http://127.0.0.1:5000`.

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Confirma que a API está funcionando |

## Status

- [x] Ambiente e dependências
- [x] Conexão com o PostgreSQL
- [x] Tabela `usuarios`
- [x] Rota inicial `GET /`
- [ ] Rota `POST /usuarios`
- [ ] Rotas de listar, buscar, atualizar e remover