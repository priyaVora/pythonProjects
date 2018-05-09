"""Developing in Third Party Framework
    Priya Vora
    5/7/2018
    Student Scores
"""
gradesfiles = open("studentgrades.txt", "r")


class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade



studentInfo={}
for each_student in gradesfiles:
    each_student = each_student.strip()
    studentInfo = each_student.split()
    current_student = Student(studentInfo[0], int(studentInfo[1]))
    scoreValue = (current_student.grade/5)
    score = int(scoreValue)
    for each in range(0, score):
        print("*", end="", flush=True)
    amount = 33 - int(score)
    print(" " + str(current_student.grade).rjust(amount))

