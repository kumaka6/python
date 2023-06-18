class ineuron:
    __students = " data science "

# to call private variable inside in-class
    def students(self):
        print(" print the clas of students ", ineuron.__students)

i = ineuron()
i.students()

# k = i.__students  # can not access

print(i._ineuron__students)
# ^ above, the private variable can only be accessed using in-class
# data abstraction = phenomina where we're trying to hide variable under class
# when we're not allowing user to access the data.

# why hide ??
# when dont want user to access data directly.

list()