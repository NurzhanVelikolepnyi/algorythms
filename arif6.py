import cmath, math
x = int(input('x: '))

result=(math.e**(2*x) - cmath.sqrt(1+abs(math.sin(abs(x))))) / (2)

print('result', result)