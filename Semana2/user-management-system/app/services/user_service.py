from app.models.user import User, Role, RoleType
from app.models.exceptions import UserNotFoundError, DuplicateUserError

class UserService:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id: int = 1

    def create_user(self, username: str, email: str, role_type: RoleType) -> User:
        # Check for duplicates
        # Create user with auto-increment id
        # Store in _users dict
        ...

    def get_user(self, user_id: int) -> User:
        # Raise UserNotFoundError if not found
        ...

    def list_users(self, active_only: bool = True) -> list[User]:
        ...

    def deactivate_user(self, user_id: int) -> User:
        ...

    def update_role(self, user_id: int, new_role: RoleType) -> User:
        ...