# constructor counter uning class method 
class student():
    count=0
    def __init__(self,name):
        self.name=name
        student.count+=1
        print("student created")

    def __del__(self):
        student.count-+1
        print("student deleted")
    @classmethod
    def total_student(cls):
        print("total obj:", cls.count)  
s1=student("A")
S2=student("B")
s3=student("C")

student.total_student()
        