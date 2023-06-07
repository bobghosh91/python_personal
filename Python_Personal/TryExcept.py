print('How many cats you want:')
numCat = int(input())
# try:
#     if int(numCat)>= 4:
#         print('Thats a lot of cat')
#     elif int(numCat)< 0:
#         print('you lying')
#     else:
#         print('Thats not many')
#
# except:
#     print('Please enter a numerical value')

# finally:
#     print("always executed")

match numCat:
    case 4:
        print("thats a lot of cat")
    case 0:
        print("thas ok amount of cat")
    case _:
        print('not many')
