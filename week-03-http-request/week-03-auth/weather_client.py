# weather_client.py — Cliente de API con todas las buenas prácticas
import os
import sys
import httpx
from dotenv import load_dotenv


class WeatherClient:
    """Cliente para consumir APIs de clima con autenticación segura."""
    
    BASE_URL = "https://httpbin.org"
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHER_API_KEY", "")
        self.app_name = os.environ.get("APP_NAME", "WeatherClient")
        
        if not self.api_key:
            print("ERROR: OPENWEATHER_API_KEY no encontrada en .env")
            print("Solución: cp .env.example .env && edita .env")
            sys.exit(1)
        
        self.client = httpx.Client(
            headers={
                "X-API-Key": self.api_key,
                "User-Agent": f"{self.app_name}/1.0",
                "Accept": "application/json",
            },
            timeout=10.0,
        )
    
    def get_weather(self, city: str) -> dict:
        """Obtiene el clima de una ciudad (simulado con httpbin)."""
        response = self.client.get(
            f"{self.BASE_URL}/get",
            params={"city": city, "units": "metric"}
        )
        response.raise_for_status()
        return response.json()
    
    def get_forecast(self, city: str, days: int = 5) -> dict:
        """Obtiene el pronóstico extendido (simulado)."""
        response = self.client.get(
            f"{self.BASE_URL}/get",
            params={"city": city, "days": days, "units": "metric"}
        )
        response.raise_for_status()
        return response.json()
    
    def close(self):
        """Cierra el cliente HTTP."""
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


def main():
    """Demuestra el uso del cliente con todas las buenas prácticas."""
    print("Weather Client — Demo de API key segura\n")
    
    with WeatherClient() as client:
        # Request 1: Clima actual
        print("1. Obteniendo clima de Mexico City...")
        weather = client.get_weather("Mexico City")
        print(f"   Status: 200 OK")
        print(f"   Headers enviados:")
        for key, value in weather.get("headers", {}).items():
            if key.startswith("X-") or key == "User-Agent":
                print(f"     {key}: {value}")
        
        # Request 2: Pronóstico
        print("\n2. Obteniendo pronóstico de Buenos Aires...")
        forecast = client.get_forecast("Buenos Aires", days=7)
        print(f"   Status: 200 OK")
        print(f"   Params enviados: {forecast.get('args', {})}")
    
    print("\n✓ Cliente cerrado correctamente")
    print("✓ API key nunca expuesta en el código fuente")


if __name__ == "__main__":
    main()