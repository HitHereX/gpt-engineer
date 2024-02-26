from fastapi import FastAPI
from routers import orders, payments, notifications

app = FastAPI()

app.include_router(orders.router)
app.include_router(payments.router)
app.include_router(notifications.router)