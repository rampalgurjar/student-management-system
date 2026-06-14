# student class
class Student:
    def __init__(self,student_id,name,age,course,marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
        
    # find average
    def calculate_average(self):
        total =0
        for eachvalue in self.marks:
            total = total + eachvalue

        average = total /len(self.marks)
        return average
        
    # Calculate grade
    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return("A")
        elif 80 <= avg < 90:
            return("B")
        elif 70 <= avg < 80:
            return("C")
        elif 60 <= avg < 70:
            return("D")
        else:
            return("Fail")  

    # display the data        
    def display(self):
        avg = self.calculate_average()
        grade = self.calculate_grade()

        print("="*20)
        print("Student_ID :",self.student_id)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Course : ",self.course)
        print("Marks : ",self.marks)
        print("Average : ",avg)
        print("Grade : ",grade)
        print("="* 20)


    # dictionary me data ko file me save karne ke liye
    def to_dict(self):
        dataofstudent={
            "student_id":self.student_id,
            "name":self.name,
            "age":self.age,
            "course":self.course,
            "marks":self.marks,
            "average":self.calculate_average(),
            "grade":self.calculate_grade()
        }
        return dataofstudent
        
