from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ContactCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    notes: str | None = None

class ContactUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone: str | None = None
    company: str | None = None
    notes: str | None = None

class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    notes: str | None = None
    created_at: datetime
    updated_at: datetime