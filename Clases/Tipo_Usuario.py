class Tipo_Usuario:
    def __init__(self, id_tipo_usuario, tipo_usuario, descripcion_tipo_usuario):
        self.id_tipo_usuario = id_tipo_usuario
        self.tipo_usuario = tipo_usuario
        self.descripcion_tipo_usuario = descripcion_tipo_usuario

    def info(self):
        return f"Tipo de Usuario ID: {self.id_tipo_usuario}, Tipo: {self.tipo_usuario}, Descripción: {self.descripcion_tipo_usuario}"
