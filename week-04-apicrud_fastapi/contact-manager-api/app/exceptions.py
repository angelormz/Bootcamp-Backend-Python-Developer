class ContactNotFoundError(Exception):
    def __init__(self, contact_id: int):
        self.contact_id = contact_id
        self.message = f"Contact with id {contact_id} not found"
        super().__init__(self.message)

class DuplicateEmailError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"Contact with email '{email}' already exists"
        super().__init__(self.message)