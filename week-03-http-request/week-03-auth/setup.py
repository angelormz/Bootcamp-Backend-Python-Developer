# Ejecuta esto para crear los archivos de setup
from pathlib import Path

# .env.example (template — SÍ se commitea)
Path(".env.example").write_text(
    "# API Keys — copia este archivo a .env y agrega tus valores\n"
    "OPENWEATHER_API_KEY=tu-api-key-aqui\n"
    "APP_NAME=WeatherClient\n"
    "APP_DEBUG=true\n"
)

# .env (valores reales — NO se commitea)
Path(".env").write_text(
    "# Secretos reales — NUNCA commitear\n"
    "OPENWEATHER_API_KEY=demo_key_para_pruebas\n"
    "APP_NAME=WeatherClient\n"
    "APP_DEBUG=true\n"
)

# .gitignore
Path(".gitignore").write_text(
    ".env\n"
    ".env.local\n"
    ".env.production\n"
    "__pycache__/\n"
    "*.pyc\n"
    "venv/\n"
    ".venv/\n"
)

print("Archivos creados: .env.example, .env, .gitignore")