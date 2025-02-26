"""ejercicio: agenda de contactos
crear un programa que use un diccionario para almacenar nombres y numeros de telefono
instrucciones:
1. crear un diccionario vacio
2. permite al usuario agregar contactos(nombre y numero)
3. permite buscar un contacto ingresando el nombre
4. permite mostrar todos los contactos guardados
5. usa un bucle para repetir el proceso hasta que el usuario decida salir"""
agenda = {}
def agenda_contactos():
    
    while True:
        mostrarMenu()
        respuesta_menu=input("Selecciona una opción: ")
        if(respuesta_menu=="1"):
            opcionUno()
        elif(respuesta_menu=="2"):
            opcionDos()
        elif(respuesta_menu=="3"):
            print(agenda)
        elif(respuesta_menu=="4"):
            return False
        else:
            print("Esta opcion no es valida.")

def mostrarMenu():
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

def opcionUno():
    contacto = input("agrega un contacto: ")
    numero = input("agrega un numero: ")
    agenda[contacto]=numero
    print("El contacto se ha agregado correctamente")
    print(agenda)

def opcionDos():
    buscar_contacto=input("¿Que contacto quieres buscar?: ")
    if(buscar_contacto in agenda):
        print(f"El numero de {contacto} es: {agenda[contacto]}" )
    else:
        print("Este contacto no esta en la agenda, vuelve a intentarlo.")
agenda_contactos()