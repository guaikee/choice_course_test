from db import modules
from interface import common_interface as ci
from lib import common

user = {'obj': None}


def login():
    while True:
        name = input('name:').strip()
        pwd = input("pwd:").strip()
        if name and pwd:
            obj = modules.Teacher.get(name)
            if obj:
                if obj.pwd == pwd:
                    user['obj'] = obj
                    print('登录成功')
                    return
                else:
                    print('密码错误')
            else:
                print('用户不存在')
        else:
            print('内容不可为空')


@common.auth('teacher')
def check_course():
    course_list = user['obj'].course
    for i in course_list:
        print(i)


@common.auth('teacher')
def choice_course():
    school_name = user['obj'].school
    school_obj = modules.School.get(school_name)
    course_list = school_obj.course
    if course_list:
        for i, s in enumerate(course_list):
            print(i, s)
        choice = input('>>>').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course_list):
                user['obj'].choice_course(course_list[choice])
                print('选择课程成功')
            else:
                print('输入错误')
        else:
            print('输入错误')
    else:
        print('目前还没有任何课程')


@common.auth('teacher')
def marking():
    course_list = user['obj'].course
    for i, c in enumerate(course_list):
        print(i, c)
    if course_list:
        choice = input(">>>").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course_list):
                course_obj = modules.Course.get(course_list[choice])
                stu_list = course_obj.stu_list
                for i, s in enumerate(stu_list):
                    print(i, s)
                if stu_list:
                    choice1 = input(">>>").strip()
                    score = input('分数:').strip()
                    if choice1.isdigit() and score.isdigit():
                        choice1 = int(choice1)
                        score = int(score)
                        if choice1 < len(stu_list) and 0 <= score <= 100:
                            user['obj'].marking(stu_list[choice1], course_list[choice], score)
                            print('打分成功')
                        else:
                            print('输入错误')
                    else:
                        print('输入错误')
                else:
                    print('该课程目前没有学生')
            else:
                print('输入错误')
        else:
            print('输入错误')
    else:
        print('请先选择课程')


dic = {'1': login, '2': check_course, '3': choice_course, '4': marking}


def run():
    while True:
        print('''
        1.登录
        2.查看课程
        3.选择课程
        4.打分
        0.返回
        ''')
        choice = input('>>').strip()
        if choice in dic:
            dic[choice]()
        elif choice == '0':
            user['name'] = None
            return
