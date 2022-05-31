x=5
if (x<10):
  print("smaller")
if (x>20):
  print("bigger")
if (x==5):
  print("its five")
print("finis")
p=10
if(p<10):
  print("bigger")
else:
  print("bigger")

print("you need to guess the number")
while True:
  L=int(input(""))
  if (L==12):
    print("you got it")
  if (L<12):
    print("put more")
  if (L>12):
    print("put less")