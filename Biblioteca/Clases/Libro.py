from autor import Autor
from detalle_libro import DetalleLibro

class Libro:
    def __init__(self, titulo, isbn, id_autor, id_detalle_libro, id_categoria, id_editorial):
        self.titulo = titulo
        self.isbn = isbn
        self.id_autor = id_autor
        self.id_detalle_libro = id_detalle_libro
        self.id_categoria = id_categoria
        self.id_editorial = id_editorial

    def validar_isbn(self):
        return len(self.isbn) in [10, 13] and self.isbn.isdigit()

    def info(self):
        return f"Título: {self.titulo}, ISBN: {self.isbn}, Autor ID: {self.id_autor}, " \
               f"Detalle ID: {self.id_detalle_libro}, Categoría ID: {self.id_categoria}, " \
               f"Editorial ID: {self.id_editorial}"
