class Biblioteca:
    def __init__(self, id_biblioteca, nombre_biblioteca, direccion_biblioteca, telefono_biblioteca):
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.direccion_biblioteca = direccion_biblioteca
        self.telefono_biblioteca = telefono_biblioteca

    def buscar_libro(self, isbn):
        pass  # Implementación para buscar un libro por ISBN

    def devolver_libro(self, libro):
        pass  # Implementación para devolver un libro

    def prestar_libro(self, libro, usuario):
        pass  # Implementación para prestar un libro a un usuario

    def info(self):
        return f"Biblioteca: {self.nombre_biblioteca}, Dirección: {self.direccion_biblioteca}, Teléfono: {self.telefono_biblioteca}"
