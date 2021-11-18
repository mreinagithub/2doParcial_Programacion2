
class Libro():

    """Clase que representa un Libro de la Libreria con su cantidad de ejemplares"""

    def __init__(self, isbn, titulo, autor, editorial, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ejemplares = ejemplares
        self.stock = self.ejemplares
        
    def __eq__(self, otro):
        if (isinstance(otro, Libro)):
            return self.isbn == otro.isbn
        else: return False
    
    def __str__(self):
        #Mostramos información del libro
        return (f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} | Editorial: {self.editorial}"
                f" | Ejemplares: {self.ejemplares} | Stock: {self.stock}")

    def prestar(self, qEjemplares):        
        
        try:
            if self.haySuficientesEjemplares(qEjemplares):         
                self.stock -= qEjemplares
            else: raise ValueError("No tiene suficientes ejemplares para satisfacer el pedido")
        except ValueError as ex:
            raise ex        

    def devolver(self, qEjemplares):
        self.stock += qEjemplares

    def haySuficientesEjemplares(self, qEjemplares):
        if qEjemplares > self.stock: return False
        else: return True

    def modificarCantidadEjemplares(self, qEjemplares):
        dif = self.ejemplares - qEjemplares
        self.stock -= dif
        self.ejemplares = qEjemplares