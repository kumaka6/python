
eval(input('Enter Value'))

# take three values from user
name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)


number = input("Enter roll number ")
name = input("Enter age ")

print("\n")
print('Roll number:', number, 'Name:', name)
print("Printing type of a input values")
print("type of number", type(number))
print("type of name", type(name))

# program to calculate addition of two input integer numbers

# convert inout into int
first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))

print("\n")
print("First Number:", first_number)
print("Second Number:", second_number)
sum1 = first_number + second_number
print("Addition of two number is: ", sum1)

# list to store multi line input
# press enter two times to exit
data = []
print("Tell me about yourself")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = ' '.join(data)
print("\n")
print("Final text input")
print(finalText)




