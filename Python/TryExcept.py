print('How many cats you want:')
numCat = input()
try:
    if int(numCat)>= 4:
        print('Thats a lot of cat')
    elif int(numCat)< 0:
        print('you lying')
    else:
        print('Thats not many')

except:
    print('Please enter a numerical value')
