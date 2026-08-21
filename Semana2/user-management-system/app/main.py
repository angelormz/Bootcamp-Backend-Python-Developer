import asyncio
import httpx

async def check_email_availability(emails: list[str]) -> dict[str, bool]:
    """Simulates checking if emails are available (async)"""
    async def check_single(email: str) -> tuple[str, bool]:
        await asyncio.sleep(0.5)  # Simula latencia de API
        is_available = "@" in email and "." in email.split("@")[-1]
        return email, is_available

    tasks = [check_single(email) for email in emails]
    results = await asyncio.gather(*tasks)
    return dict(results)