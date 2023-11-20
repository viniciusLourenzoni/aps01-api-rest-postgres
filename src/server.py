from contextlib import asynccontextmanager
from fastapi import FastAPI
# from src.config.database import create_db_and_tables, get_session
# from src.models.manutencao import Manutencao
# from src.routes.manutencao_routes import manutencao_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield

app = FastAPI()

# app.include_router(manutencao_router)

@app.get("/healthcheck")
def health_check():
    return {"status": "ok"}