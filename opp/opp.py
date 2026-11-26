class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


s = Student()  # Create an object

print("Before setting marks:", s.get_marks())

s.set_marks(80)

print("After setting marks:", s.get_marks())