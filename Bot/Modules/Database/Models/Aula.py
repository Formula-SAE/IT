from sqlalchemy import Column, String, Boolean
from ..Models.Base import Base

class Aula(Base):
    __tablename__ = "Aula"

    nome_aula = Column("nome_aula", String, primary_key=True, nullable=False)
    
    stato_aula = Column("stato_aula", Boolean, default=False, nullable=False)

    def __init__(self, nome_aula: String, stato_aula: bool):
        self.nome_aula = nome_aula
        self.stato_aula = stato_aula

    def __repr__(self):
        return f"{self.nome_aula} {self.stato_aula}"