from database import alunos_collection
from bson import ObjectId

def novos_alunos(aluno_dict):
    return alunos_collection.insert_one(aluno_dict)