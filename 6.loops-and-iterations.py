nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break/continue keywords
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Continue!')
        continue
    print(num)

# nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range loop
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

# while loop
x = 0

while x < 10:
    print(x)
    x += 1

while True:
    if x == 12:
        break
    print(x)
    x += 1