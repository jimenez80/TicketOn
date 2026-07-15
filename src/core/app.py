from src.database.connection import engine
from src.database.models import Base


def start_system():

    Base.metadata.create_all(bind=engine)

    print("Core del sistema inicializado correctamente")
    print("Base de datos lista")

    return "TicketOn core activo"