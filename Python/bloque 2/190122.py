#elif necesita de un if para funcionar, el else es todo lol contraio de if 
numero=8
compara=int(input("numero? "))

if (compara<numero):
  print("te falta")

#elif necesita un if para funcionar 
elif (compara>numero):
  print("te sobra")

#es todo lo contrario a if, no del elif
else:
  print("felicidades")