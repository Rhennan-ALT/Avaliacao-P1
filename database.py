from pymongo import MongoClient

MONGO_URL = "mongo://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["escola"]
alunos_colletion = db["alunos"] 