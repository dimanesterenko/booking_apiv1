from sqlalchemy import Column, Integer, String, Boolean
from db import Base
class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(255),unique=True,index=True,nullable=False)
    password = Column(String(255),nullable=False)
    
    

class Booking(Base):
    __tablename__='bookings'
