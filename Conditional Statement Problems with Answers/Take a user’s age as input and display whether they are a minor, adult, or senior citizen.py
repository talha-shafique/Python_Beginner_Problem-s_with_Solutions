# Question: Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

a=int(input('Enter your age: '))
if a<=18:
    print('You are a minor')
elif a in range(19,50):
    print('You are an adult')
else:
    print('You are a senior citizen')
    