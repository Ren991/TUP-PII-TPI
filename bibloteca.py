

import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print(libros)
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    
    return None

def prestar_ejemplar_libro():
    #completar
    
    libroAPrestar = input("Ingrese código del libro a prestar: ")
    
    encontro = False
    for libro in libros:
        if libroAPrestar == libro.get("cod"):
            cantidadDisponible = libro.get("cant_ej_ad") - libro.get("cant_ej_pr") # Resta la cantidad de ejemplares con la cantidad de prestados y da como total la cantidad disponible.
            
            print("Título:", libro.get("titulo"))
            print("Autor:", libro.get("autor"))
            print("Cantidad Disponible:", cantidadDisponible)

            if cantidadDisponible <= 0:
                print("El libro " + libro.get("titulo") + "no tiene ejemplares disponbles")
            else:
                libro["cant_ej_pr"] += 1
                print("Se confirmó el prestamo del libro")



            encontro = True
       

    if encontro == False: 
        print("No se encontró el libro")
    print(libros)
    return None

def devolver_ejemplar_libro():

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