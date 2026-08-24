import asyncio

from app.models.user import RoleType
from app.models.exceptions import (
    UserNotFoundError,
    DuplicateUserError,
    InvalidRoleError,
)
from app.services.user_service import UserService


async def check_email_availability(emails: list[str]) -> dict[str, bool]:
    async def check_single(email: str) -> tuple[str, bool]:
        await asyncio.sleep(0.5)

        is_available = (
            "@" in email
            and "." in email.split("@")[-1]
        )

        return email, is_available

    tasks = [check_single(email) for email in emails]

    results = await asyncio.gather(*tasks)

    return dict(results)


def main() -> None:
    service = UserService()

    # Crear usuarios
    service.create_user(
        "admin",
        "admin@example.com",
        RoleType.ADMIN,
    )

    service.create_user(
        "editor",
        "editor@example.com",
        RoleType.EDITOR,
    )

    print("Usuarios creados correctamente")

    # DuplicateUserError
    try:
        service.create_user(
            "otro_admin",
            "admin@example.com",
            RoleType.ADMIN,
        )
    except DuplicateUserError as e:
        print(f"DuplicateUserError capturado: {e}")

    # UserNotFoundError
    try:
        service.get_user(999)
    except UserNotFoundError as e:
        print(f"UserNotFoundError capturado: {e}")

    # InvalidRoleError
    try:
        service.create_user(
            "test",
            "test@example.com",
            "superadmin",  # type: ignore
        )
    except InvalidRoleError as e:
        print(f"InvalidRoleError capturado: {e}")

    # Async
    resultados = asyncio.run(
        check_email_availability(
            [
                "admin@test.com",
                "editor@test.com",
                "invalid",
            ]
        )
    )

    print(f"Resultados async: {resultados}")


if __name__ == "__main__":
    main()