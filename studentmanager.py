from student import Student
import json

class StudentManager:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self,student):
        self.students.append(student)

   # view student 
    def view_student(self):
        if not self.students:
           print("No Student found")
           return
        
        for student in self.students:
         student.display()

    #search student
    def search_student(self,student_id):
       for student in self.students:
          if student.student_id == student_id:
             return student   
       return None 
     
    # update student
    def update_student(self,student_id,name,age,course,marks):
       student = self.search_student(student_id)
                               
       if student:
          student.name = name
          student.age = age
          student.course = course
          student.marks = marks
          return True

       return False
    
    # delete student
    def delete_student(self,student_id):
       student = self.search_student(student_id)

       if student:
          self.students.remove(student)
          return True
       
       return False
      
      # save data in file
    def save_file(self):
       data = []
       for student in self.students:
          data.append(student.to_dict())

       with open("data.json" , "w") as file:
             json.dump(data, file, indent=4)
                       
       print("Data Saved Successfully")      

      # load data in file
    def load_file(self):
      try:
         with open("data.json" , "r") as file:
            data = json.load(file) 

            for item in data:   
               student_data  = Student(
                  item["student_id"],
                  item["name"],
                  item["age"],
                  item["course"],
                  item["marks"]
               )          
               self.students.append(student_data) 
      except FileNotFoundError:
        print("No previous data found.")


    

