
class student:

    __name = 0
    __rollno = 0

    def set_name(self, name):
        student.__name = name

    def get_name(self):
        return student.__name

    def set_rollno(self, rollno):
        student.__rollno = rollno
    
    def get_rollno(self):
        return student.__rollno

obj = student()
obj.set_name("rakesh")
print(obj.get_name())
obj.set_rollno(12)
print(obj.get_rollno())

        
