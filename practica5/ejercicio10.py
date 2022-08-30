'''Escribir una función que retorna True 
si una matriz cuadrada de enteros 
es matriz diagonal y False en caso contrario.

Una matriz diagonal es una matriz que 
tiene ceros en todos sus elementos, menos
 en la diagonal principal.'''
import numpy as np
matriz=np.zeros((3,3),int)

matriz[2,1]=3
nroFilas,nroColumnas=matriz.shape

r=True 
for nFila in range(nroFilas):
    for nColumna in range(nroColumnas):
        if nColumna!=nFila and matriz[nFila,nColumna]!=0:
            r= False
        
print(matriz)
print(r)

