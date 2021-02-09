import math, cmath
x=int(input('x: '))
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

x1 = (-1*b + cmath.sqrt(b*b-4*a*c)) / (2*a)

print('x',x1)