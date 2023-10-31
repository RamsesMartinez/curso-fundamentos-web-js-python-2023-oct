# # # Estructuras de control

# # mensaje = input("Escribe tu nombre: ")

# # if mensaje == "Ramses":
# #     print("Hola, bienvenido!!!")
# # elif mensaje == "Luis":
# #     print("Hola, amigo!")
# # else:
# #     print("Disculpa, no te conozco")

# # edad = int(input("Ingresa tu edad: "))

# #  if edad >= 18:  # edad <= 30  1,2,3...(18-30)...
# # if edad >= 18 and edad <= 30: # and or 
# #     print("Autenticando...")
# # else:
# #     print("Debes ser mayor de edad")

# refresco = input("Ingresa el sabor del refresco: ")
# # if refresco == "naranja" or refresco == "fresa" or refresco == "toronja":
# if refresco in ("naranja", "fresa", "toronja"):
#     print("Compramos refresco")
# else:
#     print("No compramos refrescos")

# num1 = 10
# num2 = 20

# print(not(num1 < num2))

alumnos = ["Camila", "Ana", "Pedro", "Luis", "Ramsés"]
if "Hector" not in alumnos:
    print("No se encuentra hector")