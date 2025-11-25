import uuid

class Usuario:
    def __init__(self, nombre: str, email: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email

    def is_admin(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"{self.nombre} ({self.email})"


class Cliente(Usuario):
    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)
        self.direccion = direccion


class Administrador(Usuario):
    def is_admin(self) -> bool:
        return True
