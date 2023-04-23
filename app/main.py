import psycopg2
from decouple import config
import time

print("Inicializando ...")
time.sleep(10)
try:
    conn = psycopg2.connect(
        dbname=config("POSTGRES_DB", default="my_database"),
        user=config("POSTGRES_USER", default="postgres_user"),
        password=config("POSTGRES_PASSWORD", default="postgres_password"),
        host=config("POSTGRES_HOST", default="postgres_db")
    )
    print("Conexão OK!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

try:
    cur = conn.cursor()
    print("Cursor OK!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")