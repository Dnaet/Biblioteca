from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id_prestamo, id_detalle_libro, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto=None, cantidad_solicitada=1):
        self.id_prestamo = id_prestamo
        self.id_detalle_libro = id_detalle_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad_solicitada = cantidad_solicitada

    def sumar_dias(self, dias):
        fecha_dt = datetime.strptime(self.fecha_prestamo, '%Y-%m-%d')
        fecha_dt += timedelta(days=dias)
        return fecha_dt.strftime('%Y-%m-%d')

    def calcular_fecha(self):
        return self.sumar_dias(5)  
    def marcar_devuelto(self):
        self.fecha_devuelto = datetime.now().strftime('%Y-%m-%d')  
    
