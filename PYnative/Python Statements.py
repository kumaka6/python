content = """
Multi line statement 
compound statement 
simple statement"""

print(content)
note = """ pythgon statement end with new line character, i.e., each line in a python script is a statment """
print("\nA satement is an instruction that a python iterpreter can execute \n", note)

# mainly four types of statement in Python
# print statement
# assignment statement
# conditional statement
# looping statement


# statement 1
print("Hello every one!")

# statement 2
x = 120

# statement 3
print(x)

# two statements in a single, multiple statement separated with semicolon ;
l = 10 ; m = 15

# statement 4
print(" area of rectangle is ", l * m)

# multi- line statement using back slash
addition =  10 + 20 + \
             30 + 40 + \
             50 + 60
print("multi-line statement ",addition)

# implicit continuation
addition = ( 10 + 20 +
             30 + 40 +
             50 + 60 )
print("implicit continuation ", addition)

# to create list
number_1 = [1,2,3,4,6,7,"kumar"]
print(number_1)

del number_1

        # compound statement
# contains ( groups of ) other statements; they affect or control the execution of those other statements in some way.

"""
if statement - control flow statement , execute statement under if the condition is true.
while statement - the loop statement repeatedly executes a code while particular condition is true.
for statment - in loop , we can iterate any sequence or iterable variable.
                the sequence can be string, list, set, tuple, dict
try statement - specifies exception handling 
with statement - Used to cleanup code for a group of statements, while the with statement allows the execution of initialization and finalization code around a block of code.

pass - useful as placeholder, nothing happens.
del - used to delete variable

return - return value that is an output of execution
import - to import modules, e.g. import DateTime

continue - skips the current iteration and move to the next iteration
break - stops the further execution and exits the loop


"""
