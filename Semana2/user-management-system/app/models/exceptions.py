class AppError(Exception):
    """Base exception for the application"""
    def __init__(self, message: str, code: str = "UNKNOWN_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)

class UserNotFoundError(AppError):
    """Raised when a user is not found"""
    def __init__(self, user_id: int):
        super().__init__(
            message=f"User with id {user_id} not found",
            code="USER_NOT_FOUND"
        )
        self.user_id = user_id

class DuplicateUserError(AppError):
    """Raised when trying to create a user that already exists"""
    ...

class InvalidRoleError(AppError):
    """Raised when an invalid role is assigned"""
    ...