import os
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env (Segurança de credenciais)
load_dotenv()

# Inicializa a aplicação Flask
app = Flask(__name__)

def get_db_connection():
    """
    Abre uma conexão com o PostgreSQL usando as variáveis de ambiente para configuração do banco de dados.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "sistema_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None