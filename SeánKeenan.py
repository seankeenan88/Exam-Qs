# Question 16(a)
# Student name: Seán Keenan

username = input("Please enter your username: ")
print("Welcome", username,"," "to the student result calculator.")


student_name = input("Please enter the students name: ")
student_score = float(input("Please enter the students mark: "))
score_as_a_percentage = (student_score/150.0)*100.0
exam_value = int(input("Please enter the total amount of marks going for the exam: "))
#round(student_score,score_as_a_percentage)


print(student_name,"scored",score_as_a_percentage,"%")

if student_score >=80:
    print("They got an A")
        
    if student_score >= 60:
        print("They got a B")
        
    if student_score < 60:
        print("They got a C")
        
        
        