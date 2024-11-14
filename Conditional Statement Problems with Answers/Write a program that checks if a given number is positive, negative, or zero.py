# Question: Write a program that checks if a given number is positive, negative, or zero.

a=int(input('Enter a number: '))
if a>0:
    print(f'{a} is positive')
elif a<0:
    print(f'{a} is negative')
else:
    print(f'{a} is zero')
