
from modules import my_module as mm
import sys
# sys.path.append('c:\\Users\\Dostonbek Toirov\\Desktop\\me\\github\\CoreySchaferPythonTutorials\\modules')

print(sys.path)
# from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)


import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))


import os 

print(os.getcwd())
print(os.__file__)

import antigravity