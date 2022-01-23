'''
LEGB
Local, Enclosing, Global, Built-in -> Python looks up in this order
'''

x = 'global x'

def test():
    y = 'local y'
    # print(y)
    print(x)

test()
# print(y) # throws error
print(x) # prints global x

def test():
    x = 'local x'
    print(x)

test()
print(x)

# setting global var in a local scope
def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)

# passing var as function param
def test(z):
    print(z)

test('local z')
# print z # throws error

# using builtin functions
import builtins

print(dir(builtins))

# enclosing functions scope
def outer():
    x = 'outer x'
    
    def inner(): # doesn't change outer x
        x = 'inner x'
        print(x)

    def inner2(): # changes outer x
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    inner2()
    print(x)

outer()
print(x)
