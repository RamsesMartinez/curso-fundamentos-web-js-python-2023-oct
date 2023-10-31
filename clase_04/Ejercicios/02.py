# LISTAS

# numeros = [1,2,3,4,5,20,50,100]

# print(numeros[100]) IndexError
# print(numeros[-2])
# print(numeros[-20]) IndexError


animales = ["Jirafa", "Perro", "Foca", "Delfín", "Jirafa", "Foca", "Pajaro", "Pajaro"]

# animal = animales[0]

# print(animal)

# animales[0] = "Elefante"

# print(animales)
# animales.append("Gato")
animales_2 = ["Pajaro", "Tigre"]
animales.extend(animales_2)

print(animales)

animales.insert(2,"León")

animales.remove("Pajaro")

print(animales)

animales.remove("Pajaro")

print(animales)


animales.remove("Pajaro")

print(animales)

if "Pajaro" in animales:
    animales.remove("Pajaro")


