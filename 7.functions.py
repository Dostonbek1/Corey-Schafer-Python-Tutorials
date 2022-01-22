def hello_func():
    pass

print(hello_func)
print(hello_func())

def hello_func():
    print('Hello Function!')

hello_func()

# Keep code DRY (Don't Repeat Yourself)

# returning value from a function
def hello_func():
    return 'Hello Function'

print(hello_func())
print(hello_func().upper())

# passing arguments
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting, name='You'):
    return '{}, {}!'.format(greeting, name)

print(hello_func('Hi'))

def student_info(*args, **kwargs):
    print(args) # arbitrary number of positional arguments
    print(kwargs) # arbitrary number of keyword arguments

    print(args[0])
    print(kwargs.get('name'))

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

## Calculating days in a certain month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years"""
    
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
print(days_in_month(2022, 2))