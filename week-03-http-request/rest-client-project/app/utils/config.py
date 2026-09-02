import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env en la raíz del proyecto
load_dotenv()

@dataclass
class Settings:
    weather_api_key: str = os.getenv("WEATHER_API_KEY", "")
    github_token: str = os.getenv("GITHUB_TOKEN", "")

settings = Settings()