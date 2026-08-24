
from app.models.user import User, Role, RoleType
from app.models.exceptions import (
    UserNotFoundError,
    DuplicateUserError,
    InvalidRoleError,
)


class UserService:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id: int = 1

    def create_user(
        self,
        username: str,
        email: str,
        role_type: RoleType,
    ) -> User:

        # Validar rol
        if not isinstance(role_type, RoleType):
            raise InvalidRoleError(str(role_type))

        # Validar email duplicado
        for user in self._users.values():
            if user.email == email:
                raise DuplicateUserError(email)

        role = Role(
            name=role_type,
            permissions=[],
        )

        user = User(
            id=self._next_id,
            username=username,
            email=email,
            role=role,
        )

        self._users[self._next_id] = user
        self._next_id += 1

        return user

    def get_user(self, user_id: int) -> User:
        if user_id not in self._users:
            raise UserNotFoundError(user_id)

        return self._users[user_id]

    def list_users(self, active_only: bool = True) -> list[User]:
        users = list(self._users.values())

        if active_only:
            return [user for user in users if user.is_active]

        return users

    def deactivate_user(self, user_id: int) -> User:
        user = self.get_user(user_id)
        user.is_active = False
        return user

    def update_role(
        self,
        user_id: int,
        new_role: RoleType,
    ) -> User:

        if not isinstance(new_role, RoleType):
            raise InvalidRoleError(str(new_role))

        user = self.get_user(user_id)

        user.role = Role(
            name=new_role,
            permissions=[],
        )

        return user