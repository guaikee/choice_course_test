import os
import pickle
from conf import settings

def search(type_name,name):
    path = os.path.join(settings.DB_PATH,type_name,name)
    if os.path.exists(path):
        with open(path,'rb') as f:
            obj = pickle.load(f)
            return obj

def save(obj):
    path = os.path.join(settings.DB_PATH, obj.__class__.__name__.lower(),obj.name)
    with open(path, 'wb') as f:
        pickle.dump(obj,f)







