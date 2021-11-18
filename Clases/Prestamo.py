
import datetime

from Clases.PrestamoItem import PrestamoItem

class Prestamo():

    """Clase que respresenta un prestamo en el sistema"""

    #Cantidad de días prefijado para la devolución de un préstamo a término
    __diasDevolucion = 5  

    def __init__(self, cliente, fPrestamo, items):
        self.cliente = cliente
        self.fechaPrestamo = fPrestamo
        self.fechaDevolucionEsperada = (fPrestamo + datetime.timedelta(days=self.__diasDevolucion))
        self.fechaDevolucionReal = None
        self.items = []       
        for item in items:
            try:                                        
                self.items.append(PrestamoItem(item[0], item[1]))
            except ValueError as ex:
                raise f"No puede cargar este prestamo. Error en libro {item[0]}: {ex}"

    def __str__(self):
        #Mostramos información del préstamo
        empty_string = ""
        ejemplares = "\n    ".join([i.libro.isbn + " " + i.libro.titulo + " - Ejemplares: " + str(i.cantidad) for i in self.items])
        #return (f"Cliente: {self.cliente} | Fecha: {self.fechaPrestamo} | Devolución esperada: {self.fechaDevolucionEsperada} | F.Devolución: {self.fechaDevolucionReal}\nLibros:\n{ejemplares}")
        return (f"Fecha: {self.fechaPrestamo} | Devolución esperada: {self.fechaDevolucionEsperada} | F.Devolución: {empty_string if not self.fechaDevolucionReal else self.fechaDevolucionReal}\n    Libros:\n    {ejemplares}")

    
    def devolver(self, fechaDevolucion):

        if(self.fechaDevolucionReal is not None):
            print("El prestamo ya fue devuelto")
            return

        self.fechaDevolucionReal = fechaDevolucion
        if self.fechaDevolucionReal > self.fechaDevolucionEsperada:
            self.cliente.agregarPenalizacion(fechaDevolucion)
        
        [i.libro.devolver(i.cantidad) for i in self.items]

    def confirmar(self):
        
        self.cliente.agregarPrestamo(self)

        [i.libro.prestar(i.cantidad) for i in self.items]


