# question: Print the multiplication table of a given number.
a=int(input('Enter a number: '))
for i in range(1,11):
    print(f'{a} x {i} = {a*i}')