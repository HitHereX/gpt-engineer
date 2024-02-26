from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/orders/", response_model=schemas.OrderSchema)
def create_order(order: schemas.OrderSchema, db: Session = Depends(dependencies.get_db)):
    return crud.create_order(db=db, order=order)

@router.put("/orders/{order_id}/status/", response_model=schemas.OrderStatusUpdateSchema)
def update_order_status(order_id: int, status: schemas.OrderStatusUpdateSchema, db: Session = Depends(dependencies.get_db)):
    db_order = crud.update_order_status(db=db, order_id=order_id, status=status.status)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.get("/orders/{customer_id}/", response_model=list[schemas.OrderSchema])
def get_orders_by_customer(customer_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.get_orders_by_customer(db=db, customer_id=customer_id)