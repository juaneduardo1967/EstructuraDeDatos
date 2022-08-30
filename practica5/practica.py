
import numpy as np
#N = None

#vector = np.zeros(3, int)
'''for i in range(len(vector)):

    vector[i] = input("ingrese un numero")
    print(vector[i])
print(vector)'''
'''Escribir una función que recibe un arreglo de enteros por parámetro y 
lo retorna con el contenido desplazado una posición hacia la derecha: 
el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. 
El último pasa a ser el primero.
Luego, escribir un programa que cargue un arreglo con valores 
ingresados por el usuario y llame a la función con ese arreglo. 
Mostrar el contenido del arreglo por pantalla, antes y 
después de la función.
Por ejemplo:
Arreglo original = [2, 4, 1, 5, 7, 9]
Arreglo desplazado = [9, 2, 4, 1, 5, 7]'''
vector1= np.array([2,4,5,6,8])
def desplazarArreglo(unArreglo):
    vector=np.zeros(len(unArreglo),int)
    for elemento in range(len(unArreglo)):
        if elemento == len(unArreglo-1):
            vector[0]= unArreglo[elemento] 
        vector[elemento]=unArreglo[elemento-1]
    return vector
  
largoArreglo=int(input("ingrese tamaño del arreglo"))
vector2=np.zeros(largoArreglo,int)  
for elemento in range(len(vector2)):
    vector2[elemento]= input("ingrese numero")
    
print (desplazarArreglo(vector2))





