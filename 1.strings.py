message = "Hello World"

message2 = """Hello world hey! 
Test"""

message3 = message.replace('World', 'Universe')

print(message[1])
print(len(message2))
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('l'))
print(message.replace('World', 'Universe'))
print(message3)

greeting = 'Hello'
name = 'Doston'

message = greeting + ', ' + name + '. Welcome!'
print(message) 

message = '{0}, {1}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
print(help(str))
print(help(str.lower))