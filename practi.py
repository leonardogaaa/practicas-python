class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_informacion(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} unidades.")

# --- SOLUCIÓN ---

class Smartwatch(Producto):
    def __init__(self, nombre, precio, stock, sistema_operativo):
        # 1. Llamar al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, stock)
        # 2. Atributo específico
        self.sistema_operativo = sistema_operativo

    def sincronizar(self):
        """Método específico de Smartwatch."""
        print(f"Sincronizando el {self.nombre} con el sistema {self.sistema_operativo}...")


class Laptop(Producto):
    def __init__(self, nombre, precio, stock, ram_gb):
        # 1. Llamar al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, stock)
        # 2. Atributo específico
        self.ram_gb = ram_gb

    def obtener_informacion(self):
        """Sobreescribe el método del padre para añadir la RAM."""
        # 3. Llamar al método del padre para la información base
        super().obtener_informacion()
        print(f"  > Especificación: Memoria RAM de {self.ram_gb} GB.")

# --- PRUEBA DE EJECUCIÓN ---

if __name__ == "__main__":
    
    mi_reloj = Smartwatch("Samsung Galaxy Watch 5", 250, 15, "WearOS")
    mi_laptop = Laptop("MacBook Pro M3", 1999, 5, 18)

    print("--- Información del Smartwatch ---")
    mi_reloj.obtener_informacion()
    mi_reloj.sincronizar()

    print("\n--- Información de la Laptop ---")
    mi_laptop.obtener_informacion()
    
    # Verifica que la Laptop hereda los atributos base
    print(f"\nStock de la Laptop: {mi_laptop.stock}")