from app.clients.base_client import BaseClient

class HttpBinClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(base_url="https://httpbin.org", timeout=2.0)
    async def test_delay(self, seconds: int = 3) -> dict:
        return await self.get(f"/delay/{seconds}")

    async def test_status(self, code: int) -> dict:
            return await self.get(f"/status/{code}")