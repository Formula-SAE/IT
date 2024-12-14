from Modules.Database.Models.Utente import Utente
from Modules.Database.Models.Gruppo import Gruppo
from Modules.Database.Models.Base import Base
from Modules.Database.Connect import engine

def DropAll():
    Base.metadata.drop_all(engine)