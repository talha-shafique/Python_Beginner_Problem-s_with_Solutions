# question: Find the factorial of a number using a while loop.
a=int(input('Enter a number: '))
b=1
for i in range(b,a+1):
    b=b*i
print(f'Factorial of {a} is {b}')