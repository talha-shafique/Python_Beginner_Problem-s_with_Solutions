# Question: Create a program that checks if a given string is a palindrome.

a=input('Enter a word: ')
b=a[::-1]
print(b)
if a==b:
    print('It is a palindrome')
else:
    print('It is not a palindrome')