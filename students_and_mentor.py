from pprint import pprint

students = []
lecturers = []


class Student:
    def __init__(self, name, surname, gender=None):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_of_grades = 0
        self.number_of_grades = 0
        students.append(self)

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
            else:
                lecturer.grades[course] = [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
        else:
            print('Error')

    def __str__(self):
        self.list_of_courses_progress = ''
        self.list_of_finished_courses = ''

        for element in self.courses_in_progress:
            self.list_of_courses_progress += element
            if element != self.courses_in_progress[-1]:
                self.list_of_courses_progress += ', '

        for element in self.finished_courses:
            self.list_of_finished_courses += element
            if element != self.finished_courses[-1]:
                self.list_of_finished_courses += ', '

        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.sum_of_grades / self.number_of_grades}\n'
                  f'Курсы в процессе изучения: {self.list_of_courses_progress}\n'
                  f'Завершенные курсы: {self.list_of_finished_courses}\n')
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Его/ее нет в наших рядах!'
        else:
            return self.sum_of_grades / self.number_of_grades < other.sum_of_grades / other.number_of_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n')
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.sum_of_grades = 0
        self.number_of_grades = 0
        lecturers.append(self)

    def __str__(self):
        return super(Lecturer,
                     self).__str__() + f'Средняя оценка за лекции: {self.sum_of_grades / self.number_of_grades}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Его/ее нет в наших рядах!'
        else:
            return self.sum_of_grades / self.number_of_grades < other.sum_of_grades / other.number_of_grades


class Reviewer(Mentor):

    def rate_student_hw(self, student, course, grade=None):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
            else:
                student.grades[course] = [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
        else:
            print('Error')


def average_student_grade(list_student, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for student in list_student:
        for course, grades in student.grades.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Средняя оценка студента = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')


def average_lecturer_grade(list_lecturer, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for lecturer in list_lecturer:
        for course, grades in lecturer.grades.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Средняя оценка лектора = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')


student1 = Student('Ян', 'Митин')
student2 = Student('София ', 'Митин')

mentor1 = Mentor('Иван', 'Поддубный')
mentor2 = Mentor('Николай', 'Тесла')

lecturer1 = Lecturer('Олег', 'Черный')
lecturer2 = Lecturer('Александр', 'Белый')

reviewer1 = Reviewer('Владимир', 'Кровавый')
reviewer2 = Reviewer('Дмитрий', 'Смешной')

student1.add_finished_courses('Python-Free')
student1.add_finished_courses('Введение в программирование')
student1.add_courses_in_progress('Python')
student1.add_courses_in_progress('Git')

student2.add_finished_courses('C#')
student2.add_finished_courses('Введение в программирование')
student2.add_courses_in_progress('Git')
student2.add_courses_in_progress('Python')

mentor1.add_courses_attached('Python')
mentor1.add_courses_attached('Git')

mentor2.add_courses_attached('Python')
mentor2.add_courses_attached('Git')

lecturer1.add_courses_attached('Python')
lecturer1.add_courses_attached('Git')

lecturer1.add_courses_attached('Git')
lecturer1.add_courses_attached('Python')

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer1, 'Git', 8)
student1.rate_lecturer(lecturer1, 'Git', 7)

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 4)
student2.rate_lecturer(lecturer1, 'Git', 5)
student2.rate_lecturer(lecturer1, 'Git', 2)

reviewer1.add_courses_attached('Python')
reviewer1.add_courses_attached('Git')
reviewer1.rate_student_hw(student1, 'Python', 10)
reviewer1.rate_student_hw(student1, 'Git', 9)
reviewer1.rate_student_hw(student1, 'Python', 10)
reviewer1.rate_student_hw(student1, 'Git', 10)

reviewer2.add_courses_attached('Python')
reviewer2.add_courses_attached('Git')
reviewer2.rate_student_hw(student1, 'Python', 5)
reviewer2.rate_student_hw(student1, 'Git', 5)
reviewer2.rate_student_hw(student1, 'Python', 10)
reviewer2.rate_student_hw(student1, 'Git', 6)



average_student_grade(students, 'Python')
average_lecturer_grade(lecturers, 'Git')

print()
pprint(student1.__dict__)
pprint(student1.__dict__)
pprint(mentor1.__dict__)
pprint(mentor1.__dict__)
pprint(lecturer1.__dict__)
pprint(lecturer2.__dict__)
pprint(reviewer1.__dict__)
pprint(reviewer2.__dict__)