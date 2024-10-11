class Paises:
    def __init__(self, cod_pais, nombre_pais, gentilicio_pais, cod_iso):
        self.cod_pais = cod_pais
        self.nombre_pais = nombre_pais
        self.gentilicio_pais = gentilicio_pais
        self.cod_iso = cod_iso

    def info(self):
        return f"País: {self.nombre_pais}, Código: {self.cod_pais}, " \
               f"Gentilicio: {self.gentilicio_pais}, Código ISO: {self.cod_iso}"
