# https://app.codingrooms.com/management/assignments/364934/overview

student_scores = input("Input a list of student scores ").split()
highest = 0

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if highest < student_scores[n]:
        highest = student_scores[n]

print(f'The highest score in the class is: {highest}')