'''
Escribir una función recursiva, que calcule la suma de los 
elementos de la diagonal principal de una matriz.
Nota: La suma de los elementos de la diagonal
 principal de una matriz se llama "traza de la matriz".'''

import numpy as np
matriz=np.ones((3,3),int)
nroFilas,nroColumnas=matriz.shape
suma=0
def sumaDiagonalMatriz():
   suma=matriz[nroFilas-1,nroColumnas-1] + sumaDiagonalMatriz[nroFilas-2,nroColumnas-2]
