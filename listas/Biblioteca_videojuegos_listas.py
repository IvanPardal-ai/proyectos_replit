videojuegos=["Fortnite", "Minecraft", "Rocket League"]
print("Bienvenido a tu biblioteca")
juegofavorito=input("Introduzca su videojuego favorito: ")
videojuegos.append(juegofavorito)
for i in videojuegos:
  print("-", i)
print("No hay espacio suficiente para descargar", juegofavorito)
juegoeliminar=input("Que juego deseas eliminar?: ")
if(juegoeliminar in videojuegos):
  videojuegos.remove(juegoeliminar)
  print("Descargando", juegofavorito, "...")
  print("Entrando a", juegofavorito, "...")
else:
  print(juegoeliminar, "no esta en tu biblioteca")
contraseñas_incorrectas=[]
nombre=input("Introduzca su nombre de usuario: ")
contraseña=input("Introduzca su contaseña: ")
comprobacion=input("Confirme la contraseña: ")
while contraseña!=comprobacion:
  print("Error")
  contraseñas_incorrectas.append(comprobacion)
  comprobacion=input("Repita la contraseña: ")
  if comprobacion==contraseña:
    print("Contraseña establecida")
    print("Aqui tienes tus contraseñas incorrectas: ")
    for i in contraseñas_incorrectas :
      print("-", i)