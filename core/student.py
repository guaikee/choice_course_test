from db import modules
from interface import common_interface as ci
from lib import common

user = {'obj': None}


def register():
    while True:
        name = input('name:').strip()
        pwd = input("pwd:").strip()
        pwd1 = input('again:').strip()
        if name and pwd:
            if pwd == pwd1:
                obj = modules.Student.get(name)
                if not obj:
                    modules.Student(name, pwd)
                    print('注册成功')
                    return
                print('用户已存在')
            else:
                print('密码不一致')
        else:
            print('内容不可为空')


def login():
    while True:
        name = input('name:').strip()
        pwd = input("pwd:").strip()
        if name and pwd:
            obj = modules.Student.get(name)
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


@common.auth('student')
def choice_school():
    school_list = ci.get_list('school')
    if school_list:
        for i, s in enumerate(school_list):
            print(i, s)
        choice = input('>>>').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                user['obj'].choice_school(school_list[choice])
                print('选择成功')
            else:
                print('密码错误')
        else:
            print('密码错误')
    else:
        print('请联系管理员创建学校')


@common.auth('student')
def choice_course():
    school_name = user['obj'].school
    print(school_name)
    school_obj = modules.School.get(school_name)
    course_list = school_obj.course
    print(course_list)
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


@common.auth('student')
def check_score():
    score_dic = user['obj'].score
    for k in score_dic:
        print(k, score_dic[k])


dic = {'1': register, '2': login, '3': choice_school, '4': choice_course, '5': check_score}


def run():
    while True:
        print('''
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看成绩
        0.返回
        ''')
        choice = input('>>').strip()
        if choice in dic:
            dic[choice]()
        elif choice == '0':
            user['name'] = None
            return
