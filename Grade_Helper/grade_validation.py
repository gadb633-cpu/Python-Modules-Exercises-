from grade_data import get_students

# def validate_student(student):
#     for name in get_students():
#         if type(name[0])!=str:
#             return "Name must be a string" 
#         elif type(name[1])!=int:
#             return "Grade must be an integer"  
        
        
# def validate_grade(grade):
#     for name in get_students():
#         if name[1]>100:
#             return "Grade must be between 0 and 100"    
#         elif name[1]<0:
#             return "Grade must be between 0 and 100"

def loop_student():
    for student in get_students():
        return student
    

def validate_student(student):
    
    if type(student[0])!=str:
        return False 
    elif type(student[1])!=int:
        return False
    elif student[1]>100:
        return False  
    elif student[1]<0:
        return False
    else:
        return True
    

print(validate_student(loop_student()))        
                
# def validate_grade(grade):
#     for name in get_students():
#         if name[1]>100:
#             return False  
#         elif name[1]<0:
#             return False       
# validate_grade(get_students)        