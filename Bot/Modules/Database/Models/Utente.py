from sqlalchemy import Column, String, Integer, Boolean
from ..Models.Base import Base


class Utente(Base):
    __tablename__ = "UniqueUtente"

    id_telegram = Column("id_telegram", Integer, nullable=False, primary_key=True)
    username = Column("username", String, nullable=False)
    isAdmin = Column("isAdmin", Boolean, default=False, nullable=True)
    isVerified = Column("isVerified", Boolean, default=False, nullable=True)
    isHide = Column("isHide", Boolean, default=False, nullable=True)

    def __init__(self, id_telegram: int, username: str, isAdmin: bool, isVerified: bool, isHide: bool):
        self.id_telegram = id_telegram
        self.username = username
        self.isAdmin = isAdmin
        self.isVerified = isVerified
        self.isHide = isHide

    def __repr__(self):
        return f"{self.id_telegram} {self.username} {self.isAdmin} {self.isVerified} {self.isHide}"