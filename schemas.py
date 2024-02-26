from pydantic import BaseModel
from typing import Optional

class MenuSchema(BaseModel):
    name: str
    price: float

class OrderSchema(BaseModel):
    menu_id: int
    customer_id: int

class OrderStatusUpdateSchema(BaseModel):
    status: str

class CustomerSchema(BaseModel):
    name: str
    phone_number: str

class RiderSchema(BaseModel):
    name: str
    phone_number: str
    is_available: bool

class StoreOwnerSchema(BaseModel):
    name: str
    store_name: str