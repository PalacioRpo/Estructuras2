def MergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return sorted(datos)
    mitad = len(datos) // 2
    return op_Merge(MergeSort(datos[:mitad]), MergeSort(datos[mitad:]))

def op_Merge(datosX, datosY):
  indA = indB = 0
  out = []
  while indA < len(datosX) and indB < len(datosY):
    if datosX[indA] < datosY[indB]:
      out.append(datosX[indA])
      indA += 1
    else:
      out.append(datosY[indB])
      indB += 1
  out += datosX[indA:] + datosY[indB:]
  return out    
