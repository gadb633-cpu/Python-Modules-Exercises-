from grade_data import students

def validate_student_and_grade(student,grade):
    try:
        if isinstance(student,tuple):
            if len(student) == 2:
                if isinstance(student[0],str):
                    if isinstance(student[1],int):
                        if 0 <grade <= 100:
                            return True
                        else:
                            return "Skipped student: Grade must be between 0 and 100"
                    else:
                        return "Skipped student: Grade must be an integer"
                else:
                    return "Skipped student: Name must be a string"
            else:
                return "Skipped student: tuple must be two"
        else:
            return "Skipped student: is not a tuple"
    except ValueError:
        return "valueerror"
    except TypeError:
        return "typeerror"
    



