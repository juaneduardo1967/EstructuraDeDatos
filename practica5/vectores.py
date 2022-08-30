import numpy as np
vector = np.zeros(8, int)
print(vector)
vector[0] = 1
vector[1] = 2
vector[2] = 6
print(vector[0:2])
print(len(vector))
print(vector)
for elemento in vector:
    print(elemento)

for elemento in reversed(vector):
    print(elemento)
print ("##Posicion##")
for posicion in range(len(vector)):
    print("Posicion", posicion)
    print (vector[posicion])


