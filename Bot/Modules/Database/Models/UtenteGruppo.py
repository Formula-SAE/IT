from sqlalchemy import Column, String, Integer, Boolean, PrimaryKeyConstraint
from ..Models.Base import Base


class UtenteGruppo(Base):
    __tablename__ = "Utente"

    id_telegram = Column("id_telegram", Integer, nullable=False)
    username = Column("username", String, nullable=False)
    group_name = Column("group_name", String, default=False, nullable=True)
    isAdmin = Column("isAdmin", Boolean, default=False, nullable=True)
    isVerified = Column("isVerified", Boolean, default=False, nullable=True)
    isHide = Column("isHide", Boolean, default=False, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint("id_telegram", "group_name", name="pk_id_telegram_group_name"),
    )
    
    def __init__(self, id_telegram: int, username: str, group_name: str, isAdmin: bool, isVerified: bool, isHide: bool):
        self.id_telegram = id_telegram
        self.username = username
        self.group_name = group_name
        self.isAdmin = isAdmin
        self.isVerified = isVerified
        self.isHide = isHide

    def __repr__(self):
        return f"{self.id_telegram} {self.username} {self.group_name} {self.isAdmin} {self.isVerified} {self.isHide}"