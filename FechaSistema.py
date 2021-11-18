
import datetime as dt

class FechaSistema():
    """Clase que se usa como fecha actual del sistema, proposito de pruebas
       Al usar esta fecha se puede manipular 'hoy' para simular penalizaciones, impedimentos de carga, etc."""    

    def __init__(self):
        self.hoy = dt.datetime.today().date()

    def agregarDia(self, dias):
        self.hoy = (self.hoy + dt.timedelta(days=dias))

    def fijarFecha(self, fecha):
        #Solo establecemos una fecha diferente a hoy si dicha fecha es futura.
        if fecha >= self.hoy:
            self.hoy = fecha
    
    __fechaSistema = None

    @staticmethod
    def obtenerFecha():
        if FechaSistema.__fechaSistema is None:
            FechaSistema.__fechaSistema = FechaSistema()
        return FechaSistema.__fechaSistema

    
