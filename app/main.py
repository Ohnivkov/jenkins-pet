import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from pathlib import Path


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI(title="FastAPI Pet UI ")

templates = Jinja2Templates(directory="/app/templates")


def get_db():
    connection = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    try:
        yield connection
    finally:
        connection.close()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db=Depends(get_db)):
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT 1;")
            db_status = "CONNECTED"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"

    return templates.TemplateResponse(
        name="index.html", 
        request=request,
        context={"status": db_status}
    )


@app.post("/api/records")
async def add_record(db=Depends(get_db)):
    return {"status": "success", "message": "Record added successfully"}