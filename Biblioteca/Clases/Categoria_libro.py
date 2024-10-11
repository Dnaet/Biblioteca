class CategoriaLibro:
    def __init__(self, id_categoria, nombre_categoria):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria

    def consulta_categoria(self):
        return f"Categoría ID: {self.id_categoria}, Nombre: {self.nombre_categoria}"
