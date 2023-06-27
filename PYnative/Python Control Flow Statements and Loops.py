"""
Control Flow Statements
The flow control statements are divided into three categories

Conditional statements
Iterative statements.
Transfer statements

"""

number = 6
if number > 5:
    # Calculate square
    print(number * number)
print('Next lines of code')


"""
num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)

"""

number = 56
if number > 0: print("positive"); print("second statement"); print("third statement ")
else: print("negative")

x = 1
while x <= 5: print(x,end=" "); x = x+1; print("its while loop")

for i in range(1, 11): print(i, end = " ") ; print("for loop "); print(" test ", i, " checking ")

num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i ; i += 1
    #i = i + 1
print("Sum of first 10 number is:", sum)

