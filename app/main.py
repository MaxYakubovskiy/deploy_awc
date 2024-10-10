import uvicorn
from fastapi import FastAPI
from asyncpg import connect, Connection

app = FastAPI()

async def check_db_connection() -> str:
    conn: Connection = await connect(
        user='myuser',
        password='root',
        database='mydb',
        host='localhost'
    )

    await conn.close()
    return "Database connected successfully"

@app.get("/")
async def read_root():
    db_status = await check_db_connection()
    return {"message": "Hello, World!", "db_status": db_status}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)