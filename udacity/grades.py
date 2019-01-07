print("Welcome to Grade Scripter\n\n")
names = (input("1. Enter student names separated by spaces:\n")).split()
# print(names)
assignments = (input("2. Enter number of missing assignments separated by spaces\n")).split()
assignments = list(map(int, assignments))
# print(assignments)
grades = (input("3. Enter students' current grades separated by spaces:\n")).split()
grades = list(map(int, grades))
# print(grades)

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# possible_grades = []
#
# def possible_grade(current_grade, num_missing):
#     return current_grade + num_missing * 2

for i in range(len(names)):
    possible_grade = grades[i] + assignments[i] * 2
    print(message.format(names[i], assignments[i], grades[i], possible_grade))
