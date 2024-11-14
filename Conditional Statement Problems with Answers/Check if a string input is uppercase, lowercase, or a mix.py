# question: Check if a string input is uppercase, lowercase, or a mix.

text = input("Enter a string: ")

if text.isupper():
    print("Uppercase")
elif text.islower():
    print("Lowercase")
else:
    print("Mixed case")
