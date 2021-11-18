
import datetime as dt

class Penalizacion():
    """Clase que contiene una penalizacion, es composición de cliente, está asociada a uno si o si"""

    def __init__(self, fecha):
        self.fecha = fecha
        self.fechaFin = (fecha + dt.timedelta(days=7))

    def __str__(self):
        #Mostramos información de la penalizacion
        return (f"Fecha Desde: {self.fecha} | Fecha Hasta: {self.fechaFin}")

    def estaVigente(self, hoy):
        return self.fechaFin >= hoy
