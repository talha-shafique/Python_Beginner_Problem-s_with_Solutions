# question: Write a program to check if a number is within a specified range.

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start <= number <= end:
    print("Within range")
else:
    print("Out of range")
