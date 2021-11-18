
from Clases.Penalizacion import Penalizacion

class Cliente():
    """Clase Cliente de la Librería, este puede ser asociado a N prestamos y contiene su historial de penalizaciones"""

    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.penalizaciones = []
        self.prestamos = []
    
    def __eq__(self, otro):
        if (isinstance(otro, Cliente)):
            return self.dni == otro.dni
        else: return False

    def __str__(self):
        #Mostramos información del cliente
        return (f"DNI: {self.dni} | Nombre: {self.nombre} | Apellido: {self.apellido}")                
        
    def agregarPenalizacion(self, fecha):
        self.penalizaciones.append(Penalizacion(fecha))

    def agregarPrestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def tienePenalizacionVigente(self, hoy):
        return any(p.estaVigente(hoy) == True for p in self.penalizaciones)

    def obtenerMaximaFechaPenalizacion(self):
        return max(p.fechaFin for p in self.penalizaciones)
    

    