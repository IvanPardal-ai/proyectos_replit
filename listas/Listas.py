frutas=["naranja", "pera", "mango"]
print("lista de frutas:",frutas)
print("Primera fruta:",frutas[0])
print("Tercera fruta:",frutas[2])
#Modificar un valor de una lista.
frutas[2]="manzana"
print("Fruta modificada:", frutas[2])
#Añadir un valor a una lista.
frutas.append("mandarina")
print("Nueva fruta:", frutas[3])
#Eliminar valor de una lista.
frutas.remove("pera")
print(frutas)
#Eliminar el ultimo valor de una lista.
ultimo=frutas.pop()
print("Se eliminó este valor:'", ultimo, "', la lista actualizada quedó asi:", frutas)
