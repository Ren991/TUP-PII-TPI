import cod_generator


# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 0, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    #completar
    nuevoLibro = {'cod': cod_generator.generar() ,'cant_ej_ad': int(input("ingresa la cantidad de ejemplares adquiridos: ")),
     'cant_ej_pr': int(input("ingresa la cantidad de ejemplares prestados: ")), 
     'titulo': input("ingrese titulo del libro: "),
     'autor': input("ingrese autor del libro: ")}
    
    print(nuevoLibro)
    return nuevoLibro

def generar_codigo():
    #completar
    return None

