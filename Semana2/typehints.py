from typing import Optional

#nombre: str = "Angelo"
#edad: int = 36

#Typehints con funciones
def saludar(nombre: str, edad: int) -> str: 
    return f"Hola {nombre}, tienes {edad} años"

#Typehints con diccionarios
numeros: list[int] = [1, 2, 3, 4, 5]
edades: dict[str, int] = {"Angelo": 36, "Maria": 30, "Juan": 25}


name: str = "Corey"
age = 38

def create_user(first_name: str, last_name: str, age: Optional[int]) -> dict[str, str | int | None]:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email
    }
    
user1 = create_user("Corey", "Schafer", age=38)
user2 = create_user("Jane", "Doe")
print(user1)
print(user2)    



