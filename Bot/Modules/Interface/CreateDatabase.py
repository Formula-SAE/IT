from Modules.Database.Models.UtenteGruppo import UtenteGruppo
from Modules.Database.Models.Gruppo import Gruppo
from Modules.Database.Models.Aula import Aula
from Modules.Database.Models.Utente import Utente
from Modules.Database.Models.Base import Base
from Modules.Database.Connect import engine

def CreateAll():
    Base.metadata.create_all(bind=engine)