
# data abstraction - data hiding , hiding variable behind class in terms of access

class ineuron:
    __students = "data science "

    def students(self):
        print(" Print the class of students ", ineuron.__students)

i = ineuron()
i.students()

print( i._ineuron__students)
