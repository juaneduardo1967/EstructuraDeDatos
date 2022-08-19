""" #Implementar el TDA "Propiedad" que modela un inmueble, con una estructura
#definida por los siguientes componentes:
• Calle
• Número
• Localidad
• Año de construcción
• Cantidad de ambientes
Implementar las siguientes operaciones:
• Constructor: Debe incluir las validaciones necesarias, 
teniendo en cuenta que solo
se almacenan propiedades construidas luego de 1870.
• _str_: Al usar la función print con una variable del tipo propiedad debe mostrar:
'calle' 'numero' ('localidad').
• mismaLocalidad: Operación que recibe dos propiedades y retorna True si estan en
la misma localidad y False en caso contrario.
• mayorNumeración: Operación que recibe dos propiedades y si entan en la misma
calle, retorna la que posee mayor numeración. Si estan calles diferentes debe
lanzar una excepción.
• calculaImpuestoARBA: Operación que retorna el porcentaje de impuesto
inmobiliario de una propiedad, según la siguiente regla:
◦ Propiedades entre 1870 y 1949:
▪ Entre 1 y 3 ambientes: 5% de impuesto
▪ Entre 4 y 6 ambientes: 10% de impuesto
▪ Más de 6 ambientes: 25 % de impuesto
◦ Propiedades desde 1950 hasta la actualidad:
▪ Entre 1 y 5 ambientes: 5% de impuesto
#▪ Más de 5 ambientes: 35 % de impuesto*/ """
import copy as cp

def validarTipo(variable, nombre, tipo):
    if isinstance(variable, tipo):
        return variable
    else:
        raise Exception("La variable " + nombre + " debe ser de tipo " + str(tipo) + ".")
def validarAño(año):
    if (año > 1870):
        return año
    else:
        return "valor invalido"
class Propiedad:
  def __init__(self, calle="", numero=0 , localidad="", año=0, ambientes=0):
    self.__calle=validarTipo(calle,"calle",str)
    self.__numero = numero
    self.__localidad = validarTipo(localidad, "localidad", str)
    self.__año = validarAño(año)
    self.__ambientes = ambientes
  def getCalle(self):
    return self.__calle
  def modificarCalle(self,calle):
      self.__calle = calle
  def __repr__(self):
    return self.__calle
     

prop1= Propiedad("repeto",1448,"ituzaingo",1200,4)
print (prop1)