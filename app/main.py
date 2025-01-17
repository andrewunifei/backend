from database.session import Session, engine
from database import models

def test_conn():
    db = Session()
    filme = db.query(models.Filme).filter(models.Filme.id == '1').first()
    return filme.titulo

if __name__ == '__main__':
    titulo_filme = test_conn()
    print(titulo_filme)