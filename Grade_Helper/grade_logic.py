from grade_data import get_students
from grade_validation import validate_grade,validate_student



def get_grade_status(grade):
    sum_grade=0
    num_studends_passed=0
    for grade in get_students():
        try:
            if grade[1] >=90:
                num_studends_passed+=1
                sum_grade+=grade[1]
                print(f"{grade}Excellent")
                
            elif grade[1]>60 and grade[1]<89:
                num_studends_passed+=1
                sum_grade+=grade[1]
                print(f"{grade}passed")
                
            elif grade[1]<60:
                print(f"{grade}failed")
            

        except TypeError:
            print("is not a int")
    return [num_studends_passed,sum_grade]

passed_students_and_average = get_grade_status(get_students)    
print(f"students the passed: {passed_students_and_average[0]} \nsummary: {passed_students_and_average[1]}")

def calculate_average(students):
    calculate_average_ = passed_students_and_average[1]/passed_students_and_average[0]
    return calculate_average_
print(f"average: {calculate_average(get_students)}")

def count_passed_students(students):
    num_studends_passed_ =get_grade_status(students)
    return num_studends_passed_



    # sum_grade=0
    # num_studends_passed=0
    # for grade in students:
    #     try:
    #         if grade[1] >=90:
    #             print(f"{grade}Excellent")
    #             num_studends_passed+=1
    #             sum_grade+=grade[1]
    #         elif grade[1]>60 and grade[1]<89:
    #             print(f"{grade}passed")
    #             num_studends_passed+=1
    #             sum_grade+=grade[1]
    #         elif grade[1]<60:
    #             print(f"{grade}failed")
    #     except TypeError:
    #         print("is not a int")
    # return num_studends_passed
    # return sum_grade

    # average = sum_grade / num_studends_passed
    # print(average)