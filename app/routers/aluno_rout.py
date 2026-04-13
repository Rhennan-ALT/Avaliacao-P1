from fastapi import APIRouter
from bson import ObjectId
from database import alunos_collection
from app.schemas.aluno_sch import *
from app.services.aluno_serv import novo_aluno_service

router = APIRouter(tags=["Insert de Alunos"])

@router.post("/aluno")
def novo_aluno(aluno: Aluno):
    return novo_aluno_service(aluno)