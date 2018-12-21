from core import admin,student,teacher


dic = {'1':admin.run,'2':teacher.run,'3':student.run}

def run():
    while True:
        print('''
        1.管理员视图
        2.老师视图
        3.学生视图
        ''')
        choice = input('>>').strip()
        if choice not in dic:continue
        dic[choice]()
