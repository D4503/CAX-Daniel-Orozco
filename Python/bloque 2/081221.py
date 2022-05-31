p=0
while (p<5):
  input('hola, como estas? ')
  p=p+1
  if(p>4):
    print("ª")
    
while True:
  a=int(input('ingresa un numero: '))
  if(a==10):
    print('felicidades lo adivinaste')
    break
  if (a>10):
    print('te pasaste')
  if (a<10):
    print('te falta')