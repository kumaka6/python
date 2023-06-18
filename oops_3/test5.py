# incapitulation

class ineuron:
    def __init__(self):
        self.students1 = " data science "

    def students(self):
        print(self.students1)

i = ineuron()
i.students()

#when data member and member function name are same, error
i.students1 = "data analytics"  # over ridding
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = " data science "

    def students(self):
        print(self.__students1)

    def student_change(self, new_value):  # setter function
        self.__students1 = new_value


i1 = ineuron1()
i1.students()
i1.__students1= "big data"
i1.students()
i1.student_change("kumar")
i1.students()

# inside class, we can able to change value using other class
# without using class method we can not change value of private variable
# encapsulation ?
# setter and getter ??
# Abstracting (data hiding) (access) vs encapsulation ?? (modification)

