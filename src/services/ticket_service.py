from src.database.connection import SessionLocal
from src.database.models import TicketDB

class TicketService:
    def create_ticket(self, title: str, description: str):

        db = SessionLocal()

        ticket = TicketDB(
            title=title,
            description=description,
            status="open"
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        db.close()

        return {
            "id": ticket.id,
            "title": ticket.title,
            "description": ticket.description,
            "status": ticket.status
        }
    
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
    
    def get_all_tickets(self):
        db = SessionLocal()

        tickets = db.query(TicketDB).all()

        result = []

        for ticket in tickets:
            result.append({
                "id": ticket.id,
                "title": ticket.title,
                "description": ticket.description,
                "status": ticket.status
            })

        db.close()

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