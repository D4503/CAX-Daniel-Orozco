#condiciones anidadas 
while True:

  mensaje=input("escribe hola ")

  if (mensaje!="hola"):

    if (mensaje=="HOLA"):
      print("no sabes leer?, era hola")
      continue

    elif (mensaje=="Hola"):
      print("se agradece una persona muy letrada, pero aprenda a leer, dije hola")
      continue

    elif (mensaje=="hOLA"):
      print("intenta desactivar block mayus")
      continue

    else:
      print("en serio.....")
      continue

  elif(mensaje=="hola"):
    print("hola, que agradable sujeto")
    break