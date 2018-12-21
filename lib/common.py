def auth(type_name):
    from core import admin, student, teacher
    def inner(func):
        def wrapper(*args, **kwargs):
            if type_name == 'admin':
                if admin.user['obj']:
                    return func(*args, **kwargs)
                else:
                    admin.login()
            if type_name == 'teacher':
                if teacher.user['obj']:
                    return func(*args, **kwargs)
                else:
                    teacher.login()
            if type_name == 'student':
                if student.user['obj']:
                    return func(*args, **kwargs)
                else:
                    student.login()

        return wrapper

    return inner
