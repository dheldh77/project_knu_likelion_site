import datetime
import random

def get_filename(filename):
    string = "asdf"
    for i in range(1,20):
        string+=str(random.randrange(0,10))
        
    return filename.upper()+string