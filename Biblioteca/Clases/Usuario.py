import re
from tipo_usuario import Tipo_Usuario
from rut_chile import rut_chile


class Usuario:
    def __init__(self, id_usuario, nombre_usuario, correo_usuario, telefono_usuario, rut_usuario, id_tipo_usuario, habilitado, fecha_creacion):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.rut_usuario = rut_usuario
        self.id_tipo_usuario = id_tipo_usuario
        self.habilitado = habilitado
        self.fecha_creacion = fecha_creacion

    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)

    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.fullmatch(regex, self.correo_usuario) is not None

    def info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre_usuario}, Correo: {self.correo_usuario}, " \
               f"Teléfono: {self.telefono_usuario}, RUT: {self.rut_usuario}, " \
               f"Tipo ID: {self.id_tipo_usuario}, Habilitado: {self.habilitado}, " \
               f"Fecha de Creación: {self.fecha_creacion}"
