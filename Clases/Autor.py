from datetime import datetime

class Autor:
    def __init__(self, id_autor, nombre_autor, biografia_autor, foto_autor,
                 seudonimo_autor, fecha_nac, fecha_def=None):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor
        self.seudonimo_autor = seudonimo_autor
        self.fecha_nac = self.convertir_formato(fecha_nac)
        self.fecha_def = self.convertir_formato(fecha_def) if fecha_def else None

    def info(self):
        return f"Autor: {self.nombre_autor} (Seudónimo: {self.seudonimo_autor})\n" \
               f"Biografía: {self.biografia_autor}\n" \
               f"Fecha de Nacimiento: {self.fecha_nac}\n" \
               f"Fecha de Defunción: {self.fecha_def if self.fecha_def else 'Vivo'}"

    def convertir_formato(self, fecha):
        try:
            fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
            return fecha_dt.strftime('%Y-%m-%d')
        except ValueError:
            return "Fecha no válida"
