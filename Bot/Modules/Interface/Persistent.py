from Modules.Shared.Session import session
from Modules.Database.Connect import engine
from Modules.Database.Models.Aula import Aula


def CreatePersistent():

    aulaFalcon = Aula(
        nome_aula="AulaFalcon",
        stato_aula=False
    )
    session.add(aulaFalcon)
    session.commit()