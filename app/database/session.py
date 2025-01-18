import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLITE_URL = os.getenv('SQLITE_URL')
engine = create_engine(SQLITE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)