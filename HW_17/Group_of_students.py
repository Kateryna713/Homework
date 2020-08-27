class GroupOfStudents:

    def __init__(self, student_list):
        self.student_list = student_list

    @property
    def group_average(self):
        sum_gr = 0
        for student in self.student_list:
            sum_gr = sum_gr + student.grades
        return sum_gr / len(self.student_list)

    @property
    def students_below_average(self):

        names = []

        for student in self.student_list:

            if student.grades < self.group_average:
                names.append(student)

        return names

    @property
    def highest_grade(self):

        max = 0

        for student in self.student_list:

            if student.grades > max:
                max = student.grades

        students = []

        for student in self.student_list:

            if student.grades == max:
                students.append(student)

        return {max: students}

    def max_grade(self):
        for key in self.highest_grade:
            print(f'Max grade = {key}')

    def students_enrolled_to_budget(self):
        print(f'Best students enrolled to budget are: ')
        for key in self.highest_grade:
            for name in list(self.highest_grade[key]):
                print(f'\t {name}')

    def students_dropped_out(self):
        print(f'Students dropped out of the group are: ')
        for student in self.students_below_average:
            print(f'\t {student}')


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __repr__(self):
        return f'Student {self.name}, grades {self.grades}'


def main():
    students = []

    n = int(input('Enter a number of students in the group: '))
    for i in range(0, n):
        name = input(' Enter name: ')
        grades = int(input(' Enter grades: '))
        student = Student(name, grades)
        students.append(student)
    print(f'Total list of students:')
    for student in students:
        print(f'\t {student}')

    g = GroupOfStudents(students)

    print(f'Group Average: {g.group_average}')

    g.max_grade()
    g.students_dropped_out()
    g.students_enrolled_to_budget()


if __name__ == '__main__':
    main()
