# Bucles

# for num in range(10):
#     if num == 5:
#         break # Terminará el bucle cuando num sea igual a 5
#     elif num % 2 == 0:
#         continue # Se saltará a la siguiente iteración si num es par
#     else:
#         pass # No hará nada si num es impar
#     print(num)

# final = int(input("Dame el numero final: "))
for num in range(10):
    if num % 2 == 0:
        continue
    print("HOLA!")
    print("mensaje 2")
    print("El numero es: ", num)
    print("ADIOS!")