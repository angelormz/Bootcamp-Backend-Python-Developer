from app.clients.base_client import BaseClient
from app.utils.config import settings

class WeatherClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(base_url="https://api.openweathermap.org/data/2.5")

    async def get_weather(self, city: str) -> dict:
        return await self.get("/weather", params={
            "q": city,
            "appid": settings.weather_api_key,
            "units": "metric",
        })