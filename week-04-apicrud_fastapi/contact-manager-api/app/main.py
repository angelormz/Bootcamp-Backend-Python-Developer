from fastapi import FastAPI, HTTPException, status, Query
from app.schemas.contact import ContactCreate, ContactUpdate, ContactResponse
from app.services.contact_service import ContactService
from app.exceptions import ContactNotFoundError, DuplicateEmailError

app = FastAPI(
    title="Contact Manager API",
    description="API CRUD para gestión de contactos — Week 4 Entrega",
    version="1.0.0",
)

service = ContactService()

@app.get("/")
def health_check() -> dict[str,str]:
    return {"status": "ok"}

@app.get("/contacts", response_model=list[ContactResponse])
def list_contacts(
    company: str | None = None,
    limit: int = Query(default=50, ge=1, le=100),
) -> list[ContactResponse]:
    return service.list_all(company=company, limit=limit)

@app.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int) -> ContactResponse:
    try:
        return service.get_by_id(contact_id)
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")

@app.post("/contacts", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(data: ContactCreate) -> ContactResponse:
    try:
        return service.create(data)
    except DuplicateEmailError as e:
        raise HTTPException(status_code=409, detail=e.message)

@app.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, data: ContactUpdate) -> ContactResponse:
    try:
        return service.update(contact_id, data)
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")

@app.delete("/contacts/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int) -> None:
    try:
        service.delete(contact_id)
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")