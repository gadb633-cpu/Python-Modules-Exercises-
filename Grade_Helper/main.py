from grade_data import students


sum_grade = 0
num_passed = 0
num_student_normal = 0
for student in students:
    if isinstance(student,tuple):
        if isinstance(student[0],str):
            if isinstance(student[1],int):
                if 0 < student[1] <= 100:
                    if student[1]>= 90:
                        sum_grade += student[1]
                        num_student_normal +=1
                        num_passed +=1
                        print(student[0],student[1],"Excellent")
                    elif 60<=student[1]< 89:
                        sum_grade += student[1]
                        num_student_normal +=1
                        num_passed +=1
                        print(student[0],student[1],"passed")
                    elif student[1]< 60:
                        num_student_normal +=1
                        sum_grade += student[1]
                        print(student[0],student[1],"failed")
                else:
                    print("Skipped student: Grade must be between 0 and 100")               
            else:
                print("Skipped student: Grade must be an integer")
        else:
            print("Skipped student: Name must be a string")        
    else:
        print("Skipped student: is not a tuple")
print(num_passed)
print(sum_grade/num_student_normal)












