from sqlalchemy import Column, String, Integer
from ..Models.Base import Base

class Gruppo(Base):
    __tablename__ = "Gruppo"

    id_gruppo = Column("id_gruppo", Integer, primary_key=True, nullable=False)
    
    team_name = Column("team_name", String, default="", nullable=False)

    def __init__(self, id_gruppo: Integer, team_name: str):
        self.id_gruppo = id_gruppo
        self.team_name = team_name

    def __repr__(self):
        return f"{self.id_gruppo} {self.team_name}"