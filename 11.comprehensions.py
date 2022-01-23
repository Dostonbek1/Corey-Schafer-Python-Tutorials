nums = [1, 2, 3, 3, 4, 5, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]

####
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list = [n*n for n in nums]
print(my_list)

# using map + lambda
# my_list = map(lambda n: n*n, nums) # python 2.7
# print(my_list)

# n when it is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


# Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip (names, heroes):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 2, 4, 5, 6, 4, 5, 6, 7, 8]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 3, 4, 5, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n*n

# my_gen = gen_func(nums)
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)