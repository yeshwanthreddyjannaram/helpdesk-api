from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

# ==============> POST CUSTOMERS <=================
@router.post("", status_code= 201)
def create_customer(customer : schemas.CustomerCreate, db: Session= Depends(get_db)):
    new_customer= models.Customer(
        name= customer.name,
        email = customer.email
    )
    
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    
    return new_customer

#==============> GET ALL_CUSTOMERS <===============
@router.get("")
def get_customers(db: Session= Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers

#===============> GET CUSTOMER_BY_ID <=============
@router.get("/{customer_id}")
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer= db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    
    if customer is None:
        raise HTTPException(
            status_code= 404,
            detail= "Customer not found"
        )
        
    return customer

#=================> DELETE CUSTOMMER <==============
@router.delete("/{customer_id}")
def delete_customer_by_id(customer_id: int, db: Session= Depends(get_db)):
    customer= db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    
    if customer is None:
        raise HTTPException(
            status_code= 404,
            detail= "Customer not found"
        )
    db.delete(customer)
    db.commit()
    
    return {"message": "Customer deleted successfully"}

