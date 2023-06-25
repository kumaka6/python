"""
A variable is a reserved memory area (memory address) to store value.
A variable can be either mutable or immutable.
If the variable’s value can change, the object is called mutable,
    while if the value cannot change, the object is called immutable


"""
import sys

a = 100
print(type(a))  # class 'int'

b = 100.568
print(type(b))  # class 'float'

str1 = "PYnative"
print(type(str1))  # class 'str'

my_list = [10, 20, 20.5, 100]
print(type(my_list))  # class 'list'

my_set = {'Emma', 'Jessa', 'Kelly'}
print(type(my_set))  # class 'set'

my_tuple = (5, 10, 15, 20, 25)
print(type(my_tuple))  # class 'tuple'

my_dict = {1: 'William', 2: 'John'}
print(type(my_dict))  # class 'dict'

# using __name__ method of type function to display only the name of data  type
print("If we want to get the name of the datatype only as output,")
my_list =[10,20,20.5,'Python',100]
# It will print only datatype of variable
print(type(my_list).__name__) # list

print(type(my_list).__qualname__)

"""
Constant is a variable or value that does not change, which means it remains the same and cannot be modified.
But in the case of Python, the constant concept is not applicable.
By convention, we can use only uppercase characters to define the constant variable if we don’t want to change it.

"""

#importing constant from constant.py file and using it
import constant
print(constant.MANI , constant.KUMAKA)

# python is case sensitive
Mani = 120
mAni = 130
print(mAni, Mani)

# multiple assignments
#   single value to multiple variable
a = b = c = 10
print(a) # 10
print(b) # 10
print(c) # 10

# multiple value to multiple variable
roll_no, marks, name = 10, 70, "Jessa"
print(roll_no, marks, name) # 10 20 Jessa
mark2 = 10; mark4 = 20
print(mark2, mark4, type(mark2).__name__)

"""
Scope: The scope of a variable refers to the places where we can access a variable.
Depending on the scope, the variable can categorize into two types local variable and the global variable.
"""

def test1():  # defining 1st function
    price = 900  # local variable
    print("Value of price in test1 function :", price)

def test2():  # defining 2nd function
    # NameError: name 'price' is not defined
    print("Value price in test2 function:", price)

# call functions
test1()
#test2()

price = 900  # Global variable

def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900

def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900

# call functions
test1()
test2()

n = 300
m = n
print(id(n)) # same memory address
print(id(m)) # same memory address

m = 500
n = 400
print("Memory address of m:", id(m))  # 1686681059984
print("Memory address of n:", id(n))  # 1686681059824

kumaka = "mani"
print(id(kumaka))

print(a, b)
print(id(a), " -- ", id(b))
del a
print(b)
# print(a)  object a only deleted, not value in b
a = 10
print(id(a))

print(sys.getrefcount(a), " --- ", sys.getrefcount(b))

k = "ku"
m = "ku"

print(id(k), " -- ", id(m), " --- ", sys.getrefcount(k), sys.getrefcount(m))

"""
    Packing
In Python, we can create a tuple (or list) by packing a group of variables.
Packing can be used when we want to collect multiple values in a single variable.
Generally, this operation is referred to as tuple packing.
"""
a = 10
b = 20
c = 20
d = 40

# tuple packing
tuple1 = a, b, c, d # Packing tuple
print(tuple1) # (10, 20, 20, 40)

# tuple unpacking
d,c, b , a = tuple1
print(a, b, c, d)



