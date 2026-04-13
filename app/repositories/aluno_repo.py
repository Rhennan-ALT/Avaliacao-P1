from database import alunos_colletion
from bson import objectid

def novos_alunos(aluno_dict):
    return alunos_colletion.insert_one(aluno_dict)