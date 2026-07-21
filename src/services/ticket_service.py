from src.repositories.ticket_repository import TicketRepository
from src.domain.enums.ticket_status import TicketStatus


class TicketService:

    def __init__(self):
        self.repository = TicketRepository()

    def _to_dict(self, ticket):
        return {
            "id": ticket.id,
            "title": ticket.title,
            "description": ticket.description,
            "status": ticket.status
        }

    def create_ticket(self, titulo: str, descripcion: str):

        ticket = self.repository.create(titulo, descripcion)

        return self._to_dict(ticket)

    def get_all_tickets(self, status: TicketStatus | None = None):

        tickets = self.repository.get_all(status)

        result = []

        for ticket in tickets:
            result.append(self._to_dict(ticket))

        return result

    def get_ticket_by_id(self, ticket_id: int):

        ticket = self.repository.get_by_id(ticket_id)

        if ticket is None:
            return None

        return self._to_dict(ticket)

    def update_ticket(
        self,
        ticket_id: int,
        title: str,
        description: str,
        status: TicketStatus
    ):

        ticket = self.repository.update(
            ticket_id,
            title,
            description,
            status
        )

        if ticket is None:
            return None

        return self._to_dict(ticket)

    def delete_ticket(self, ticket_id: int):

        return self.repository.delete(ticket_id)