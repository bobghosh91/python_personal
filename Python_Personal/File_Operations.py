import os

# print(os.path.join('folder1','folder2','file.txt'))
#
# print(os.getcwd())
#
# print(os.path.abspath('t.txt'))
#
# print(os.path.relpath('C:\\Users\\bisha\\Desktop\\Bob\\Python' , 'C:\\Users\\bisha\\Desktop'))
#
# print(os.path.exists('C:\\Users\\bisha\\Desktop\\Bob\\Python'))
#
# os.makedirs('C:\\bob\\bobo')

#open a file
# myfile = open('fruits.txt')
# print(myfile.read())
# myfile = None
# myfile.close()

# with open('fruits.txt', 'r') as myFile: # read mode
# with open('fruits.txt', 'w') as myFile: # write mode
# with open('fruits.txt', 'a+') as myFile:
#     myFile.write('\nokra')
#     myFile.seek(0)
#     content = myFile.read()
#     myFile = None
#
# print(content)


#print Line by line using readLine method
myfile = open('fruits.txt')
myline = myfile.readline()

while myline != "":
    print(myline)
    myline = myfile.readline()
myfile.close()
myFile = None

