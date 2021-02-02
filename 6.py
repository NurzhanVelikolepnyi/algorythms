a =int(input('a: '))
b =int(input('b: '))
c =int(input('c: '))

d=b**2-4*a*c
if (d>=0):
    x1=(-1*b-d**0.5)/(2*a)
    x2=(-1*b+d**0.5)/(2*a)
    print('x1','x2',x1,x2)
else:
    print('Решения нет')
    

