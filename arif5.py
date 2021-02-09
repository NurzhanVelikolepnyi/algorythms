import math, cmath
b=int(input('b: '))
a=int(input('a: '))

result = (cmath.asin(60) - b) / (abs(b) + cmath.acos(30)) + a
print('result', result)