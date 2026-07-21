from pydantic import BaseModel, Field
from src.domain.enums.ticket_status import TicketStatus

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus

class TicketCreate(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=100
    )

    description: str = Field(
        min_length=10,
        max_length=500
    )

class TicketUpdate(BaseModel):
    title: str
    description: str
    status: TicketStatus

class MessageResponse(BaseModel):
    message: str