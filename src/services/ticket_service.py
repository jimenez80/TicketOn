from src.database.connection import SessionLocal
from src.database.models import TicketDB
from src.repositories.ticket_repository import TicketRepository


class TicketService:

    def __init__(self):
        self.repository = TicketRepository()

    def create_ticket(self, titulo: str, descripcion: str):

        ticket = self.repository.create(titulo, descripcion)

        return {
            "id": ticket.id,
            "title": ticket.title,
            "description": ticket.description,
            "status": ticket.status
        }

    def get_all_tickets(self):

        
        tickets = self.repository.get_all()

        result = []

        for ticket in tickets:
            result.append({
                "id": ticket.id,
                "title": ticket.title,
                "description": ticket.description,
                "status": ticket.status
            })

        
        return result

    def update_ticket_status(self, ticket_id: int, new_status: str):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()

        if ticket is None:
            db.close()
            return None

        ticket.status = new_status

        db.commit()
        db.refresh(ticket)

        result = {
            "id": ticket.id,
            "title": ticket.title,
            "description": ticket.description,
            "status": ticket.status
        }

        db.close()

        return result

    def delete_ticket(self, ticket_id: int):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()

        if ticket is None:
            db.close()
            return False

        db.delete(ticket)
        db.commit()

        db.close()

        return True