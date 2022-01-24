li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li) 
li.sort() # in-place

print('Sorted list:\t', s_li)
print(li)

s_li = sorted(li, reverse=True)
li.sort(reverse=True)

tup = (9,1,8,2,7,3,6,4,5) # tuple cannot be sorted in place
s_tup = sorted(tup) 
print(s_tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None}
s_di = sorted(di) # sorts the keys of dict and returns a list of keys
print(s_di)

#####
li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print(s_li)

s_li2 = sorted(li, key=abs)
print(s_li2)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employees = [e1,e2, e3]
def e_sort(emp):
    return emp.name

from operator import attrgetter

s_employees = sorted(employees, key=e_sort, reverse=True)
s_employees2 = sorted(employees, key=lambda e: e.name)
s_employees3 = sorted(employees, key=attrgetter('name'))

print(s_employees)
print(s_employees2)
print(s_employees3)