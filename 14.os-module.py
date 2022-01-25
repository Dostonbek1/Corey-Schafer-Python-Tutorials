import os

print(dir(os)) # show all available methods of the module

print(os.getcwd()) # get current working dir
# os.chdir('') # changes dir

print(os.listdir())
os.mkdir('OS-Demo-2')
os.makedirs('test/OS-Demo-2')
print(os.listdir())

os.rmdir('OS-Demo-2')
os.removedirs('test/OS-Demo-2')
print(os.listdir())

with open('test.txt', 'w') as fp:
    pass
os.rename('test.txt', 'demo.txt')

from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
os.remove('demo.txt')

for dirpath, dirnames, filenames in os.walk(r'../'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)