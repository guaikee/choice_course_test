import os
from conf import settings

def get_list(name):
    path = os.path.join(settings.DB_PATH,name)
    return os.listdir(path)