from grade_data import students

def validate_student(student):
    if isinstance(student,tuple):
        if len(student) == 2:
            if isinstance(student[0],str):
                return True
            else:
                return "Skipped student: Name must be a string"
        else:
            return "Skipped student: tuple must be two"
    else:
        return "Skipped student: is not a tuple"
            
                


def validate_grade(grade):
    pass
