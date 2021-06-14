from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses or self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades and 1 <= grade <= 10:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        for i in self.grades.items():
            av_grade = round(mean(i[1]), 1)
            return av_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания:{self.average_grade() if len(self.grades) > 0 else "Оценок пока нет"}\
        \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Этот человек не является студентом!')
            return
        if self.average_grade() > other.average_grade():
            return f'{self.name} {self.surname} получил(а) средний балл выше'
        else:
            return f'{other.name} {other.surname} получил(а) средний балл выше'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        for i in self.grades.items():
            av_grade = round(mean(i[1]), 1)
            return av_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self.average_grade() if len(self.grades) > 0 else "Оценок пока нет"}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Этот человек не является лектором!')
            return
        if self.average_grade() > other.average_grade():
            return f'{self.name} {self.surname} получил(а) средний балл выше'
        else:
            return f'{other.name} {other.surname} получил(а) средний балл выше'


first_reviewer = Reviewer('Филипп', 'Воронов')
first_reviewer.courses_attached = 'HTML и CSS', 'JavaScript', 'GIT'
second_reviewer = Reviewer('Алёна', 'Батицкая')
second_reviewer.courses_attached = 'HTML и CSS', 'JavaScript', 'GIT', 'Python для начинающих'

first_student = Student('Наталья', 'Дмитриева', 'Ж')
first_student.finished_courses = 'GIT'
first_student.courses_in_progress = 'Python для начинающих'
second_student = Student('Иван', 'Иванов', 'М')
second_student.finished_courses = 'HTML и CSS'
second_student.courses_in_progress = 'JavaScript'

first_lecturer = Lecturer('Дмитрий', 'Качалов')
first_lecturer.courses_attached = 'GIT', 'JavaScript'
second_lecturer = Lecturer('Владимир', 'Языков')
second_lecturer.courses_attached = 'HTML и CSS', 'JavaScript'

first_reviewer.rate_hw(second_student, 'JavaScript', 10)
first_reviewer.rate_hw(second_student, 'JavaScript', 9)
first_reviewer.rate_hw(second_student, 'JavaScript', 9)

second_reviewer.rate_hw(first_student, 'Python для начинающих', 10)
second_reviewer.rate_hw(first_student, 'Python для начинающих', 10)
second_reviewer.rate_hw(first_student, 'Python для начинающих', 10)

first_student.rate_hw(first_lecturer, 'GIT', 5)
first_student.rate_hw(first_lecturer, 'GIT', 4)
first_student.rate_hw(first_lecturer, 'GIT', 3)

second_student.rate_hw(second_lecturer, 'HTML и CSS', 10)
second_student.rate_hw(second_lecturer, 'HTML и CSS', 8)
second_student.rate_hw(second_lecturer, 'JavaScript', 10)

print(first_student.__str__())
print(second_student.__str__())
print(first_reviewer.__str__())
print(second_reviewer.__str__())
print(first_lecturer.__str__())
print(second_lecturer.__str__())
print(first_lecturer > second_lecturer)
print(second_student > first_student)


def lecturers_average_mark(lecturer_list, course):
    mark_list = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            mark_list.append(lecturer.grades)
    for elem in mark_list:
        return round(mean(elem.get(course, None)), 1)


average_mark_person = lecturers_average_mark([first_lecturer, second_lecturer], 'GIT')
print(average_mark_person)


def students_average_mark(student_list, course):
    mark_list = []
    for student in student_list:
        if course in student.grades:
            mark_list.append(student.grades)
    for elem in mark_list:
        return round(mean(elem.get(course, None)), 1)


average_mark_student = students_average_mark([first_student, second_student], 'JavaScript')
print(average_mark_student)
