"""ejercicio: agenda de contactos
crear un programa que use un diccionario para almacenar nombres y numeros de telefono
instrucciones:
1. crear un diccionario vacio
2. permite al usuario agregar contactos(nombre y numero)
3. permite buscar un contacto ingresando el nombre
4. permite mostrar todos los contactos guardados
5. usa un buclr para repetir el proceso hasta que el usuario decida salir"""
agenda = {}
nuevo_contacto = input("agrega un contacto: ")
nuevo_numero = input("agrega un numero: ")
agenda[nuevo_contacto]=nuevo_numero