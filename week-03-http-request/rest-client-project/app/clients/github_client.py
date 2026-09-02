from app.clients.base_client import BaseClient

class GitHubClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(base_url="https://api.github.com")

    async def get_user(self, username: str) -> dict:
        return await self.get(f"/users/{username}")

    async def get_user_repos(self, username: str, per_page: int = 5) -> list[dict]:
        return await self.get(
            f"/users/{username}/repos",
            params={"per_page": per_page, "sort": "updated"},
        )