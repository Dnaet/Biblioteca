from categoria_libro import CategoriaLibro
from libro import Libro

class DetalleLibro:
    def __init__(self, id_detalle_libro, fecha_edicion, numero_paginas, id_categoria_libro,
                 cantidad_ejemplares, ejemplares_disponibles):
        self.id_detalle_libro = id_detalle_libro
        self.fecha_edicion = fecha_edicion
        self.numero_paginas = numero_paginas
        self.id_categoria_libro = id_categoria_libro 
        self.cantidad_ejemplares = cantidad_ejemplares
        self.ejemplares_disponibles = ejemplares_disponibles

    def info(self):
        return f"Detalle del Libro ID: {self.id_detalle_libro}, " \
               f"Fecha de Edición: {self.fecha_edicion}, " \
               f"Número de Páginas: {self.numero_paginas}, " \
               f"Categoría ID: {self.id_categoria_libro}, " \
               f"Cantidad de Ejemplares: {self.cantidad_ejemplares}, " \
               f"Ejemplares Disponibles: {self.ejemplares_disponibles}"

    def actualizar_disponibilidad(self, origen, cantidad):
        if origen == "retirar":
            if self.ejemplares_disponibles >= cantidad:
                self.ejemplares_disponibles -= cantidad
            else:
                print("No hay suficientes ejemplares disponibles para retirar.")
        elif origen == "devolver":
            self.ejemplares_disponibles += cantidad
