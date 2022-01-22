# Conditionals
if True:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print('Language is Python')

## Comparisons
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is  | checks if values have the same id

language = 'Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# Boolean Operations
## and
## or
## not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log in')
else:
    print('Welcome')

## is operation
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)

print(id(a))
print(id(b))
print(a is b)
print(a is c)

# False Values:
    # False
    # none
    # Zero of numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')