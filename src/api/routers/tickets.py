from fastapi import APIRouter, HTTPException

from src.services.ticket_service import TicketService
from src.api.schemas.ticket import (
    TicketResponse,
    TicketCreate,
    TicketUpdate
)

router = APIRouter()

router = APIRouter()

@router.get(
    "/tickets",
    response_model=list[TicketResponse]
)
def get_all_tickets():

    service = TicketService()

    return service.get_all_tickets()

@router.get(
    "/tickets/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket_by_id(ticket_id: int):

    service = TicketService()

    ticket = service.get_ticket_by_id(ticket_id)

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    return ticket
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
@router.put(
    "/tickets/{ticket_id}",
    response_model=TicketResponse
)
def update_ticket(
    ticket_id: int,
    ticket: TicketUpdate
):

    service = TicketService()

    updated_ticket = service.update_ticket_status(
        ticket_id=ticket_id,
        new_status=ticket.status
    )

    if updated_ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    return updated_ticket