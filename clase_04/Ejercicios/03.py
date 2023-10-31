# # Diccionarios

# mi_diccionario = {
#     "clave1": "Valor 1",
#     "clave2": 10,
#     "clave3": [1,2,3,4,5],
#     "clave4": ("A", "B", "C"),
#     "clave5": {
#         1: "Perro",
#         35: "Gato",
#         320: "Hamster"
#     }
# }

# print(mi_diccionario)

agenda = {
    "5512121212": {
        "nombre": "Raul",
        "apellido": "Vazquez"
    },
    "5698230983":{
        "nombre": "Luis",
        "apellido": "Hernandez",
        "fechaNacimiento": "01/01/1990"
    }
}

print(agenda["5512121212"]["nombre"])
print(agenda["5698230983"]["nombre"])