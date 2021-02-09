import cmath, math

a = int(input('a: '))
b = int(input('b: '))

result = (cmath.sqrt(b-a)) / (a**2) * abs(cmath.acos(15) / cmath.asin(15))

print('result', result)