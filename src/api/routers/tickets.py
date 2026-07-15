from fastapi import APIRouter

from src.services.ticket_service import TicketService
from src.api.schemas.ticket import TicketResponse, TicketCreate

router = APIRouter()


@router.get(
    "/tickets",
    response_model=list[TicketResponse]
)
def get_all_tickets():

    service = TicketService()

    return service.get_all_tickets()


@router.post(
    "/tickets",
    response_model=TicketResponse
)
def create_ticket(ticket: TicketCreate):

    service = TicketService()

    return service.create_ticket(
        titulo=ticket.title,
        descripcion=ticket.description
    )