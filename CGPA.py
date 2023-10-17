class Student:
  def __init__(self,name,     roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students_list):
  #sort the list of students in desceding order of CGPA
  sorted_students=sorted(students_list,
                     key=lambda student:
                      student.cgpa,
                      reverse=True) 
  
  #syntax - lamda arg:exp
  return sorted_students

#Example useage:
students = [
      Student("RAVI","4622128002",7.8), 
      Student("VIJAY","4622128003",7.9), 
      Student("HARANIGA","4622128004",8.1), 
      Student("DHANA","4622128005",9.9),
]

sorted_students=sort_students(students)
#Print the shorted list of student 
for student in sorted_students:
  print ("Name:{},Roll number:{},CGPA:{}".format(student.name,student.roll_number,
                                                 student.cgpa))
