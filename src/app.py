from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db import create_db_and_tables
from src.routers import auth, posts


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(posts.router)
