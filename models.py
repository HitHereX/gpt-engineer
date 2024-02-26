from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    menu = relationship("Menu")
    status = Column(String, default="pending")  # pending, accepted, cooking, ready, delivering, delivered, cancelled
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rider_id = Column(Integer, ForeignKey('riders.id'), nullable=True)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)

class Rider(Base):
    __tablename__ = "riders"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    is_available = Column(Boolean, default=True)

class StoreOwner(Base):
    __tablename__ = "store_owners"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    store_name = Column(String)