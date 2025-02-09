from mysql.connector import cursor, connect, MySQLConnection

from .Session import session
from sqlalchemy import select, func, distinct, literal
from sqlalchemy.orm import aliased, load_only
from sqlalchemy.sql import exists
from ..Database.Models.LinkUserAndGroup import LinkUserAndGroup
from ..Database.Models.Utente import Utente
from ..Database.Models.Gruppo import Gruppo
from ..Database.Models.Aula import Aula


def InsertGroup(id_group: int, group_name: str):
    gruppo = Gruppo(id_group=id_group, group_name=group_name)
    session.add(gruppo)
    session.commit()


def InsertUserInGroup(id_user: int, id_group: int):
    link_user = LinkUserAndGroup(id_user=id_user, id_group=id_group)
    session.add(link_user)
    session.commit()


def InsertUser(id_user: int, username: str, isAdmin: bool, isVerified: bool, isHide: bool):
    unique_utente = Utente(id_user=id_user, username=username,
                           isAdmin=isAdmin, isVerified=isVerified, isHide=isHide)
    session.add(unique_utente)
    session.commit()


def GetGroupUsers(id_group: int) -> dict:
    """Get users from id_group"""
    gruppo = session.query(Gruppo).filter(Gruppo.id_group == id_group).one_or_none()
    if gruppo is None:
        return {}
    else:
        return session.query(LinkUserAndGroup, Utente.username, Utente.id_user).filter(LinkUserAndGroup.id_group == gruppo.id_group)\
                .join(Utente, Utente.id_user == LinkUserAndGroup.id_user).all()


def CheckUserExists(id_user: int) -> bool:
    flag = session.query(Utente.id_user).filter(Utente.id_user == id_user).first()
    return flag is not None


def CheckUserExistsInGroup(id_user: int, id_group: int) -> bool:
    flag = session.query(LinkUserAndGroup) \
        .filter(LinkUserAndGroup.id_user == id_user, LinkUserAndGroup.id_group == id_group) \
        .first()

    return flag is not None


def GetGroups() -> list:
    return session.query(Gruppo.group_name, Gruppo.id_group).all()


def GetGroupName(id_group: int) -> str:
    return session.query(Gruppo.group_name).filter(Gruppo.id_group == id_group).first().group_name


def CheckGroupExists(id_group: int) -> bool:
    flag = session.query(Gruppo).filter(Gruppo.id_group == id_group).first()
    return flag is not None


def GetStatoAula(nome: str) -> bool:
    aula = session.query(Aula).filter(Aula.nome == nome).first()
    return aula.stato


def SetStatoAula(nome: str, stato: bool):
    aula: Aula = session.query(Aula).filter(Aula.nome == nome).one()
    aula.stato_aula = stato
    session.commit()


def GetIsAdmin(id_user: int) -> bool:
    utente = session.query(Utente).filter(Utente.id_user == id_user).first()
    return utente.isAdmin
