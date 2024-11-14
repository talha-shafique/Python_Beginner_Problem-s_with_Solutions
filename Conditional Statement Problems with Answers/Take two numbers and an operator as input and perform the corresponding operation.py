a=int(input('Enter 1st digit: '))
b=int(input('Enter 2nd digit: '))
c=input('Choose the operation you want to perform (+,-,*,/) from (1-4) respectively: ')
if c==1:
    print(f'{a} + {b} = {a+b}')
elif c==2:
    print(f'{a} - {b} = {a-b}')
elif c==3:
    print(f'{a} * {b} = {a*b}')
else:
    print(f'{a} / {b} = {a/b}')

