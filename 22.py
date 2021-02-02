a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
x=int(input('x: '))
y=int(input('y: '))

if a>b:
    r=a
    a=b
    b=r

if b>c:
    r=b
    b=c
    c=r

if a>b:
    r=a
    a=b
    b=r

if x>y:
    r=x
    x=y
    y=r

if a<x and b<y:
    print('Пройдёт')
else:
    print('Не Пройдёт')

