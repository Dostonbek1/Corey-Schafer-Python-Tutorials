# Lists

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Education', 'Chemistry']
courses.append('Medicine')
courses.insert(0, 'Art')
courses.extend(courses_2)
courses.remove('Math')

print(len(courses))
print(courses[2])
print(courses[-3])
print(courses[:2])
print(courses[2:])

popped = courses.pop() # removes and returns last item
print(popped)

courses.reverse() # in-place
print(courses)

courses.sort() # in-place
print(courses)

courses.sort(reverse=True) # in-place
print(courses)

sorted_courses = sorted(courses) # not in-place
print(sorted_courses)

print(courses.index('CompSci'))
print('Art' in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

#Tuple
## Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

## Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # throws error


# Sets 
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = []
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()