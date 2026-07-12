from fastapi import FastAPI
import psycopg2
import os
import time

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "devops_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mamba_mentality")


@app.get('/')
def read_root():
    try:
        conn=psycopg2.connect(host=DB_HOST, database=DB_NAME, password=DB_PASSWORD,
                              user=DB_USER,)
        conn.close()
        db_status = "Успішно підключено до PostgreSQL!)))"
    except Exception as e:
        db_status = f"Помилка підключення до БД: {str(e)}"
    return {
        "status": "Додаток працює",
        "database": db_status
    }
        
