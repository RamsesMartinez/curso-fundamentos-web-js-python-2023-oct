# Conjuntos

# conjunto_1 = {6, 1,2,3,4,5, 2, 4, 6, 6, 1}
# conjunto_2 = set(["uva", "piña", "sandia", "uva"])
# print(conjunto_2)

conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5}

interseccion = conjunto_1.intersection(conjunto_2)
print("interseccion:", interseccion)

union = conjunto_1.union(conjunto_2)
print("union: ", union)

difference_1 = conjunto_1.difference(conjunto_2)
difference_2 = conjunto_2.difference(conjunto_1)

print(difference_1)
print(difference_2)