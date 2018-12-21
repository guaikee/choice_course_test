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
                obj = modules.Admin.get(name)
                if not obj:
                    modules.Admin(name, pwd)
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
            obj = modules.Admin.get(name)
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

@common.auth('admin')
def create_school():
    name = input('学校名:').strip()
    addr = input('学校地址:').strip()
    if name and addr:
        school_obj = modules.School.get(name)
        if not school_obj:
            user['obj'].create_school(name, addr)
            print('创建学校成功')
        else:
            print('学校已存在')
    else:
        print('内容不可为空')

@common.auth('admin')
def create_teacher():
    school_list = ci.get_list('school')
    if school_list:
        for i, s in enumerate(school_list):
            print(i, s)
        choice = input('>>>').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                name = input('name:').strip()
                pwd = input("pwd:").strip()
                if name and pwd:
                    obj = modules.Teacher.get(name)
                    if not obj:
                        user['obj'].create_teacher(name, pwd, school_list[choice])
                        print('创建老师成功')
                    else:
                        print('该老师已存在')
                else:
                    print('内容不可为空')
            else:
                print('输入错误')
        else:
            print('输入错误')
    else:
        print('请先创建学校')

@common.auth('admin')
def create_course():
    school_list = ci.get_list('school')
    if school_list:
        for i, s in enumerate(school_list):
            print(i, s)
        choice = input('>>>').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                name = input('课程名称>>>').strip()
                if name:
                    obj = modules.Course.get(name)
                    if not obj:
                        user['obj'].create_course(name)
                        school_obj = modules.School.get(school_list[choice])
                        if name not in school_obj.course:
                            school_obj.add_course(name)
                            print('创建课程成功')
                        else:
                            print('该学校已有此课程')
                    else:
                        print('该课程已存在')
                else:
                    print('内容不可为空')
            else:
                print('输入错误')
        else:
            print('输入错误')
    else:
        print('请先创建学校')


dic = {'1': register, '2': login, '3': create_school, '4': create_teacher, '5': create_course}


def run():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建老师
        5.创建课程
        0.返回
        ''')
        choice = input('>>').strip()
        if choice in dic:
            dic[choice]()
        elif choice == '0':
            user['name'] = None
            return
