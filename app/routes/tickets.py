
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(prefix="/tickets")


# =============> PYDANTIC MODELS <=================

class Ticket(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=10)
    customer_name: str = Field(default="Guest", min_length=3)
    customer_id: int | None = Field(default=None, gt=0)


class TicketStatus(BaseModel):
    status: Literal["Open", "In Progress", "Resolved"]


class TicketUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    description: str | None = Field(default=None, min_length=10)
    status: Literal["Open", "In Progress", "Resolved"] | None = None



# =============> POST TICKET <====================

@router.post("", status_code=201)
def create_ticket(ticket: Ticket, db: Session = Depends(get_db)):
    
    if ticket.customer_id is not None:
        customer = db.query(models.Customer).filter(
            models.Customer.id == ticket.customer_id
        ).first()

        if customer is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )
    new_ticket = models.Ticket (
        title = ticket.title,
        description = ticket.description,
        customer_name = ticket.customer_name,
        customer_id = ticket.customer_id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return {
        "message": "Ticket Created Successfully",
        "ticket": new_ticket
    }


# =============> GET ALL TICKETS <=================

@router.get("", status_code=200)
def get_tickets(db: Session= Depends(get_db)):
    tickets= db.query(models.Ticket).all()
    return tickets


# =============> GET TICKET BY ID <================

@router.get("/{ticket_id}", status_code=200)
def get_ticket_by_id(ticket_id: int, db: Session= Depends(get_db)):
    ticket= db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    
    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket does not exist"
        )
    return ticket


# =============> UPDATE TICKET STATUS <============

@router.put("/{ticket_id}", status_code=200)
def update_ticket(ticket_id: int, ticket: Ticket, db: Session= Depends(get_db)):
    existing_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    if existing_ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket does not exist"
        )
    existing_ticket.title=ticket.title
    existing_ticket.description= ticket.description
    existing_ticket.customer_name= ticket.customer_name
    
    db.commit()
    db.refresh(existing_ticket)
    return existing_ticket
    
    
# =============> DELETE TICKET <===================

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session= Depends(get_db)):
    ticket= db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    
    db.delete(ticket)
    db.commit()
    
    return {"message": "Ticket deleted successfully"}


# =============> PATCH UPDATE <====================

@router.patch("/{ticket_id}")
def patch_ticket(ticket_id: int, ticket: TicketUpdate, db: Session= Depends(get_db)):
    existing_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    if existing_ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    
    update_data = ticket.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(existing_ticket, key, value)
    db.commit()
    db.refresh(existing_ticket)
    
    return existing_ticket
