from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


# ==============>  CUSTOMER_CLASS_TABLE  <==============

class Customer(Base):
    __tablename__= "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable= False)
    
    tickets= relationship("Ticket", back_populates= "customer",  passive_deletes=True)
    
# ==============>  TICKET_CLASS_TABLE  <================

class Ticket(Base):
    __tablename__= "tickets"
    
    customer_id= Column(Integer, ForeignKey("customers.id", ondelete="SET NULL") ,nullable= True)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable= False)
    description = Column(String, nullable= False)
    customer_name = Column(String, default= "Guest")
    status = Column(String, default= "Open")
    
    customer= relationship("Customer", back_populates= "tickets")