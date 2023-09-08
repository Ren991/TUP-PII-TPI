

import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    #Se recorre el array libros y se busca que la propiedad cant_ej_pr de los objetos tenga un valor mayor a 0
    
    for libro in libros:
        if libro.get("cant_ej_pr") > 0:
            print("Nombre : " + libro.get("titulo") + " || Cantidad prestados : " + str(libro.get("cant_ej_pr")))
    return None

def registrar_nuevo_libro():

    # A la variable nuevo_libro se le asigna el return de la función nuevo.libro() del archivo libro.py
    # Luego se añade al array

    nuevo_libro = l.nuevo_libro()

    libros.append(nuevo_libro)
    print(libros)
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    #Se le pide el código del libro al usuario
    #Se recorre el array , si encuentra ese codigo valida la propiedad cant_ej_ad.
    #Si no encuentra el código devuelve mensaje.

    libroAEliminar = input("Ingrese código del libro del cual quiere eliminar un ejemplar: ")
    
    encontro = False
    for libro in libros:
        if libroAEliminar == libro.get("cod"):
            
            
          

            if libro["cant_ej_ad"] <= 0:
                print("El libro " + libro.get("titulo") + " no tiene ejemplares")
            else:
                libro["cant_ej_ad"] -= 1
                print("Se confirmó la eliminacion del ejemplar")



            encontro = True
       

    if encontro == False: 
        print("No se encontró el libro")
    print(libros)

    return None

def prestar_ejemplar_libro():
    #completar
    
    #Se le pide el código del libro al usuario
    #Se recorre el array , si encuentra ese codigo valida que haya libros disponibles para prestar.
    #Si hay libros disponibles se le suma una unidada la propiedad -> cant_ej_pr
    #Si no encuentra el código ingresado devuelve mensaje.


    libroAPrestar = input("Ingrese código del libro a prestar: ")
    
    encontro = False
    for libro in libros:
        if libroAPrestar == libro.get("cod"):
            cantidadDisponible = libro.get("cant_ej_ad") - libro.get("cant_ej_pr") # Resta la cantidad de ejemplares con la cantidad de prestados y da como total la cantidad disponible.
            
            print("Título:", libro.get("titulo"))
            print("Autor:", libro.get("autor"))
            print("Cantidad Disponible:", cantidadDisponible)

            if cantidadDisponible <= 0:
                print("El libro = " + libro.get("titulo") + " || no tiene ejemplares disponbles")
            else:
                libro["cant_ej_pr"] += 1
                print("Se confirmó el prestamo del libro")



            encontro = True
       

    if encontro == False: 
        print("No se encontró el libro")
    print(libros)
    return None

def devolver_ejemplar_libro():

    #Se le pide el código del libro al usuario
    #Se recorre el array , si encuentra ese codigo valida que la cantidad de prestados sea mayor a 0.
    #Si hay libros para devolver se le resta una unidada la propiedad -> cant_ej_pr
    #Si no encuentra el código ingresado devuelve mensaje.

    libroADevolver = input("Ingrese código del libro a devolver: ")
    
    encontro = False
    for libro in libros:
        if libroADevolver == libro.get("cod"):           
            
            
            encontro = True
            if libro.get("cant_ej_pr") > 0:
                libro["cant_ej_pr"] -= 1
                print("Se confirmó la devolución del libro "+ libro.get("titulo"))
                
            else:
                print("El libro = ||"  +libro.get("titulo") +"||  no tiene ejemplares prestados")            



    if encontro == False: 
        print("No se encontró el libro")
    
    print(libros)
    
    return None

def nuevo_libro():
    #completar
    return None