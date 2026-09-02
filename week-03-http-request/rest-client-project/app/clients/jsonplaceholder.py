from app.clients.base_client import BaseClient

class JSONPlaceholderClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(base_url="https://jsonplaceholder.typicode.com")

    async def get_posts(self, user_id: int | None = None) -> list[dict]:
        params = {"userId": user_id} if user_id else None
        return await self.get("/posts", params=params)

    async def get_user(self, user_id: int) -> dict:
        return await self.get(f"/users/{user_id}")

    async def create_post(self, title: str, body: str, user_id: int) -> dict:
        return await self.post("/posts", data={
            "title": title,
            "body": body,
            "userId": user_id,
        })