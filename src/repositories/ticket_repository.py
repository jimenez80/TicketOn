from src.database.connection import SessionLocal
from src.database.models import TicketDB
from src.domain.enums.ticket_status import TicketStatus


class TicketRepository:

    def create(self, titulo: str, descripcion: str):

        db = SessionLocal()

        ticket = TicketDB(
            title=titulo,
            description=descripcion,
            status=TicketStatus.OPEN
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        db.close()

        return ticket

    def get_all(self, status: TicketStatus | None = None):

        db = SessionLocal()

        query = db.query(TicketDB)

        if status is not None:
            query = query.filter(
                TicketDB.status == status
            )

        tickets = query.all()

        db.close()

        return tickets

    def get_by_id(self, ticket_id: int):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        db.close()

        return ticket

    def update(
        self,
        ticket_id: int,
        title: str,
        description: str,
        status: TicketStatus
    ):

        db = SessionLocal()

        ticket = db.query(TicketDB).filter(
            TicketDB.id == ticket_id
        ).first()

        if ticket is None:
            db.close()
            return None

        ticket.title = title
        ticket.description = description
        ticket.status = status

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