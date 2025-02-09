from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from ..Models.Base import Base


class Utente(Base):
    __tablename__ = "Utente"

    id_user = Column("id_user", Integer, nullable=False, primary_key=True)
    username = Column("username", String, nullable=False)
    isAdmin = Column("isAdmin", Boolean, default=False, nullable=True)
    isVerified = Column("isVerified", Boolean, default=False, nullable=True)
    isHide = Column("isHide", Boolean, default=False, nullable=True)

    groups = relationship("LinkUserAndGroup", back_populates="users", cascade="all, delete")

    def __init__(self, id_user: int, username: str, isAdmin: bool, isVerified: bool, isHide: bool):
        super().__init__()
        self.id_user = id_user
        self.username = username
        self.isAdmin = isAdmin
        self.isVerified = isVerified
        self.isHide = isHide

    def __repr__(self):
        return f"{self.id_user} {self.username} {self.isAdmin} {self.isVerified} {self.isHide}"