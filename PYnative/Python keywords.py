
# to get list of keywords
import keyword
#print(list(keyword.kwlist))
x = (keyword.kwlist)
z = len(x)/5
print(z)

j = 1; k = 1
for i in x:
    print(i.center(15, " "), end="")
    if j/6 == k:
        print("")
        k = k+1
    j = j+1
    
"""
j= 1
for i in x:
    print(" ",j, ". ", i)
    j =j+1
"""

# list of keywords
"""
     False           None           True      __peg_parser__      and             as      
     assert         async          await          break          class         continue   
      def            del            elif           else          except        finally    
      for            from          global           if           import           in      
       is           lambda        nonlocal         not             or            pass     
     raise          return          try           while           with          yield    
"""

#help(keyword)

print(help('__peg_parser__'))
s = "__peg_parser__"
keyword.iskeyword(s)
keyword.issoftkeyword(s)
print(keyword.softkwlist)

x = "kumar"
y = "thara"
z = "kumar"
print(x is y)
print(x is z)

"""
with keyword is used when working with unmanaged resources (like file streams). 
It allows you to ensure that a resource is “cleaned up”
    when the code that uses it finishes running, even if exceptions are thrown.

"""


"""
# Opening file
with open('sample.txt', 'w', encoding='utf-8') as fp:
    # read sample.txt
    print(fp.read())
"""

