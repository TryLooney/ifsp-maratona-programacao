from sys import stdin
data = [float(i) for i in stdin.read().split()]
a = data[0]
b = data[1]
c = data[2]
if (a >= (b+c)):
    print("NAO FORMA TRIANGULO")
if (a**2 == (b**2 + c**2)):
    print ("TRIANGULO RETANGULO")
if (a**2 > (b**2 + c**2)):
    print ("TRIANGULO OBTUSANGULO")
if (a**2 < (b**2 + c**2)):
    print ("TRIANGULO ACUTANGULO")
if (a == b and a == c and b == c):
    print ("TRIANGULO EQUILATERO")
if (a == b or a == c or c == b):
    print ("TRIANGULO ISOSCELES")