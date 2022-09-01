class Cuenta:
  def __init__(self,numero, dni, saldo, interes):
    self.__numeroCuenta= numero #validarNumero(numero,int)
    self.__dni=dni
    self.__saldo= saldo
    self.__interes=int(interes)
  def __repr__(self):
    return  self.__numeroCuenta 
  def actualizarSaldo(self,interes):
    self.__saldo
    saldor= int(self.__saldo) * interes
    print (saldor)
  
cuenta1 = Cuenta("23","123","300","23") 
print(cuenta1)
cuenta1.actualizarSaldo(34)
print(cuenta1)
