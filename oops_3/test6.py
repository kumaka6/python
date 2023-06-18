# polymorphism

class ineuron:
    def students(self):
        print(" print a students details ")

class class_type:
    def class_for_students(self):
        print(" print the class type of students")

def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()
ineuron_external(i)
ineuron_external(j)
def ser(a,b):
    return a + b


print(ser(3, 4))
print(ser("kumar", " thara"))
