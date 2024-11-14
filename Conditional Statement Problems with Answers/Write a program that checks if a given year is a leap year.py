# Question: Write a program that checks if a given year is a leap year.

a=int(input('Enter a year: '))

if a%4==0:
    if a%100==0: 
        if a%400==0:
            print('It is a leap year')
        else:
            print('It is not a leap year')
    else:
        print('It is a leap year')
else:
        print('It is not a leap year')

