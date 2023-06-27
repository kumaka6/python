


num = 90
result = isinstance(num, int)
if result:
    print("Yes")
else:
    print("No")


platform = "PYnative"
print(type(platform))  # <class 'str'>

# display string
print(platform)  # 'PYnative'

# accessing 2nd character of a string
print(platform[1])  # Y

platform = "PYnative"
# Now let's try to change 2nd character of a string.
#platform[0] = 'p'
# Gives TypeError: 'str' object does not support item assignment

# store int value
roll_no = 33
# display roll no
print("Roll number is:", roll_no)
# output 33
print(type(roll_no))
# output class 'int'

# store integer using int() class
id = int(25)
print(id)  # 25
print(type(id))  # class 'int'


# store a floating-point value
salary = 8000.456
print("Salary is :", salary)  # 8000.456
print(type(salary))  # class 'float'

# store a floating-point value using float() class
num = float(54.75)
print(num)  # 54.75
print(type(num))  # class 'float'

# exponential float
num1 = 1.22e4
print(num1)  # 12200.0
print(type(num1))  # class 'float'

x = 9 + 8j  # both value are int type
y = 10 + 4.5j  # one int and one float
z = 11.2 + 1.2j  # both value are float type
print(type(x))  # class 'complex'>

print(x)  # (9+8j)
print(y)  # (10+4.5j)
print(z)  # (11.2+1.2j)

my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)  # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))  # class 'list'

# Accessing first element of list
print(my_list[0])  # 'Jessa'

# slicing list elements
print(my_list[1:5])  # ['Kelly', 20, 35.75]

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])  # 'Emma'

# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)  # ['Jessa', 'Kelly', 20, 35.75]

# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)

# create a dictionary
my_dict = {1: "Smith", 2: "Emma", 3: "Jessa"}

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# create a dictionary using a dit class
my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Smith

# change the value of a key
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly

# create a set using curly brackets{,}
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# create a set using set class
my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}

# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Jessa', 300}

my_set = {11, 44, 75, 89, 56}
print(type(my_set))  # class 'set'

# creating frozenset
f_set = frozenset(my_set)
print(type(f_set))  # class 'frozenset'


x = 25
y = 20

z = x > y
print(z)  # True
print(type(z))  # class 'bool'

a = [9, 14, 17, 11, 78]
b = bytes(a)
print(type(b))  # class 'bytes'
print(b[0])  # 9
print(b[-1])  # 78

# create a bytearray
list1 = [9, 17, 11, 78]
b_array = bytearray(list1)
print(b_array)
print(type(b_array))  # class 'bytearray'

# modifying bytearray
b_array[1] = 99
print(b_array[1])  # 99

# iterate bytearray
for i in b_array:
    print(i, end=" ")  # 9 99 11 78

# Generate integer numbers from 10 to 14
numbers = range(10, 15, 1)
print(type(numbers))  # class 'range'

# iterate range using for loop
for i in range(10, 25, 2):
    print(i, end=" ")
# Output 10 11 12 13 14


