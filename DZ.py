class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"


class Reviewer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def grade_homework(self, student, course, grade):
        student.receive_grade(course, grade)


class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.average_rating = None

    def receive_lecture_rating(self, course, rating):
        if not hasattr(self, 'lecture_ratings'):
            self.lecture_ratings = {}
        if course not in self.lecture_ratings:
            self.lecture_ratings[course] = []
        self.lecture_ratings[course].append(rating)

    def calculate_average_rating(self, course):
        if course in self.lecture_ratings:
            ratings = self.lecture_ratings[course]
            self.average_rating = sum(ratings) / len(ratings)
            return self.average_rating
        else:
            return None

    def __str__(self):
        if self.average_rating is None:
            return super().__str__() + "\nСредняя оценка за лекции: Нет данных"
        else:
            return super().__str__() + f"\nСредняя оценка за лекции: {self.average_rating}"


class Student(Person):
    def __init__(self, first_name, last_name, courses_in_progress=None, completed_courses=None):
        super().__init__(first_name, last_name)
        self.grades = {}
        self.courses_in_progress = courses_in_progress or []
        self.completed_courses = completed_courses or []

    def receive_grade(self, course, grade):
        self.grades[course] = grade

    def rate_lecturer(self, lecturer, course, rating):
        lecturer.receive_lecture_rating(course, rating)

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        completed_courses_str = ", ".join(self.completed_courses)
        if not self.courses_in_progress:
            courses_in_progress_str = "Нет курсов"
        if not self.completed_courses:
            completed_courses_str = "Нет курсов"
        return super().__str__() + f"\nСредняя оценка за домашние задания: {self.calculate_average_grade()}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {completed_courses_str}"

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0



def average_grade_for_course(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += student.grades[course]
            count += 1
    if count > 0:
        return total_grade / count
    else:
        return 0



def average_lecture_rating_for_course(lecturers, course):
    total_rating = 0
    count = 0
    for lecturer in lecturers:
        avg_rating = lecturer.calculate_average_rating(course)
        if avg_rating is not None:
            total_rating += avg_rating
            count += 1
    if count > 0:
        return total_rating / count
    else:
        return 0



some_reviewer = Reviewer("Some", "Buddy")
some_lecturer1 = Lecturer("John", "Doe")
some_lecturer2 = Lecturer("Jane", "Smith")
some_student1 = Student("Ruoy", "Eman", ["Python", "Git"], ["Введение в программирование"])
some_student2 = Student("Alex", "Green", ["Java"], [])


some_reviewer.grade_homework(some_student1, "Python", 9.5)
some_reviewer.grade_homework(some_student1, "Git", 8.5)
some_reviewer.grade_homework(some_student2, "Java", 7.5)

some_student1.rate_lecturer(some_lecturer1, "Python", 9.0)
some_student1.rate_lecturer(some_lecturer1, "Python", 8.5)
some_student1.rate_lecturer(some_lecturer2, "Python", 7.0)

some_student2.rate_lecturer(some_lecturer2, "Java", 8.0)

print(some_reviewer)
print(some_lecturer1)
print(some_lecturer2)
print(some_student1)
print(some_student2)

print("Средняя оценка за домашние задания по курсу Python:", average_grade_for_course([some_student1, some_student2], "Python"))
print("Средняя оценка за лекции по курсу Python:", average_lecture_rating_for_course([some_lecturer1, some_lecturer2], "Python"))
