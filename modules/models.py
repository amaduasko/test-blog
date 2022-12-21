from sqlalchemy import Column,VARCHAR, DATE, TEXT, INT,BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(BIGINT, primary_key=True)
    fio = Column(TEXT)
    datar = Column(DATE)
    id_role = Column(INT)
    created_on = Column(DATE)


class Role(Base):
    __tablename__ = "roles"
    id = Column(INT, primary_key=True)
    name= Column(VARCHAR(50))
