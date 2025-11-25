import uuid

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        self.stock -= cantidad

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio}€ - Stock: {self.stock}"


class ProductoElectronico(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int):
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio}€ - Stock: {self.stock} - Garantía: {self.garantia_meses} meses"


class ProductoRopa(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio}€ - Stock: {self.stock} - Talla: {self.talla} - Color: {self.color}"
