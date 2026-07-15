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
    
    def update_status(self, ticket_id: int, new_status: str):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        if ticket is None:
            db.close()
            return None

        ticket.status = new_status

        db.commit()
        db.refresh(ticket)

        db.close()

        return ticket
    
    def delete(self, ticket_id: int):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        if ticket is None:
            db.close()
            return False

        db.delete(ticket)
        db.commit()

        db.close()

        return True
    
    def get_by_id(self, ticket_id: int):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        db.close()

        return ticket

    def get_by_id(self, ticket_id: int):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        db.close()

        return ticket