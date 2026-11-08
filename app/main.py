from fastapi import FastAPI
from app.routes.tickets import router as ticket_router
from app.routes.customers import router as customer_router

app = FastAPI()


#=============> Welcome endpoint <==============
@app.get("/")
def home():
    return {"message": "Welcome to HelpDesk API"}


# ============> Connect ticket routes <============
app.include_router(ticket_router)

#=============> Connect Customers_routes <=========
app.include_router(customer_router)
