print('bienvenido que va a querer? ')
print('esta es nuestra losta de articulos:')

print('1) snickers')
print('2) platano')
print('3) tomate')
print('4) lechuga')
print('5) cebolla')
print('6) naranjas')
print('7) paquete 20 cubrebocas KN95')
print('8) riñon')
print('9) gorra')
print('10) paraguas')
print('11) colchon')
print('12) nada')
precio1=10
precio2=75
precio3=69.90
precio4=26.90
precio5=26.90
precio6=25.90
precio7=180
precio8=182000
precio9=360
precio10=79.90
precio11=1365
precio12=0
while True:
  opcion=int(input('escribe el numero del articulo que quieres '))
  
  if opcion==1:
    print('snickers $10')
    total1=precio1
  if opcion==2:
    print('platano $75 Kg')
    total1=precio2
  if opcion==3:
    print('tomate $69.90 Kg')
    total1=precio3
  if opcion==4:
    print('lechuga $26,90 Kg')
    total1=precio4
  if opcion==5:
    print('cebolla $36.90 Kg')
    total1=precio5
  if opcion==6:
    print('naranjas $25.90 Kg')
    total1=precio6
  if opcion==7:
    print('paquete 20 cubrebocas KN95 $180')
    total1=precio7
  if opcion==8:
    print('riñon $182000')
    total1=precio8
  if opcion==9:
    print('gorra $360')
    total1=precio9
  if opcion==10:
    print('paraguas $79.90')
    total1=precio10
  if opcion==11:
    print('colchon $1365.92')
    total1=precio11
  if opcion==12:
    total1=precio12
  opcion1=int(input('escribe el numero del articulo que quieres '))
  if opcion1==1:
    print('snickers $10')
    total2=precio1
  if opcion1==2:
    print('platano $75 Kg')
    total2=precio2
  if opcion1==3:
    print('tomate $69.90 Kg')
    total2=precio3
  if opcion1==4:
    print('lechuga $26,90 Kg')
    total2=precio4
  if opcion1==5:
    print('cebolla $36.90 Kg')
    total2=precio5
  if opcion1==6:
    print('naranjas $25.90 Kg')
    total2=precio6
  if opcion1==7:
    print('paquete 20 cubrebocas KN95 $180')
    total2=precio7
  if opcion1==8:
    print('riñon $182000')
    total2=precio8
  if opcion1==9:
    print('gorra $360')
    total2=precio9
  if opcion1==10:
    print('paraguas $79.90')
    total2=precio10
  if opcion1==11:
    print('colchon $1365.92')
    total2=precio11
  if opcion1==12:
    total2=precio12
  print("$",total1+total2)
  print('este es el total a pagar')