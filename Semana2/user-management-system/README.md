User Management System

## Stack Tecnológico

* Lenguaje: Python 3.11+
* Type checking: mypy
* HTTP (async demo): httpx
* Sin frameworks web - Python puro

## Funcionalidades

* Creación de usuarios
* Manejo de roles con Enum
* Validación de usuarios duplicados
* Búsqueda y desactivación de usuarios
* Actualización de roles
* Excepciones personalizadas:

  * UserNotFoundError
  * DuplicateUserError
  * InvalidRoleError

* Uso de @dataclass
* Type hints
* Programación asíncrona con asyncio
* Concurrencia con asyncio.gather()
* Decoradores personalizados

## Estructura del proyecto

user-management-system/
├── app/
│   ├── __init__.py
│   ├── main.py                  
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py              
│   │   └── exceptions.py        
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py      
│   └── utils/
│       ├── __init__.py
│       └── decorators.py        
├── pyproject.toml
└── README.md

## Instalación

Crear un entorno virtual:

bash
python3 -m venv .venv

Activarlo en macOS/Linux:

bash
source .venv/bin/activate

Instalar mypy:

bash
python -m pip install mypy

## Ejecución

Desde la carpeta raíz del proyecto:

bash
python -m app.main

Salida esperada aproximada:

- Usuarios creados correctamente
- DuplicateUserError capturado
- UserNotFoundError capturado
- InvalidRoleError capturado
- Resultados async: {'admin@test.com': True, 'editor@test.com': True, 'invalid': False}

## Validación de tipos

Ejecutar:

bash
python -m mypy app/

Resultado esperado:

Success: no issues found in 9 source files

## Conceptos utilizados

Este proyecto demuestra el uso de:

* dataclasses
* Enum
* type hints
* excepciones personalizadas
* decoradores
* servicios y modelos
* async / await
* asyncio.gather()
* asyncio.run()
