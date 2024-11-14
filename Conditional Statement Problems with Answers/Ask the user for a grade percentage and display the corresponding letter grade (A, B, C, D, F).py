# Question: Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

a=int(input('Enter grade percentage: '))
if 100>=a>=90:
    print('A Grade')
elif 90>a>=80:
    print('B Grade')
elif 80>a>=70:
    print('C Grade')
elif 70>a>=50:
    print('D Grade')
elif a<50:
    print('F Grade')
else:
    print("""Enter valid grade percentage (0-100)%""")