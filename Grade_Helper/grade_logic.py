from grade_data import students


def get_grade_status(grade):

    if grade>= 90:
        return "Excellent"
    elif 60<=grade< 89:
        return "passed" 
    elif grade< 60:
        return "failed"
    


def calculate_average(sum_grade,num_student_normal):
    return f"Average: {sum_grade/num_student_normal}"
    

def count_passed_students(num_passed):
    return num_passed

    
