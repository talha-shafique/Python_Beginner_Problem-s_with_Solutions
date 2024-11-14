# question: Check if a year input by the user is a century year.
a=input('Enter a year: ')
if a[-1]=='0' and a[-2]=='0':
    print('It is a century year')
else:
    print('It is not a century year')
