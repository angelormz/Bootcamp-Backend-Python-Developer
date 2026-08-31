# api_client.py — Cliente que consume APIs autenticadas
import os
import httpx
from dotenv import load_dotenv

load_dotenv()


def demo_api_key_header():
    """Demuestra envío de API key en header personalizado."""
    print("=" * 60)
    print("Demo 1: API Key en header X-API-Key")
    print("=" * 60)
    
    api_key = os.environ.get("OPENWEATHER_API_KEY", "demo-key")
    
    # httpbin.org refleja todo lo que le envías — perfecto para testing
    response = httpx.get(
        "https://httpbin.org/headers",
        headers={
            "X-API-Key": api_key,
            "X-App-Name": "WeatherClient",
        }
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    
    print("Headers que el servidor recibió:")
    for key, value in data["headers"].items():
        print(f"  {key}: {value}")


def demo_bearer_token():
    """Demuestra envío de Bearer token en Authorization header."""
    print("\n" + "=" * 60)
    print("Demo 2: Bearer Token en Authorization header")
    print("=" * 60)
    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ejemplo"
    
    response = httpx.get(
        "https://httpbin.org/bearer",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"Respuesta: {response.json()}")
    else:
        print(f"Error: {response.text}")


def demo_basic_auth():
    """Demuestra Basic Auth con httpx."""
    print("\n" + "=" * 60)
    print("Demo 3: Basic Auth")
    print("=" * 60)
    
    # httpbin.org tiene un endpoint que valida Basic Auth
    username = "testuser"
    password = "testpass"
    
    response = httpx.get(
        f"https://httpbin.org/basic-auth/{username}/{password}",
        auth=(username, password)
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"Autenticado: {response.json()}")
    else:
        print("Autenticación fallida")


def demo_query_param_key():
    """Demuestra API key como query parameter."""
    print("\n" + "=" * 60)
    print("Demo 4: API Key como query parameter")
    print("=" * 60)
    
    api_key = os.environ.get("OPENWEATHER_API_KEY", "demo-key")
    
    response = httpx.get(
        "https://httpbin.org/get",
        params={
            "api_key": api_key,
            "city": "Mexico City",
        }
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"URL completa: {data['url']}")
    print(f"Params recibidos: {data['args']}")
    print("⚠️  Nota: la API key es visible en la URL — menos seguro que headers")


if __name__ == "__main__":
    demo_api_key_header()
    demo_bearer_token()
    demo_basic_auth()
    demo_query_param_key()