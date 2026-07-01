from grade_data import students
from grade_logic import calculate_average,count_passed_students,get_grade_status
from grade_output import print_student_result,print_summary
from grade_validation import validate_student_and_grade


def run_grade_helper(students):
    sum_grade = 0
    num_passed = 0
    num_student_normal = 0
    for student in students:
        if validate_student_and_grade(student,student[1])==True:
            status = get_grade_status(student[1])
            sum_grade += student[1]
            num_student_normal += 1
            if status!= "failed":
                num_passed +=1
            print(print_student_result(student[0],student[1],status))
        else:
            print(validate_student_and_grade(student,student[1]))
    print(calculate_average(sum_grade,num_student_normal))
    print(f"num passed: {num_passed}")          




