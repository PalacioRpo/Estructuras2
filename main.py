from ordenamiento import *
from generadorDatos import *
import random
#Realizado por: Maria Paulina López Salazar - Camilo Palacio Restrepo
if __name__ == "__main__":
  print("Inicio")
  poblacion = []
  poblacion = generarGrupos(20, poblacion)
  puntos = []
  punto_llegada = []
  puntoss = generarPuntos(20, poblacion, puntos)
  numpunto = 1
  for punto in puntoss:
    censo = 0
    print('-' * 20)
    print("Punto de encuentro:", numpunto)
    punto = familia_n(punto)
    numfamilias = 1
    for familia in punto:
      for familiar in familia:
        censo+=1
      print("Familia :", numfamilias)
      print(familia)
      numfamilias += 1
    punto_llegada = carros(punto, punto_llegada)
    numpunto += 1
    print('-'*5, "Censo:", censo, '-'*5)
  numcarros = 1
  print('-'*5, "Punto de llegada", '-'*5)
  for carro in punto_llegada:
    if len(carro) != 0:
      print("Carro #", numcarros)
      print(carro)
    numcarros += 1
  print("Fin!")