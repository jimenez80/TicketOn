from src.repositories.ticket_repository import TicketRepository


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

    def get_all_tickets(self):

        tickets = self.repository.get_all()

        result = []

        for ticket in tickets:
            result.append(self._to_dict(ticket))

        return result

    def get_ticket_by_id(self, ticket_id: int):

        ticket = self.repository.get_by_id(ticket_id)

        if ticket is None:
            return None

        return self._to_dict(ticket)

    def update_ticket_status(self, ticket_id: int, new_status: str):

        ticket = self.repository.update_status(ticket_id, new_status)

        if ticket is None:
            return None

        return self._to_dict(ticket)

    def delete_ticket(self, ticket_id: int):

        return self.repository.delete(ticket_id)
        
    def get_ticket_by_id(self, ticket_id: int):

        ticket = self.repository.get_by_id(ticket_id)

        if ticket is None:
            return None

        return self._to_dict(ticket)