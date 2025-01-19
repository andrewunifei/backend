from pydantic import BaseModel

class MovieIn(BaseModel):
    nome: str
    ano: int 
    diretor: str

class MovieOut(BaseModel):
    id: int
    nome: str
    ano: int 
    diretor: str