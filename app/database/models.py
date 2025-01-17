from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    
    id = Column(Integer, primary_key=True, index=True)