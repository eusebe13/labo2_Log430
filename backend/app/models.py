import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String  #, ForeignKey
from sqlalchemy.orm import declarative_base  #, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    total = Column(Float)
