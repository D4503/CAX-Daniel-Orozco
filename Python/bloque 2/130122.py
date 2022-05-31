

while True:
  L=int(input("escribe el numero que tienen que adivinar "))
  if (L>99):
    print("reinicia el juego no se permiten numeros mayores de 3 digitos")
    break
  P=int(input("escribe un numero, si adivinas el de tu amig@ ganas "))
  if (L==P):
    print("lo lograste")
  if (L<P):
    fal=L-P
    print("te sobro", fal)
  if (L>P):
    sob=L-P
    print("te Falto", sob)