# Question: Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
a=int(input('Enter a temperature: '))
if a>=35:
    print('It is hot')
elif 0>=a>=34:
    print('It is moderate')
else:
    print('It is freezing')

