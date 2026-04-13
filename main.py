from fastapi import FastAPI
from app.routers.aluno_rout import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"Insert dos Dados da Colletion"}