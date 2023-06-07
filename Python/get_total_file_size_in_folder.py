import os

totalsize = 0

for filename in os.listdir('C:\\Users\\bisha\\Desktop\\Bob\\Python'):
    if not os.path.isfile(os.path.join('C:\\Users\\bisha\\Desktop\\Bob\\Python' , filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users\\bisha\\Desktop\\Bob\\Python' , filename))

print(totalsize)