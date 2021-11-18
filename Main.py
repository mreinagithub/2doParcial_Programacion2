from pickle import FALSE
from SoporteInterfaz import *
from Clases.Cliente import Cliente
from Clases.Libro import Libro
from Clases.Prestamo import Prestamo

from FechaSistema import FechaSistema

#fechaSistema = FechaSistema.obtenerFecha()

clientes = []
libros = []
prestamos = []

def main():   

    opt = ""
    while True:        
        #bucle hasta que eliga salir del sistema
        opt = mostrarMenuPrincipal()
        if(opt == "0"):
            #decidió salir del sistema            
            print("\n")
            print("GRACIAS POR VISITAR MI PROGRAMA !!!")
            quit()   
        else:
            procesarSeleccion(opt)
            if usarPersistencia:
                util.guardarBD([fechaSistema.hoy, clientes, libros, prestamos])

    

def precargaDatos():
    
    #Libros
    libros.append(Libro("084-121-2310-12-1","El tránsito terreno","Plasencia, Juan Luis","Larrosa Mas, S.L.",8))
    libros.append(Libro("084-121-2311-13-2","Sistemas operativos","Bazilian Eric","GGG&G",15))
    libros.append(Libro("084-121-2312-14-3","Poemas intrínsecos","Llorens Antonia","Deloria Editores",10))
    libros.append(Libro("084-121-2313-15-4","Avances en Arquitectura","Richter, Helmut","TechniBooks",7))
    libros.append(Libro("084-121-2314-16-5","Historia de Occidente","Dulac, George","McCoy Hill",2))
    libros.append(Libro("084-121-2315-17-6","Procesadores cuánticos","Bazilian, Eric","Grisham Publishing",20))

    #Clientes
    clientes.append(Cliente(30780685,"Martin","Reina"))
    clientes.append(Cliente(31774115,"Adriana","Correa"))
    clientes.append(Cliente(6656108,"Luz Irene","Baleiron"))
    clientes.append(Cliente(25125878,"Bautista","Carvajal"))

    #Penalización de prueba sobre cliente Adriana Correa
    cli = clientes[1]
    cli.agregarPenalizacion(fechaSistema.hoy)

    #Prestamos
    cli = clientes[0]
    prestamos.append(Prestamo(cli, fechaSistema.hoy, [[libros[0],5],[libros[2],2]]))
    prestamos[0].confirmar()  

    cli = clientes[2]
    prestamos.append(Prestamo(cli,fechaSistema.hoy, [[libros[1],1],[libros[2],4]]))
    prestamos[1].confirmar()
    
  

def procesarSeleccion(opt):
    if(opt == "1"):
        modificarFechaSistema()

    if(opt == "2"):
        altaLibro(libros)
    
    if(opt == "3"):
        modificarLibro(libros, prestamos)

    if(opt == "4"):
        limpiarPantalla()
        print(obtenerTopEncabezado() + "############## TODOS LOS LIBROS #################" + obtenerPieEncabezado())
        for libro in libros:
            print(f"-> {libro}")
            print("------------------------------------------------------------------------------")
        esperarYVolver()
    if(opt == "5"):
        altaCliente(clientes)

    if(opt == "6"):
        limpiarPantalla()
        print(obtenerTopEncabezado() + "############# TODOS LOS CLIENTES ################" + obtenerPieEncabezado())
        for cliente in clientes:
            print(f"-> {cliente}")
            print("------------------------------------------------------------------------------")
        esperarYVolver()

    if (opt == "7"):
        nuevoPrestamo(clientes, libros, prestamos)

    if (opt == "8"):        
        devolverPrestamo(clientes)

    if (opt == "9"):
        limpiarPantalla()
        haySinDevolver = False
        print(obtenerTopEncabezado() + "############ PRESTAMOS NO DEVUELTOS #############" + obtenerPieEncabezado())
        for cli in clientes:
            sinDevolver = [prestamo for prestamo in cli.prestamos if prestamo.fechaDevolucionReal is None]
            if sinDevolver:
                haySinDevolver = True
                print(cli)
                for prestamo in sinDevolver:
                    print(f"--> {prestamo}")                    
                print("------------------------------------------------------------------------------")
            
        if not haySinDevolver: 
            print() 
            print("No hay prestamos sin devolver actualmente.")                       
        esperarYVolver()

    if (opt == "10"):
        limpiarPantalla()     
        hayPrestamos = False  
        print(obtenerTopEncabezado() + "############ HISTORIAL DE PRESTAMOS #############" + obtenerPieEncabezado()) 
        for cli in clientes:
            historial = [prestamo for prestamo in cli.prestamos]
            if historial:   
                hayPrestamos = True             
                print(cli)
                for prestamo in historial:
                    print(f"--> {prestamo}")                    
                print("------------------------------------------------------------------------------")
            
        if not hayPrestamos: 
            print()
            print("No hay prestamos realizados aún.")
        esperarYVolver()

    if (opt == "11"):
        limpiarPantalla()     
        hayPenalizaciones = False  
        print(obtenerTopEncabezado() + "########## PENALIZACIONES POR CLIENTE ###########" + obtenerPieEncabezado())  
        for cli in clientes:
            penalizaciones = [penalizacion for penalizacion in cli.penalizaciones]
            if penalizaciones:   
                hayPenalizaciones = True             
                print(cli)
                for penalizacion in penalizaciones:
                    print(f"--> {penalizacion}")                    
                print("------------------------------------------------------------------------------")
            
        if not hayPenalizaciones: 
            print()
            print("No hay penalizaciones aún.")
        esperarYVolver()

    if (opt == "12"):
        limpiarPantalla()
        print(obtenerTopEncabezado() + "############### LIBROS SIN STOCK ################" + obtenerPieEncabezado())  
        sinStock = [libro for libro in libros if libro.stock == 0]
        if not sinStock: 
            print()
            print("No hay libros sin stock actualmente.")
        else :
            print("Libros sin Stock:")
            for l in sinStock:
                print(f"-> {l}")
                print("------------------------------------------------------------------------------")
        esperarYVolver()

"""False, se maneja con memoria - True, usa persistencia en archivo con pickle"""
usarPersistencia = True


if __name__ == "__main__":
    
    if not usarPersistencia:
        precargaDatos()
    else:
        try:
            datosBD = util.abrirBD()
            fechaSistema.fijarFecha(datosBD[0])
            clientes = datosBD[1]
            libros = datosBD[2]
            prestamos = datosBD[3]
        except FileNotFoundError:
            precargaDatos()    
        except Exception as ex:
            print(f"Hubo un error al intentar levantar el archivo: {ex}")
            quit()

    main()



 



