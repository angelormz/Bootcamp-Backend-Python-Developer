class AppError(Exception):
    """Excepción base de la aplicación."""

    def __init__(
        self,
        message: str,
        code: str = "UNKNOWN_ERROR",
    ) -> None:
        self.message = message
        self.code = code

        super().__init__(message)


class UserNotFoundError(AppError):
    """Se lanza cuando un usuario no existe."""

    def __init__(self, user_id: int) -> None:
        super().__init__(
            message=f"User with id {user_id} not found",
            code="USER_NOT_FOUND",
        )

        self.user_id = user_id


class DuplicateUserError(AppError):
    """Se lanza cuando el email ya existe."""

    def __init__(self, email: str) -> None:
        super().__init__(
            message=f"User with email {email} already exists",
            code="DUPLICATE_USER",
        )

        self.email = email


class InvalidRoleError(AppError):
    """Se lanza cuando el rol no es válido."""

    def __init__(self, role: str) -> None:
        super().__init__(
            message=f"Invalid role: {role}",
            code="INVALID_ROLE",
        )

        self.role = role
