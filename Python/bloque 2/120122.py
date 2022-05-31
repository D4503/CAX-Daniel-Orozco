#codigo que solicite 3 calificaciones y calcular el promedio y tiene que decir si tiene premio, si aprueba o reprueba (aprobar es de 9 para arriba, reprobar es de abajo de 6 y aprobar es con mas de 6)

while True:
  cal1=int(input("escribe la primer calificacion"))
  cal2=int(input("escribe la segunda calificacion"))
  cal3=int(input("escribe tu tercer calificacion"))
  cal=cal1+cal2+cal3
  prom=cal/3
  print(prom, "este es tu promedio")
  if (prom<6):
    print("ni modo reprobaste")
  if (prom>9):
    print("toma una medalla")
  if (prom>6<9):
    print("bueno... aprobaste")