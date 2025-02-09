from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..Models.Base import Base


class LinkUserAndGroup(Base):
    __tablename__ = "LinkUserAndGroup"

    id_user = Column(Integer, ForeignKey("Utente.id_user", ondelete="CASCADE"), nullable=False, primary_key=True)
    id_group = Column(Integer, ForeignKey("Gruppo.id_group", ondelete="CASCADE"), nullable=False)

    users = relationship("Utente", back_populates="groups")
    groups = relationship("Gruppo", back_populates="users")

    def __init__(self, id_user: int, id_group: int):
        super().__init__()
        self.id_user = id_user
        self.id_group = id_group

    def __repr__(self):
        return f"{self.id_user} {self.id_group}"
