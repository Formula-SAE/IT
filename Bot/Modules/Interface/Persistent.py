from Modules.Shared.Session import session
from Modules.Database.Connect import engine
from Modules.Database.Models.Aula import Aula
from Modules.Database.Models.Utente import Utente


def CreatePersistent():

    aulaFalcon = Aula(
        nome_aula="AulaFalcon",
        stato_aula=False
    )

    session.add(aulaFalcon)

    new_user = Utente(id_telegram=12345, username="aaa", isAdmin=False, isVerified=True, isHide=False)
    session.add(new_user)


    session.commit()