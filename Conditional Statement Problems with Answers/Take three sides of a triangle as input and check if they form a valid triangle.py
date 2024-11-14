# Question: Take three sides of a triangle as input and check if they form a valid triangle.

a=int(input('Enter L1 of the triangle (cm): '))
b=int(input('Enter L2 of the triangle (cm): '))
c=int(input('Enter L3 of the triangle (cm): '))
if a+b>c and a+c>b and b+c>a:
    print("Triangle is valid")
else:
    print("Triangle is not valid")