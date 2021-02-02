st=int(input('st: '))
if st<5:
    zp=130
if st<=5:
    zp=180
else:
    zp=180+(st-15)*10
print('zp:', zp)
 