import os

print(os.path.join('folder1','folder2','file.txt'))

print(os.getcwd())

print(os.path.abspath('t.txt'))

print(os.path.relpath('C:\\Users\\bisha\\Desktop\\Bob\\Python' , 'C:\\Users\\bisha\\Desktop'))

print(os.path.exists('C:\\Users\\bisha\\Desktop\\Bob\\Python'))

os.makedirs('C:\\bob\\bobo')

#open a file
myfile = open('fruits.txt')
print(myfile.read())

for i in range(1,4):
    print(i)
