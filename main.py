from services.Tienda_service import TiendaService
from models.Producto import ProductoElectronico, ProductoRopa, Producto

def main() -> None:
    tienda = TiendaService()

    # Crear usuarios
    c1 = tienda.registrar_usuario("cliente", "Álvaro Garcia", "alvaro@example.com", "Calle Falsa 123")
    c2 = tienda.registrar_usuario("cliente", "Javier Ruiz", "javi@example.com", "Av. Inventada 5")
    c3 = tienda.registrar_usuario("cliente", "Marta Hernández", "marta@example.com", "Plaza Mayor 1")
    admin = tienda.registrar_usuario("administrador", "Admin", "admin@tienda.com")

    # Crear productos
    p1 = ProductoElectronico("Smartphone X", 399.99, 10, garantia_meses=24)
    p2 = ProductoElectronico("Auriculares Pro", 89.50, 25, garantia_meses=12)
    p3 = Producto("Tarjeta regalo 50€", 50.0, 100)
    p4 = ProductoRopa("Camiseta Básica", 12.99, 50, talla="M", color="Blanco")
    p5 = ProductoRopa("Chaqueta Invierno", 79.90, 5, talla="L", color="Negro")

    for p in (p1, p2, p3, p4, p5):
        tienda.añadir_producto(p)

    print("=== Inventario inicial ===")
    for prod in tienda.listar_productos():
        print(prod)

    # Hacer pedidos
    pedido1 = tienda.realizar_pedido(c1.id, [(p1.id, 1), (p4.id, 2)])
    pedido2 = tienda.realizar_pedido(c2.id, [(p2.id, 2), (p3.id, 1)])
    pedido3 = tienda.realizar_pedido(c3.id, [(p4.id, 1), (p5.id, 1), (p3.id, 2)])

    print("\n=== Pedidos realizados ===")
    print(pedido1, "\n---")
    print(pedido2, "\n---")
    print(pedido3)

    print(f"\n=== Historial de pedidos de {c1.nombre} ===")
    for p in tienda.listar_pedidos_por_usuario(c1.id):
        print(p)

    print("\n=== Stock después de pedidos ===")
    for prod in tienda.listar_productos():
        print(prod)

if __name__ == "__main__":
    main()
