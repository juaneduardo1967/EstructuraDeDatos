'''Escribir una función que retorna True si una matriz
 cuadrada de enteros es simétrica y False en caso contrario.

Una matriz simétrica es como la de la imagen 
(no importan los elementos de la diagonal principal):'''
import numpy as np
matriz=np.zeros((3,3),int)
matriz[1,0]=3
matriz[0,1]=3
nroFilas,nroColumnas=matriz.shape
r=True 
for nFila in range(nroFilas):
    for nColumna in range(nroColumnas):
        if matriz[nFila,nColumna]!= matriz[nColumna,nFila]:
            r= False        
print(matriz)
print(r)
