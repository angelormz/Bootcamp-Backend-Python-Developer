# config.py — Módulo reutilizable de configuración
import os
import sys
from dotenv import load_dotenv


class Config:
    """Configuración de la aplicación cargada desde variables de entorno."""
    
    def __init__(self):
        load_dotenv()
        
        self.openweather_api_key = os.environ.get("OPENWEATHER_API_KEY", "")
        self.app_name = os.environ.get("APP_NAME", "MyApp")
        self.debug = os.environ.get("APP_DEBUG", "false").lower() == "true"
    
    def validate(self, required: list[str] | None = None) -> None:
        """Verifica que las variables requeridas estén presentes."""
        required = required or []
        missing = []
        
        for var_name in required:
            attr_name = var_name.lower()
            value = getattr(self, attr_name, None)
            if not value:
                missing.append(var_name)
        
        if missing:
            print(f"ERROR: Variables faltantes: {', '.join(missing)}")
            print("Solución: copia .env.example a .env y agrega tus valores")
            print("  cp .env.example .env")
            sys.exit(1)
    
    def __repr__(self) -> str:
        key_preview = f"{self.openweather_api_key[:8]}..." if self.openweather_api_key else "NO SET"
        return (
            f"Config(app={self.app_name}, debug={self.debug}, "
            f"api_key={key_preview})"
        )


# Singleton: una sola instancia de configuración
config = Config()