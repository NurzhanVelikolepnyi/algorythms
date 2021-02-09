import cmath, math

x = int(input('x: '))

result = cmath.sqrt(x**(1/5)) / math.e **abs(x+1)

print('result', result)