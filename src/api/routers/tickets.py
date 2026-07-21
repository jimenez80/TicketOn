from fastapi import APIRouter, HTTPException, Query

from src.services.ticket_service import TicketService
from src.domain.enums.ticket_status import TicketStatus
from src.api.schemas.ticket import (
    TicketResponse,
    TicketCreate,
    TicketUpdate,
    MessageResponse
)

router = APIRouter()


@router.get(
    "/tickets",
    response_model=list[TicketResponse]
)
def get_all_tickets(
    status: TicketStatus | None = Query(
        default=None,
        description="Filtrar tickets por estado"
    )
):

    service = TicketService()

    return service.get_all_tickets(status)


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

    updated_ticket = service.update_ticket(
        ticket_id=ticket_id,
        title=ticket.title,
        description=ticket.description,
        status=ticket.status
    )

    if updated_ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    return updated_ticket


@router.delete(
    "/tickets/{ticket_id}",
    response_model=MessageResponse
)
def delete_ticket(ticket_id: int):

    service = TicketService()

    deleted = service.delete_ticket(ticket_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    return {
        "message": "Ticket eliminado correctamente"
    }