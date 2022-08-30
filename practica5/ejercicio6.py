'''Escribir un programa que crea y cargar
 dos matrices de tamaño 3x3, 
 las suma y muestra el resultado.'''
import numpy as np
m1=np.ones((3,3),int)
m2=np.ones((3,3),int)
def crearMatriz(matriz, nroFilas,nroColumnas):
    matriz=np.zeros((nroFilas,nroColumnas))
    for nFila in range(nroFilas):
        for ncolumna in range(nroColumnas):
            matriz[nFila,ncolumna]=input("inresar numero")
    return matriz
m1=crearMatriz(m1,3,3)
print(m1)
m2=crearMatriz(m2,3,3)
m3=np.zeros((3,3),int)

print(m2)
def sumaMatricez(m1,m2):
    nroFilas,nroColumnas=m1.shape
    for nFila in range(nroFilas):
        for nColumna in range(nroColumnas):
            m3[nFila,nColumna] =m1[nFila,nColumna] + m2 [nFila,nColumna]
    return m3
print(sumaMatricez(m1,m2))