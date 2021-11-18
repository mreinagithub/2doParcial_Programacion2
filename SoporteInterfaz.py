
import re
from Clases.Libro import Libro
from Clases.Cliente import Cliente
from Clases.Prestamo import Prestamo
from Utilidades import Utilidades as util

from FechaSistema import FechaSistema

fechaSistema = FechaSistema.obtenerFecha()

def obtenerTopEncabezado():
    return "#################################################\n"

def obtenerPieEncabezado():
    return f"\n########### Fecha Actual: {fechaSistema.hoy} ############\n#################################################"


def mostrarMenuPrincipal():
    limpiarPantalla()
    menu = ("Modificar Fecha del sistema (para pruebas de funcionalidad como penalizaciones)", "Alta de Libro", "Modificación de Libro", "Mostrar Libros", "Alta Cliente", "Mostrar Clientes",
            "Nuevo Préstamo", "Devolución de préstamo", "Listar prestamos sin devolver por cliente", "Historial de préstamos por cliente",
            "Mostrar penalizaciones por cliente","Mostrar libros sin stock físico") 
    encabezado = (obtenerTopEncabezado() + "######## MENU PRINCIPAL LIBRERÍA PROG 2 #########" + obtenerPieEncabezado())
    opcionSalida = "Salir del sistema"
    textoInput = "Seleccione la opción deseada:"

    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione una opción:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    return opt;

def modificarFechaSistema():
    limpiarPantalla()             
    dias = None
    while(dias is None):
        print(obtenerTopEncabezado() + f"########## MODIFICAR FECHA DEL SISTEMA ##########" + obtenerPieEncabezado())
        dias = procesarYValidarInput("Indique la cantidad de días que desea agregar (0 para cancelar): ",int)
        if(dias is not None):
            if(dias == "0"): return
            if(dias < 0): 
                print("La cantidad de días debe ser un valor positivo")
                dias = None
            else:
                fechaSistema.agregarDia(dias)
                print(f"Fecha del sistema modificada.\nNueva fecha Actual: {fechaSistema.hoy}")
                esperarYVolver()

def altaLibro(libros):
    limpiarPantalla()
    #Variables
    isbn = None
    titulo = None 
    autor = None 
    editorial = None
    qEjemplares = None   
    print(obtenerTopEncabezado() + "################ ALTA DE LIBRO ##################" + obtenerPieEncabezado())  
    while(isbn is None):
        isbn = procesarYValidarInput("Indique el ISBN del Libro -Formato necesario: '999-999-9999-99-9' - (0 para cancelar): ",str)
        if(isbn is not None):
            if(isbn == "0"): return
            if(not util.validarISBN(isbn)): 
                print("Valor ISBN inválido.")
                isbn = None
            elif(any([l.isbn == isbn for l in libros])):
                print("El ISBN ingresado ya existe.")
                isbn = None  
    while(titulo is None):
        titulo = procesarYValidarInput("Indique el TÍTULO del Libro (0 para cancelar): ",str)
        if(titulo is not None):
            if(titulo == "0"): return
            if(len(titulo) < 3): 
                print("El título debe tener al menos 3 caractéres")
                titulo = None
    while(autor is None):
        autor = procesarYValidarInput("Indique el AUTOR del Libro (0 para cancelar): ",str)
        if(autor is not None):
            if(autor == "0"): return
            if(len(autor) < 3): 
                print("El autor debe tener al menos 3 caractéres")
                autor = None     
    while(editorial is None):
        editorial = procesarYValidarInput("Indique la EDITORIAL del Libro (0 para cancelar): ",str)
        if(editorial is not None):
            if(editorial == "0"): return
            if(len(editorial) < 3): 
                print("La editorial debe tener al menos 3 caractéres")
                editorial = None 
    while(qEjemplares is None):            
        qEjemplares = procesarYValidarInput(f"Indique la cantidad de EJEMPLARES disponibles (0 para cancelar): ",int)
        if(qEjemplares is not None):
            if(qEjemplares == "0"): return
            if(qEjemplares <= 0): 
                print("No puede cargar una cantidad cero o inferior.")
                qEjemplares = None           
    
    nuevoLibro = Libro(isbn, titulo, autor, editorial, qEjemplares)

    if(nuevoLibro is not None):
        print("-------------------------------")
        print("Libro dado de alta -->")
        print(nuevoLibro)
        libros.append(nuevoLibro)
        esperarYVolver()

def modificarLibro(libros, prestamos):
    limpiarPantalla()
    #Variables
    libro = None    
    titulo = None
    autor = None
    editorial = None
    qEjemplares = None
    #Inputo de datos   
    lstLibros = sorted(libros, key = lambda c: c.titulo)
    menu = [lc.isbn + " - " +  lc.titulo + " - Total Ejemplares: " + str(lc.ejemplares) for lc in lstLibros]    
    encabezado = obtenerTopEncabezado() + "############ MODIFICACION DE LIBRO ##############" + obtenerPieEncabezado()  
    opcionSalida = "Cancelar modificación"
    textoInput = "Seleccione el libro que desea modificar:"
    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione una opción de menú válida:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    if(opt == "0"): return
    libro = lstLibros[int(opt)-1]   
    limpiarPantalla()
    print(obtenerTopEncabezado() + "############ MODIFICACION DE LIBRO ##############" + obtenerPieEncabezado()  )
    print(libro)
    while(titulo is None):
        titulo = procesarYValidarInput("Indique el NUEVO TÍTULO del Libro (0 para cancelar o deje vacío para no realizar cambios en el título): ",str,True)
        if(titulo is None): break
        if(titulo == "0"): return
        if(len(titulo) < 3): 
            print("El título debe tener al menos 3 caractéres")
            titulo = None
    while(autor is None):
        autor = procesarYValidarInput("Indique el NUEVO AUTOR del Libro (0 para cancelar o deje vacío para no realizar cambios en el autor): ",str, True)
        if(autor is None): break
        if(autor == "0"): return
        if(len(autor) < 3): 
            print("El autor debe tener al menos 3 caractéres")
            autor = None             
    while(editorial is None):
        editorial = procesarYValidarInput("Indique la NUEVA EDITORIAL del Libro (0 para cancelar o deje vacío para no realizar cambios en la editorial): ",str, True)
        if(editorial is None): break
        if(editorial == "0"): return
        if(len(editorial) < 3): 
            print("La editorial debe tener al menos 3 caractéres")
            editorial = None 
    while(qEjemplares is None):            
        qEjemplares = procesarYValidarInput(f"Indique la NUEVA CANTIDAD DE EJEMPLARES disponibles (deje vacío para no realizar cambios en la cantidad): ",int,True,True)
        if(qEjemplares is None): break        
        if(qEjemplares < 0): 
            print("No puede cargar una cantidad inferior a cero.")
            qEjemplares = None   
        else: 
            qFueraDeStock = util.obtenerCantidadConPrestamoVigente(prestamos, libro)
            if (qFueraDeStock > qEjemplares):
                print(f"No puede establecer menos cantidad de ejemplares que los que tiene prestados actualmente. Cantidad prestados: {qFueraDeStock}")
                qEjemplares = None   

    libro.titulo = libro.titulo if not titulo else titulo
    libro.autor = libro.autor if not autor else autor
    libro.editorial = libro.editorial if not editorial else editorial
    if qEjemplares is not None : 
        libro.modificarCantidadEjemplares(qEjemplares)

    print()
    print("Libro modificado:")
    print(libro)
    esperarYVolver()

def altaCliente(clientes):
    limpiarPantalla()
    #Variables
    dni = None
    nombre = None 
    apellido = None     
    print(obtenerTopEncabezado() + "############### ALTA DE CLIENTE #################" + obtenerPieEncabezado()  )
    while(dni is None):
        dni = procesarYValidarInput("Indique DNI del Cliente -Debe tener entre 7 y 8 dígitos- (0 para cancelar): ",str)
        if(dni is not None):
            if(dni == "0"): return
            if(not util.validarDNI(dni)): 
                print("Valor DNI inválido.")
                dni = None
            elif(any([c.dni == dni for c in clientes])):
                print("El DNI ingresado ya existe.")
                dni = None  
    while(nombre is None):
        nombre = procesarYValidarInput("Indique el NOMBRE del Cliente (0 para cancelar): ",str)
        if(nombre is not None):
            if(nombre == "0"): return
            if(len(nombre) < 3): 
                print("El nombre debe tener al menos 3 caractéres")
                nombre = None
    while(apellido is None):
        apellido = procesarYValidarInput("Indique el APELLIDO del Cliente (0 para cancelar): ",str)
        if(apellido is not None):
            if(apellido == "0"): return
            if(len(apellido) < 3): 
                print("El apellido debe tener al menos 3 caractéres")
                apellido = None        
    
    nuevoCliente = Cliente(dni, nombre, apellido)

    if(nuevoCliente is not None):
        print("-------------------------------")
        print("Cliente dado de alta -->")
        print(nuevoCliente)
        clientes.append(nuevoCliente)
        esperarYVolver()
                
def nuevoPrestamo(clientes, libros, prestamos):
    limpiarPantalla()
    #Variables
    cliente = None    
    librosElegidos = []    
    #Inputo de datos   
    lstClientes = sorted(clientes, key = lambda c: c.apellido)
    menu = [lc.apellido + ", " +  lc.nombre for lc in lstClientes]    
    encabezado = obtenerTopEncabezado() + "############### ALTA DE PRESTAMO ################" + obtenerPieEncabezado()  
    opcionSalida = "Cancelar préstamo"
    textoInput = "Seleccione el cliente deseado:"
    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione una opción de menú válida:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    if(opt == "0"): return
    cliente = lstClientes[int(opt)-1]      
    if(cliente.tienePenalizacionVigente(fechaSistema.hoy)):        
        limpiarPantalla()      
        print(obtenerTopEncabezado() + "############### ALTA DE PRESTAMO ################" + obtenerPieEncabezado())
        print(f"\nCliente -----> {cliente}\n")        
        print(f"El cliente está penalizado hasta el {cliente.obtenerMaximaFechaPenalizacion()}. No puede gestionar el préstamo.")
        esperarYVolver()
    else:
        encabezado = obtenerTopEncabezado() + "############### ALTA DE PRESTAMO ################" + obtenerPieEncabezado() + f"\nCliente -----> {cliente}\nLibros a prestar:"        
        textoInput = "Seleccione el libro deseado:"
        opcionSalida = "Finalizar carga"        
        opt = ""
        while opt != "0":
            limpiarPantalla()  
            filtro = [l for l in libros if l not in [le[0] for le in librosElegidos]]    
            lstLibros = sorted(filtro, key = lambda l: l.titulo)
            menu = [lc.isbn + " - " +  lc.titulo + " - Stock: " + str(lc.stock) for lc in lstLibros]            
            opt = generarPantalla(encabezado,menu,opcionSalida,textoInput)
            while not opt.isdigit() or len(menu) < int(opt):
                textoInput = "La opción ingresada es incorrecta. Seleccione una opción de menú válida:"
                limpiarPantalla()
                opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
            if(opt != "0"):
                libro = lstLibros[int(opt)-1] 
                qEjemplares = None
                if libro.stock == 0: input("El libro seleccionado NO tiene stock. Presione cualquier tecla para continuar.")
                else:
                    while(qEjemplares is None):            
                        qEjemplares = procesarYValidarInput(f"{libro}\nIndique la cantidad de EJEMPLARES a prestar (0 para cancelar este libro): ",int)
                        if(qEjemplares is not None):                    
                            if(qEjemplares == "0"): break
                            if(qEjemplares < 0): 
                                print("No puede cargar una cantidad cero o inferior.")
                                qEjemplares = None       
                            elif not libro.haySuficientesEjemplares(qEjemplares):
                                print("No ya suficientes ejemplares para satisfacer la demanda.")
                                qEjemplares = None                   
                    if qEjemplares != "0":
                        librosElegidos.append([libro,qEjemplares])            

        if not librosElegidos:
            print("No puede generar un préstamo sin libros")
            esperarYVolver()
        else:
            limpiarPantalla()
            prestamo = Prestamo(cliente, fechaSistema.hoy, librosElegidos)
            print(obtenerTopEncabezado() + "############### ALTA DE PRESTAMO ################" + obtenerPieEncabezado())
            print("")
            print(prestamo.cliente)
            print(prestamo)
            print("")
            confirmar = input("¿Confirma la generación del préstamo? (Presione 'N' para Cancelar o cualquier tecla para confirmar):")
            if confirmar.upper() == "N": return
            else:
                prestamo.confirmar()  
                prestamos.append(prestamo)
                print()              
                print("Prestamo generado correctamente")
                esperarYVolver()
                
def devolverPrestamo(clientes):

    limpiarPantalla()
    #Variables
    cliente = None        
    #Inputo de datos   
    lstClientes = sorted(clientes, key = lambda c: c.apellido)
    menu = [lc.apellido + ", " +  lc.nombre for lc in lstClientes]
    encabezado = obtenerTopEncabezado() + "############# DEVOLUCIÓN DE PRESTAMO ############" + obtenerPieEncabezado()  
    opcionSalida = "Cancelar devolución"
    textoInput = "Seleccione el cliente deseado:"
    opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    while not opt.isdigit() or len(menu) < int(opt):
        textoInput = "La opción ingresada es incorrecta. Seleccione una opción de menú válida:"
        limpiarPantalla()
        opt = generarPantalla(encabezado, menu, opcionSalida, textoInput)
    if(opt == "0"): return
    cliente = lstClientes[int(opt)-1]                
    lstPrestamosADevolver = [p for p in cliente.prestamos if p.fechaDevolucionReal is None]
    print("\n")
    if not lstPrestamosADevolver: print("Este cliente no tiene préstamos sin devolver")
    else:
        limpiarPantalla()
        encabezado = obtenerTopEncabezado() + "############# DEVOLUCIÓN DE PRESTAMO ############" + obtenerPieEncabezado()  + f"\n\n{cliente}"
        textoInput = "Seleccione el préstamo a devolver:"
        opt = generarPantalla(encabezado, lstPrestamosADevolver, opcionSalida, textoInput)
        while not opt.isdigit() or len(menu) < int(opt):
            textoInput = "La opción ingresada es incorrecta. Seleccione una opción de menú válida:"
            limpiarPantalla()
            opt = generarPantalla(encabezado, lstPrestamosADevolver, opcionSalida, textoInput)
        if(opt == "0"): return
        limpiarPantalla()
        prestamo = lstPrestamosADevolver[int(opt)-1]                
        print(obtenerTopEncabezado() + "############# DEVOLUCIÓN DE PRESTAMO ############" + obtenerPieEncabezado())
        print()
        print(prestamo)        
        print()
        confirmar = input("¿Confirma la devolución del préstamo? (Presione 'N' para Cancelar o cualquier tecla para confirmar):")
        if confirmar.upper().strip() == "N": return
        else:
            prestamo.devolver(fechaSistema.hoy)                
            print()
            print("Prestamo devuelto correctamente")
    esperarYVolver()


def procesarYValidarInput(textoInput, validarComo, permitirValorVacio = False, ceroEsValorValido = False):
    
    dato = input(textoInput)
    if(not ceroEsValorValido and dato == "0"):
        return dato
    if(dato == ""):
        if not permitirValorVacio:
            print("El campo no puede estar vacío")
        return None
    try:
        datoPars = validarComo(dato)
    except Exception:
        print("El formato ingresado es inválido")
        return None
    else:     
        return datoPars

def limpiarPantalla():    
    import os
    os.system("cls")

def generarPantalla(encabezado, menu, opcionSalida, textoInput):    
    print(encabezado)    
    indice = 1
    for item in menu:
        print(f"{indice} - {item}")
        indice += 1    
    print(f"{0} - {opcionSalida}")
    return input(textoInput)

def esperarYVolver():
    print("\n")
    input("Presione ENTER para continuar.")



