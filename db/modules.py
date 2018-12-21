from db import db_handler


class BasesClass:
    @classmethod
    def get(cls, name):
        return db_handler.search(cls.__name__.lower(), name)

    def save(self):
        db_handler.save(self)


class Admin(BasesClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def create_school(self, name, addr):
        School(name, addr)

    def create_teacher(self, name, pwd, school):
        Teacher(name, pwd, school)

    def create_course(self, name):
        Course(name)


class Teacher(BasesClass):
    def __init__(self, name, pwd, school):
        self.name = name
        self.pwd = pwd
        self.school = school
        self.course = []
        self.save()

    def choice_course(self, course):
        self.course.append(course)
        self.save()

    def marking(self, stu, course, score):
        stu.score[course] = score
        stu.save()


class Student(BasesClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.course = []
        self.score = {}
        self.save()

    def choice_school(self, school):
        self.school = school
        self.save()

    def choice_course(self, course):
        self.course.append(course)
        self.save()


class School(BasesClass):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = []
        self.save()

    def add_course(self, course_name):
        self.course.append(course_name)
        self.save()


class Course(BasesClass):
    def __init__(self, name, period='5mons', price=20000):
        self.name = name
        self.period = period
        self.price = price
        self.stu_list = []
        self.save()

    def add_stu(self, stu):
        self.stu_list.append(stu)
        self.save()
