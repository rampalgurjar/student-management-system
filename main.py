from student import Student
from studentmanager import StudentManager

manager = StudentManager()

manager.load_file()

while True:
    print("========STUDENT MANAGEMENT SYSTEM===========")
    print("1) Add Student")
    print("2) View Student")
    print("3) Search Stuent")
    print("4) Update Student")
    print("5) Delete Student")
    print("6) Exit")

    choice = int(input("Enter Your choice: "))
    # add student
    if choice == 1:
        name = input("Enter the student Name : ")
        age = int(input("Enter the Student Age : "))
        course = input("Enter the course name : ")

        marks =[]

        noofsubject = int(input("How Many Subject ? : "))

        for i in range(noofsubject):
            mark = int(input(f"Enter subject {i+1} marks : "))
            marks.append(mark)

        student_id = manager.generate_id()    


        student = Student(
                student_id,
                name,
                age,
                course,
                marks
                 )
        
        result = manager.add_student(student)
        if result:
          print("Student Added Successfully!")    
        else:
            print("Student ID Already Exists!")    
        

    # view student
    elif choice == 2:
        manager.view_student()
        
    # search student 
    elif choice ==3:
        student_id = int(input("Enter Student id : "))
        student = manager.search_student(student_id)
        if student:
            print("Student Found")
            student.display()
        else:
            print("Not Found")    
        

    # update student
    elif choice == 4:
        student_id = int(input("Enter student id to update : "))
        name = input("Enter name to update : ")
        age = int(input("Enter age to update : "))
        course = input("Enter course to update : ")
        marks = []
        noofsubject = int(input("Enter Number of Subject : "))
        for i in range(noofsubject):
            mark = int(input(f"Enter student {i+1} mark"))
            marks.append(mark)                        

        result = manager.update_student(student_id,name,age,course,marks)

        if result:
          print("Student Updated Successfully")
        else:
          print("Student Not Found")   

    # delete student
    elif choice == 5:
        student_id = int(input("Enter the Student ID : "))
        result = manager.delete_student(student_id)    
        if result:
            print("Student Delete Successfull")
        else:
            print("Student Not Found")


    # Exit
    elif choice == 6:
       manager.save_file()
       break      
