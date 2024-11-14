# Question: Check if a given number is a multiple of both 3 and 5.
a=int(input('Enter a number: '))
if a%3==0 and a%5!=0:
    print('It is a multiple of 3')
elif a%3!=0 and a%5==0:
    print('It is a multiple of 5')
else:
    print('It is a multiple of both 3 & 5')

