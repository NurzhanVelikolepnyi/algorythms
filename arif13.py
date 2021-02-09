import cmath, math

a = int(input('a: '))
x = int(input('x: '))

result = cmath.sqrt(a) - abs(math.e**math.log10(x))

print('result', result)