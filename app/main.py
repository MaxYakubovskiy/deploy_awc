import asyncio
import uvicorn
from fastapi import FastAPI
from asyncpg import connect, Connection

app = FastAPI()

async def check_db_connection() -> str:
    await asyncio.sleep(5)
    conn: Connection = await connect(
        user='myuser',
        password='root',
        database='mydb',
        host='db'
    )

    await conn.close()
    return "Database connected successfully"

@app.get("/")
async def read_root():
    db_status = await check_db_connection()
    return {"message": "Hello, World!", "db_status": db_status}