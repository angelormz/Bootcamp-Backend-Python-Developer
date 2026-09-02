from app.clients.base_client import BaseClient

class Countries(BaseClient):
    def __init__(self) -> None:
        super().__init__(base_url="https://restcountries.com/v3.1")

    async def get_country_by_name(self, name:str):
        """Consulta información de un país por su nombre común o traducción."""
        return await self.get(f"/name/{name}")