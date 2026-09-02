import asyncio
from app.clients.github_client import GitHubClient
from app.clients.jsonplaceholder import JSONPlaceholderClient
from app.clients.weather_client import WeatherClient
from app.clients.httpbin import HttpBinClient
from app.clients.countries import Countries

async def main() -> None:
    github = GitHubClient()
    placeholder = JSONPlaceholderClient()

    # Concurrent requests with asyncio.gather
    user, repos, posts = await asyncio.gather(
        github.get_user("torvalds"),
        github.get_user_repos("torvalds", per_page=3),
        placeholder.get_posts(user_id=1),
    )

    print(f"\n--- GitHub User ---")
    print(f"Name: {user['name']}")
    print(f"Public repos: {user['public_repos']}")

    print(f"\n--- Top Repos ---")
    for repo in repos:
        print(f"  - {repo['name']} ({repo['stargazers_count']} stars)")

    print(f"\n--- Posts (User 1) ---")
    for post in posts[:3]:
        print(f"  - {post['title'][:50]}...")

    # POST demo
    new_post = await placeholder.create_post(
        title="Test from REST Client",
        body="This post was created by our Python client",
        user_id=1,
    )
    print(f"\n--- Created Post ---")
    print(f"ID: {new_post['id']}, Title: {new_post['title']}")

    # Weather (optional, requires API key)
    try:
        weather = WeatherClient()
        data = await weather.get_weather("Mexico City")
        print(f"\n--- Weather ---")
        print(f"City: {data['name']}, Temp: {data['main']['temp']}°C")
    except Exception as e:
        print(f"\n--- Weather (skipped) ---")
        print(f"Could not fetch weather: {e}")


    countries = Countries()
    print("\n--- REST Countries ---")
    try:
        data = await countries.get_country_by_name("Canada")

        if not data:
            print("No se recibieron datos del país.")
        else:
            pais = data[0] if isinstance(data, list) and len(data) > 0 else data
            
            # Nombre común
            nombre_data = pais.get("name")
            nombre = nombre_data.get("common", "Desconocido") if isinstance(nombre_data, dict) else "Desconocido"
            
            # Capital
            capitales = pais.get("capital", ["N/A"])
            capital = capitales[0] if isinstance(capitales, list) and len(capitales) > 0 else str(capitales)
            
            # Población
            poblacion = pais.get("population", 0)

            print(f"País: {nombre} | Capital: {capital} | Población: {poblacion:,}")

    except Exception as e:
        print(f"Error al consultar país: {e}")


    httpbin = HttpBinClient()

    print("\n========================================")
    print("4. PRUEBA DE ERRORES CON HTTPBIN (safe_get)")
    print("========================================")
    print("Probando error 404 (Not Found):")
    await httpbin.safe_get("/status/404")

    print("\nProbando error 500 (Internal Server Error):")
    await httpbin.safe_get("/status/500")

    print("\nProbando Timeout (el cliente tiene timeout=2s y pedimos retraso de 4s):")
    await httpbin.safe_get("/delay/4")
    

if __name__ == "__main__":
    asyncio.run(main())