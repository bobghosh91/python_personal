lines = 5 #how many lines of tree is required
length = lines*2 - 1  #consider the last line where number of stars are 9 which is 5*2 - 1
spaces = lines-1 #this will be how many spaces we need at start
i = 1
symbol = '+'

while i<= lines:
    print(' '*(spaces-i+1), symbol*(2*i-1))
    i += 1



#      *
#     ***
#    *****
#   *******
#  *********

def holidaybush(n):
    for i in range(n):
        print(' ' * (n - (i + 1)),'+' * (2*i+1))

holidaybush(5)