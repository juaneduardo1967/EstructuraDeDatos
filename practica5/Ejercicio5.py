import numpy as np

def borrarEnPosicion(vector, posDel):      #vector = [4, 3, 5, 8, 6, 7] / posDel = 2
  for pos in range(posDel,len(vector)-1):  # 2 , 3 , 4
    vector[pos] = vector[pos+1]            # [4, 3, 8, 6, 7, 7]
  vector[len(vector)-1] = 0   

vector1=([2,4,6,8,2,5,7,9,3,])

print(vector1)
def borrarTodos(vector,dato):
    for pos in range (len(vector)):
        if vector1[pos]==dato:
            borrarEnPosicion(vector,pos)


borrarTodos(vector1,2)
print(vector1)
