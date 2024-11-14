# Question: Write a program to find the largest of two numbers.
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
if a>b:
    print(f'{a} is greater than {b}')
elif b>a:
    print(f'{b} is greater than {a}')
else:
    print('Both are equal')

