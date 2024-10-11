import autor

class Libro:
    def __init__(self, isbn: str, titulo: str, autor: autor.Autor):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor  # Almacena una instancia de Autor

    def validar_isbn(self) -> bool:
        if 10 <= len(self._isbn) <= 13 and self._isbn.isdigit():
            return True
        else:
            return False  # Considera lanzar una excepción o imprimir un mensaje de error

    def get_info(self) -> str:
        return f"{self._titulo} (ISBN: {self._isbn}) - Autor: {self._autor.nombre_autor if self._autor else 'Desconocido'}"
