from typing import List, Dict, Tuple
from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido


class TiendaService:
    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: str = "") -> Usuario:
        if tipo.lower() == "cliente":
            user = Cliente(nombre, email, direccion)
        elif tipo.lower() == "administrador":
            user = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido")

        self.usuarios[user.id] = user
        return user

    def añadir_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> None:
        if producto_id in self.productos:
            del self.productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    def realizar_pedido(self, usuario_id: str, items: List[Tuple[str, int]]) -> Pedido:
        if usuario_id not in self.usuarios:
            raise ValueError("Usuario no encontrado")

        usuario = self.usuarios[usuario_id]
        if not isinstance(usuario, Cliente):
            raise ValueError("Solo los clientes pueden hacer pedidos")

        productos_pedido = {}
        for prod_id, cantidad in items:
            if prod_id not in self.productos:
                raise ValueError(f"Producto con id {prod_id} no encontrado")
            prod = self.productos[prod_id]
            if not prod.hay_stock(cantidad):
                raise ValueError(f"No hay suficiente stock para {prod.nombre}")
            productos_pedido[prod] = cantidad

        for prod, cantidad in productos_pedido.items():
            prod.actualizar_stock(cantidad)

        pedido = Pedido(usuario, productos_pedido)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_por_usuario(self, usuario_id: str) -> List[Pedido]:
        return [p for p in self.pedidos if p.cliente.id == usuario_id]
