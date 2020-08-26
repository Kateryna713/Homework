class GroupOfStudents:

    def __init__(self, student_list):

        self.student_list = student_list

    @property
    def group_average(self):
        sum_gr = 0
        for i in range(0, len(self.student_list)):
            sum_gr = sum_gr + self.student_list[i].get_grades()
        return sum_gr / len(self.student_list)

    @property
    def students_below_average(self):

        names = []

        average = self.group_average

        for i in range(0, len(self.student_list)):

            if self.student_list[i].get_grades() < average:
                names.append(self.student_list[i].get_name())

        return names

    @property
    def highest_grade(self):

        max = 0

        for i in range(0, len(self.student_list)):

            if self.student_list[i].get_grades() > max:
                max = self.student_list[i].get_grades()

        students = []

        for i in range(0, len(self.student_list)):
            if self.student_list[i].get_grades() == max:
                students.append(self.student_list[i].get_name())

        max_dict = {max: students}
        return max_dict

    def max_grade(self):

        max_dict = self.highest_grade
        for key in max_dict:
            print(f'Max grade = {key}')

    def students_enrolled_to_budget(self):
        print(f'Best students enrolled to budget are: ')
        max_dict = self.highest_grade
        for key in max_dict:

            temp = max_dict[key]
            for name in list(temp):
                print(f'\t {name}')

    def students_dropped_out(self):
        print(f'Students dropped out of the group are: ')
        students = self.students_below_average
        for student in students:
            print(f'\t {student}')


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __repr__(self):
        return f'Student {self.name}, grades {self.grades}'

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades


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
