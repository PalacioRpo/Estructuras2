import random
from ordenamiento import *

#genera un grupo de varias familias
def generarFamilias(num_familias, grupo, cont):
    if num_familias == 1:  
      return grupo
    else:
        num_familiares = random.randint(2, 12)
        familia = []
        i = 0
        familiar = 0
        while i < num_familiares:
          if i < 2:
            familiar = random.randint(24, 59)
            familia.append(familiar)
            cont+=1
          else:
            familiar = random.randint(1, 100)
            familia.append(familiar)
            cont+=1
          i+=1
        familia = MergeSort(familia)
        familia.reverse()
        familia = adultoResponsable(familia)
        grupo.append(familia)
        return generarFamilias(num_familias-1, grupo, cont)

#devuelve un booleano si tiene un niño en la familia

#genera varios grupos con sus respectivas familias
def generarGrupos(num_grupos, poblacion):
  if num_grupos == 0:  
      return poblacion
  else:
    grupo = []
    num_familias = random.randint(5, 10)
    poblacion.append(generarFamilias(num_familias, grupo, 0))
    return generarGrupos(num_grupos-1, poblacion)

#genera varios puntos de encuentro, a los cuales se les enviaran los grupos
def generarPuntos(cantidad_grupos, poblacion, puntos):
  if cantidad_grupos == 0:
    return puntos
  else:
    puntos.append(poblacion[cantidad_grupos-1])
  return generarPuntos(cantidad_grupos-1, poblacion, puntos)

#Garantiza, que en la primera posición del arreglo haya un adulto responsable, acompañante de adultos mayores
def adultoResponsable(datos):
  temporal = [0]
  i = 0
  while i < len(datos):
    if datos[i] < 60:
      temporal[0] = datos.pop(i)
      j = 0
      while j < len(datos):
        temporal.append(datos[j])
        j+=1
      break
    i+=1
  return temporal
    
#Familias indivisibles, con niños
def validar_ninos(datos):
  n = 20
  for dato in datos:
    if dato <= 17:
      n = dato
      break
  if n < 18:
    return True
  else:
    return False
    
def familia_n(datos):
  temporal = []
  i = 0
  while i < len(datos):
    if validar_ninos(datos[i]):
      temporal.append(datos[i])
      datos.pop(i)
      i -= 1
    i += 1
  j = 0
  while j < len(datos):
    temporal.append(datos[j])
    j += 1
  return temporal

#genera los carros, donde se ubicarán los grupo de a 12 personas
def carros(grupo, punto_llegada):
  if len(grupo) == 0:
    return punto_llegada
  else:
    carro = []
    nuevocarro = False
    for dato in grupo: 
      i = 0
      lendato = len(dato)
      while i < lendato:
        if len(carro) == 12:
          nuevocarro = True
          break
        carro.append(dato[0])
        dato.pop(0)
        i+=1      
      if nuevocarro:
        break
    
    punto_llegada.append(carro)
    return carros(grupo[1:],punto_llegada)

def eliminarVacios(datos):
  i = 0
  lendatos = len(datos)
  while i < lendatos:
    if len(datos[i]) == 0:
      datos.pop(i)
    i+=1