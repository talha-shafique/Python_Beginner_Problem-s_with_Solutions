# Question: Write a program to find the largest of three numbers.

a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if a>b and a>c:
    print(f'{a} is the largest')
elif b>a and b>c:
    print(f'{b} is the largest')
else:
    print(f'{c} is the largest')
    

