from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    roster = []

    roster.append(Student("Will", 100))
    roster.append(Student("John", 95))
    roster.append(Student("Martin", 84))
    roster.append(Student("Matt", 97))
    roster.append(Student("Fiona", 77))
    roster.append(Student("Carrie", 82))
    roster.append(Student("Anthony", 100))
    roster.append(Student("Joe", 68))
    roster.append(Student("Lisa", 89))
    roster.append(Student("Sarah", 92))

    for i in roster:
        i.print_student_info()

    (average_grade(roster))

__main__()