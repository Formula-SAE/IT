from mysql.connector import cursor, connect, MySQLConnection

from .Session import session
from sqlalchemy import select, func, distinct, literal
from sqlalchemy.orm import aliased, load_only
from sqlalchemy.sql import exists
from ..Database.Models.Utente import Utente
from ..Database.Models.Gruppo import Gruppo
from ..Database.Models.Aula import Aula


def InsertGroup(id_gruppo: int, team_name: str):
    gruppo = Gruppo(
        id_gruppo=id_gruppo,
        team_name=team_name)

    session.add(gruppo)
    session.commit()

def InsertUser(id_Telegram: int, username: str, group_name: str, isAdmin: bool, isVerified: bool, isHide: bool):
    utente = Utente(
        id_telegram=id_Telegram,
        username=username,
        group_name=group_name,
        isAdmin=isAdmin,
        isVerified=isVerified,
        isHide=isHide
    )

    session.add(utente)
    session.commit()


def RemoveUser(id_telegram: int) -> dict:
    if not CheckUserExists(id_telegram=id_telegram):
        return {"Error": "Utente non esistente"}
    session.query(Utente).filter(Utente.id_telegram == f"{id_telegram}").delete()
    session.commit()

    return {"State": f"Utente con id_telegram: '{id_telegram}' cancellato!"}


def GetGroupUsers(id_telegram_group: int) -> dict:
    """Get users from id_telegram_group"""
    team_name = session.query(Gruppo).filter(Gruppo.id_gruppo == -id_telegram_group).one().team_name
    return session.query(Utente).filter(Utente.group_name == team_name, Utente.isVerified == True).all()


def CheckUserExists(id_telegram: int) -> bool:
    query = session.query(Utente).filter(Utente.id_telegram == f"{id_telegram}")
    exists = session.query(query.exists()).scalar()

    return bool(exists)


def GetUsername(id_telegram: int) -> str:
    return session.query(Utente).filter(Utente.id_telegram == f"{id_telegram}").one().username


def GetGroupName(id_telegram: int) -> str:
    return session.query(Utente).filter(Utente.id_telegram == f"{id_telegram}").one().email

def CheckGroupExists(id_telegram: int) -> bool:
    query = session.query(Gruppo).filter(Gruppo.id_gruppo == f"{id_telegram}")
    exists = session.query(query.exists()).scalar()

    return bool(exists)


def GetStatoAula(nome_aula: str) -> bool:
    return session.query(Aula).filter(Aula.nome_aula == nome_aula).one().stato_aula

def SetStatoAula(nome_aula : str, status : bool):
    aula: Aula = session.query(Aula).filter(Aula.nome_aula == nome_aula).one()
    aula.stato_aula = status
    session.commit()

def GetIsAdmin(id_telegram: int) -> bool:
    return bool(session.query(Utente).filter(Utente.id_telegram == f"{id_telegram}").one().is_Admin)
