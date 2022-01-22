students = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(students)
print(students['name'])
print(students['courses'])
# print(students['phone']) # throws key error
print(students.get('phone')) # returns None if doesn't exist
print(students.get('phone', 'Not Found')) # returns 'Not Found' if key doesn't exist

# adding/updating value
students['phone'] = '777-7777'
students['age'] = 28

students.update({'name': 'Jane', 'age':22})

# deleting key/value
del students['name']
age = students.pop('age') # removes and returns popped value
print(age)

print(students)

# loop through dicts
print(students.keys())
print(students.values())
print(students.items()) # both keys and values

for key in students:
    print(key)

for key, value in students.items():
    print(key, value)
