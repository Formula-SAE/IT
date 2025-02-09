from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..Models.Base import Base


class Gruppo(Base):
    __tablename__ = "Gruppo"

    id_group = Column("id_group", Integer, primary_key=True, nullable=False)

    group_name = Column("group_name", String, default="", nullable=False)

    users = relationship("LinkUserAndGroup", back_populates="groups", cascade="all, delete")

    def __init__(self, id_group: int, group_name: str):
        super().__init__()
        self.id_group = id_group
        self.group_name = group_name

    def __repr__(self):
        return f"{self.id_group} {self.group_name}"
