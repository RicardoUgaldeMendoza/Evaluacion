from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:1234@localhost/paquexpress_db"
motor = create_engine(DATABASE_URL)
SesionLocal = sessionmaker(bind=motor, autocommit=False, autoflush=False)
Base = declarative_base()

def obtener_bd():
    bd = SesionLocal()
    try:
        yield bd
    finally:
        bd.close()