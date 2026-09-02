import httpx
from typing import Any

class BaseClient:
    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.base_url = base_url
        self.timeout = timeout

    async def get(self, endpoint: str, params: dict[str, Any] | None = None, #El argumento puede ser un diccionario o un None. El valor por defecto = None hace que el parámetro sea opcional.
                  headers: dict[str, str] | None = None) -> dict[str, Any]: #Por estándar del protocolo HTTP, tanto las cabeceras como sus valores de headers HTTP sus valores son siempre cadenas de texto plano
        # Query Params / JSON Body: En los parámetros de URL o en el cuerpo JSON, los valores pueden ser enteros, booleanos, listas o strings por lo que se tipan con Any.
        async with httpx.AsyncClient(timeout=self.timeout, follow_redirects=True) as client:
            # Conext Manager (async with httpx.AsyncClient(..) para abrir y cerrar la sesión HTTP de forma limpia y eficiente)
            response = await client.get(
                f"{self.base_url}{endpoint}", #Concatenan la URL base con el endopoint relativo
                params=params,
                headers=headers,
            )
            response.raise_for_status() # Verifica el código de estado HTTP. Si la API responde con un error 4xx o 5xx, interrumpe el flujo y lanza una excepción en lugar de continuar con datos inválidos.
            return response.json() # Convierte el cuerpo de la respuesta JSON a un diccionario de Python y lo retorna al llamador.


    async def safe_get(self, endpoint: str, params: dict | None = None,
                        headers: dict | None = None,):
            try:
                return await self.get(endpoint, params=params, headers=headers)
            except httpx.TimeoutException:
                print(f"[TIMEOUT] {endpoint} no respondió dentro del límite configurado.")
                return None
            except httpx.HTTPStatusError as e:
                print(f"[HTTP {e.response.status_code}] Error en {endpoint}: {e.response.text[:100]}")
                return None
            except httpx.ConnectError:
                print(f"[CONNECTION] Error de conexión de red hacia {endpoint}.")
                return None
            except Exception as e:
                print(f"[ERROR] Excepción inesperada en {endpoint}: {e}")
                return None    


    async def post(self, endpoint: str, data: dict[str, Any],
                   headers: dict[str, str] | None = None) -> dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout ,follow_redirects=True) as client:
            response = await client.post(
                f"{self.base_url}{endpoint}",
                json=data,
                headers=headers,
            )
            response.raise_for_status()
            return response.json()


    