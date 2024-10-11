class Tipo_Categoria:
    def __init__(self, id_tipo_categoria, tipo_categoria):
        self.id_tipo_categoria = id_tipo_categoria
        self.tipo_categoria = tipo_categoria

    def info(self):
        return f"Tipo de Categoría ID: {self.id_tipo_categoria}, Nombre: {self.tipo_categoria}"
