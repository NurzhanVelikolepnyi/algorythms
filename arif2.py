import math

x = int(input('x: '))

result = (math.cos(x) / math.sin(x)) + math.sin(x**3)**2

print('result:', result)