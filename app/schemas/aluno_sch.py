from pydantic import BaseModel

class Endereco(BaseModel):
    cidade: str
    estado: str

class Aluno(BaseModel):
    nome: str
    idade: int
    curso: str
    notas: list
    endereco: Endereco