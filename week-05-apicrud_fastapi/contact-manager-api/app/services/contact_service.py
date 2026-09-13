from datetime import datetime
from app.schemas.contact import ContactCreate, ContactUpdate, ContactResponse
from app.exceptions import ContactNotFoundError, DuplicateEmailError

class ContactService:
    def __init__(self) -> None:
        self._contacts: dict[int, dict] = {}
        self._next_id: int = 1

    def create(self, data: ContactCreate) -> ContactResponse:
        # Check duplicate email
        # Create contact with auto-increment id
        # Return ContactResponse

        for contact in self._contacts.values():
            if contact["email"] == str(data.email):
                raise DuplicateEmailError(str(data.email))

        now = datetime.now()

        contact = {
            "id": self._next_id,
            "name": data.name,
            "email": str(data.email),
            "phone": data.phone,
            "company": data.company,
            "notes": data.notes,
            "created at": now,
            "updated at": now,
        }

        self._contacts[self._next_id] = contact
        self._next_id += 1

        return ContactResponse(**contact)

    def get_by_id(self, contact_id: int) -> ContactResponse:
        # Raise ContactNotFoundError if not found
        
        contact = self._contacts.get(contact_id)

        if contact is None:
            raise ContactNotFoundError(contact_id)

        return ContactResponse(**contact)

    def list_all(self, company: str | None = None, limit: int = 50) -> list[ContactResponse]:
        # Filter by company if provided
        # Apply limit

        contacts = list(self._contacts.values())

        if company is not None:
            contacts = [
                contact
                for contact in contacts
                if contact["company"] == company
            ]

            return [
                ContactResponse(**contact)
                for contact in contacts[:limit]
            ]

    def update(self, contact_id: int, data: ContactUpdate) -> ContactResponse:
        # Partial update (only non-None fields)
        # Update updated_at timestamp

        contact = self._contacts.get(contact_id)

        if contact is None:
            raise ContactNotFoundError(contact_id)

        update_data = data.model_dump(exclude_none=True)

        contact.update(update_data)
        contact["updated_at"] = datetime.now()

        return ContactResponse(**contact)

    def delete(self, contact_id: int) -> None:
        # Raise ContactNotFoundError if not found

        if contact_id not in self._contacts:
            raise ContactNotFoundError(contact_id)

        del self._contacts[contact_id]
