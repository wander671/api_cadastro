from app import get_db_connection

conn = get_db_connection()

if conn is None:
    print("Falhou: veja a mensagem de erro acima.")
else:
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print("Conectado com sucesso!")
    print(cursor.fetchone()[0])
    cursor.close()
    conn.close()
