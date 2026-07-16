from pydantic import BaseModel


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str 

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketUpdate(BaseModel):
    status: str

class MessageResponse(BaseModel):
    message: str