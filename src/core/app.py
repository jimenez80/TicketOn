from src.database.connection import engine
from src.database.models import Base, TicketDB
from src.services.ticket_service import TicketService

def start_system():
    Base.metadata.create_all(bind=engine)
    service = TicketService()

    ticket = service.create_ticket(
        title="Primer ticket",
        description="Ticket creado desde SQLite"
    )

    tickets = service.get_all_tickets()

    updated_ticket = service.update_ticket_status(
        ticket_id=ticket["id"],
        new_status="in_progress"
    )

    deleted = service.delete_ticket(ticket["id"])

    tickets = service.get_all_tickets()

    print("Core del sistema inicializado correctamente")

    print("Base de datos lista")

    print(f"Ticket creado: {ticket}")
    print(f"Ticket actualizado: {updated_ticket}")
    print(f"Ticket eliminado: {deleted}")

    print("\nTickets almacenados:")

    for item in tickets:
        print(item)

    return "TicketOn core activo"