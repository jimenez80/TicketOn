from src.database.connection import SessionLocal
from src.database.models import TicketDB


class TicketRepository:

    def create(self, titulo: str, descripcion: str):

        db = SessionLocal()

        ticket = TicketDB(
            title=titulo,
            description=descripcion,
            status="open"
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        db.close()

        return ticket

    def get_all(self):

        db = SessionLocal()

        tickets = db.query(TicketDB).all()

        db.close()

        return tickets