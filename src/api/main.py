from fastapi import FastAPI

from src.api.routers.tickets import router


app = FastAPI(
    title="TicketOn API",
    version="1.0.0",
    description="API para la gestión de tickets de TicketOn"
)

app.include_router(router)