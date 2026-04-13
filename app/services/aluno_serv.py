from app.repositories.aluno_repo import novos_alunos
from bson import ObjectId

def novo_aluno_service(aluno):
    res = novos_alunos(aluno.model_dump())
    return {"Mensage": "Novo Aluno Adicionado com Sucesso...", "id": str(res.inserted_id)}