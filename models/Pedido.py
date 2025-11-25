import uuid
from datetime import datetime
from typing import Dict

from models.Usuario import Cliente
from models.Producto import Producto


class Pedido:
    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]):
        self.id = str(uuid.uuid4())
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.productos.items())

    def __str__(self) -> str:
        productos_str = "\n".join([f"{p.nombre} x {c}" for p, c in self.productos.items()])
        return (
            f"Pedido ID: {self.id}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Productos:\n{productos_str}\n"
            f"Total: {self.calcular_total():.2f}€"
        )
