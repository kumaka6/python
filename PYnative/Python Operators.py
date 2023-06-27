"""
Python has seven types of operators that we can use to perform different operation and produce a result.
    Arithmetic operator
    Relational operators
    Assignment operators
    Logical operators
    Membership operators
    Identity operators
    Bitwise operators

** Arithmetic operator **
Arithmetic operators are the most commonly used.
The Python programming language provides arithmetic operators that perform addition, subtraction, multiplication, and division.
It works the same as basic mathematics.

There are seven arithmetic operators we can use to perform different mathematical operations, such as:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
// Floor division)
℅ (Modulus)
** (Exponentiation)



"""
x = 13
y = 4

print(x % y)
# Output 1

x = 2
y = 4
z = 2.2

# normal division
print(y / x)
# Output 2.0

# floor division to get result as integer
print(y // x)
# Output 2

# normal division
print(y / z)  # 1.81

# floor division.
# Result as float because one argument is float
print(y // z)  # 1.0

x = 2
y = 4
z = 8
print(y / x)
# Output 2.0
print(z / y / x)
# Output 1.0
# print(z / 0)  # error

num = 2
# 2*2
print(num ** 2)
# Output 4

# 2*2*2
print(num ** 3)
# Output 8

x = 10
y = 5
z = 2

# > Greater than
print(x > y)  # True
print(x > y > z)  # True

# < Less than
print(x < y)  # False
print(y < x)  # True

# Equal to
print(x == y)  # False
print(x == 10)  # True

# != Not Equal to
print(x != y)  # True
print(10 != x)  # False

# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True

# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True

a = 4
b = 2

a += b
print(a)  # 6

a = 4
a -= 2
print(a)  # 2

a = 4
a *= 2
print(a)  # 8

a = 4
a /= 2
print(a)  # 2.0

a = 4
a **= 2
print(a)  # 16

a = 5
a %= 2
print(a)  # 1

a = 4
a //= 2
print(a)  # 2

print(True and False)  # False
# both are True
print(True and True)  # True
print(False and False)  # False
print(False and True)  # false

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")

"""
In the case of arithmetic values, Logical and always returns the second value; as a result.
"""
print(10 and 20) # 20
print(10 and 5)  # 5
print(100 and 300) # 300

"""
In the case of arithmetic values, Logical or it always returns the first value; as a result.
"""
print(10 or 20) # 10
print(10 or 5) # 10
print(100 or 300) # 100

print(not False)  # True return complements result
print(not True)  # True return complements result

# actual use in code
a = True

# Logical not
if not a:
    # a is True so expression is False
    print(a)
else:
    print("Do nothing")


"""
In the case of arithmetic values, Logical not always return False for nonzero value.
"""
print(not 10) # False. Non-zero value
print(not 1)  # False. Non-zero value
print(not 5)  # False. Non-zero value
print(not 0)  # True. zero value

my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")

my_tuple = (11, 15, 21, 29, 50, 70)
number = 35
if number not in my_tuple:
    print("number is not present")
else:
    print("number is present")


x = 10
y = 11
z = 10
print(x is y) # it compare memory address of x and y
print(x is z) # it compare memory address of x and z
print(x is (z))

x = 10
y = 11
z = 10
print(x is not y) # it campare memory address of x and y
print(x is not z) # it campare memory address of x and z


"""
Bitwise Operators
In Python, bitwise operators are used to performing bitwise operations on integers. 
To perform bitwise, we first need to convert integer value to binary (0 and 1) value.

The bitwise operator operates on values bit by bit, so it’s called bitwise.
It always returns the result in decimal format. Python has 6 bitwise operators listed below.

& Bitwise and
| Bitwise or
^ Bitwise xor
~ Bitwise 1’s complement
<< Bitwise left-shift
>> Bitwise right-shift

"""

a = 7
b = 4
c = 5
print(a & b)
print(a & c)
print(b & c)

a = 7
b = 4
c = 5
print(a | b)
print(a | c)
print(b | c)

a = 7
b = 4
c = 5
print(a ^ c)
print(b ^ c)

a = 7
b = 4
c = 3
print(~a, ~b, ~c)
# Output -8 -5 -4

print(4 << 2)
# Output 16
print(5 << 3)
# Output 40

print(4 >> 2)
# Output
print(5 >> 2)
# Output