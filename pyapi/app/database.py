import asyncpg
from fastapi import FastAPI
from contextlib import asynccontextmanager

DATABASE_URL = "postgresql://postgres:root@localhost:5432/template1"

@asynccontextmanager
async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
