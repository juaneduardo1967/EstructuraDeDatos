class Quiniela:
    def __init__(self,a,segundoPremio,multiplicador=1):
        
        self.__primerPremio= a
        self.__segundoPremio= segundoPremio
        self.__multiplicador=multiplicador
        self.__premio1= int(self.__primerPremio)* int(multiplicador)
    def __repr__(self):
        return "numero 1 es  " +str(self.__primerPremio) +  "numero 2 es: " + str(self.__segundoPremio) + "primer premio es "+str(self.__premio1)
quiniela1=Quiniela(23,34,3)
print (quiniela1)