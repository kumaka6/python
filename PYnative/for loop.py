sum = 0
for i in range(2, 22, 2):
    sum = sum + i
print(sum)
# output 110

for num in range(10):
    print(num)

numbers = [1, 2, 3, 4, 5]
# iterate over each element in list num
for i in numbers:
    # ** exponent operator
    square = i ** 2
    print("Square of:", i, "is:", square)

numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
list_size = len(numbers)
average = sum / list_size
print(average)


# Reversed numbers using reversed() function
list1 = [10, 20, 30, 40]
for num in reversed(list1):
    print(num)

# outer loop
for i in range(1, 6):
    print('Multiplication table of:', i)
    count = 1
    # inner loop to print multiplication table of current number
    while count < 11:
        print(i * count, end=' ')
        count = count + 1
    print('\n')

odd = [1, 5, 7, 9]
even = [i + 1 for i in odd if i % 2 == 1]
print(even)


numbers = [4, 2, 5, 7, 8]
for i, v in enumerate(numbers):
    print('Numbers[', i, '] =', v)


dialogue = "Remember, Red, hope is a good thing, maybe the best of things, and no good thing ever dies"
# split on whitespace
for word in dialogue.split():
    print(word)

dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for key in dict1:
    print(key, "->", dict1[key])


dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for value in dict1.values():
    print(value)