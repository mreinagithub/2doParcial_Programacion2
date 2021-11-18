
import re

class Utilidades:


    @staticmethod
    def validarISBN(valor):
        resu = re.match("^\d{3}-\d{3}-\d{4}-\d{2}-\d{1}$",valor)
        if resu : return True
        else: return False

    @staticmethod
    def validarDNI(valor):
        resu = re.match("^\d{7,8}$",valor)
        if resu : return True
        else: return False

    @staticmethod
    def obtenerCantidadConPrestamoVigente(prestamos, libro):

        qPrestados = 0
        for prestamo in [prestamo for prestamo in prestamos if prestamo.fechaDevolucionReal is None]:
            qPrestados += sum([item.cantidad for item in prestamo.items if item.libro.isbn == libro.isbn])

        return qPrestados


    @staticmethod
    def guardarBD(listas):
        import pickle
        with open("Libreria.pickle", "wb") as a:
            pickle.dump(listas, a)
        

    @staticmethod
    def abrirBD():
        import pickle
        with open("Libreria.pickle", "rb") as a:        
            listas = pickle.load(a)
        return listas

    