from Modules.Shared.Session import session
from Modules.Database.Connect import engine
from Modules.Database.Models.Aula import Aula
from Modules.Database.Models.Utente import Utente
from Modules.Database.Models.Gruppo import Gruppo
from Modules.Database.Models.LinkUserAndGroup import LinkUserAndGroup


def CreatePersistent():

    aulaFalcon = Aula(
        nome="AulaFalcon",
        stato=False
    )

    session.add(aulaFalcon)

    group = Gruppo(id_group=1, group_name="Test Group")
    session.add(group)

    session.commit()

    new_user = Utente(id_user=12345, username="Test", isAdmin=False, isVerified=True, isHide=False)

    session.add(new_user)

    link = LinkUserAndGroup(id_user=new_user.id_user, id_group=group.id_group)
    session.add(link)

    session.commit()
