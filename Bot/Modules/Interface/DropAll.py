from Modules.Database.Models.LinkUserAndGroup import LinkUserAndGroup
from Modules.Database.Models.Gruppo import Gruppo
from Modules.Database.Models.Aula import Aula
from Modules.Database.Models.Utente import Utente
from Modules.Database.Models.Base import Base
from Modules.Database.Connect import engine

def DropAll():
    Base.metadata.drop_all(engine)