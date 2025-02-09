from sqlalchemy import Column, String, Boolean
from ..Models.Base import Base


class Aula(Base):
    __tablename__ = "Aula"

    nome = Column("nome", String, primary_key=True, nullable=False)

    stato = Column("stato", Boolean, default=False, nullable=False)

    def __init__(self, nome: str, stato: bool):
        super().__init__()
        self.nome = nome
        self.stato = stato

    def __repr__(self):
        return f"{self.nome} {self.stato}"
