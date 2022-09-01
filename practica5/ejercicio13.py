''' Escribir 3 procedimientos que reciben una 
cadena de caracteres y..:

Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprima la cadena cada dos caracteres. 
Por ej.: 'recta' debería imprimir 'rca'
[ ]
arrCar = np.zeros(5,str)
arrCar[0] = "r"
print(arrCar)
  '''
string="America"
for letra in string[2:7:2]:
    print(letra)