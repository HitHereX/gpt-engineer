from sqlalchemy.orm import Session
from . import models, schemas

def get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()

def create_order(db: Session, order: schemas.OrderSchema):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order_status(db: Session, order_id: int, status: str):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db_order.status = status
        db.commit()
        db.refresh(db_order)
    return db_order

def get_orders_by_customer(db: Session, customer_id: int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()

def get_orders_by_rider(db: Session, rider_id: int):
    return db.query(models.Order).filter(models.Order.rider_id == rider_id).all()

def get_available_riders(db: Session):
    return db.query(models.Rider).filter(models.Rider.is_available == True).all()