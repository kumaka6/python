class ineuron:
    def student(self):
        print(" print the details of all the students ")

    def achivers(self):
        print(" print the list of all the achivers")

    def hall_of_fame(self):
        print(" print everyone from hall of fame")


class ineuron_vision(ineuron):

    # redefining student details, definition
    def student(self):
        print(" re-defined student : Print the details of all student")


iv = ineuron_vision()

iv.student()