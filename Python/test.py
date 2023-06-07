"""
name='b'
while name:
    print('pleae type your name')
    name=input()
print('Thank you')

"""
# import pandas
# df = pandas.read_csv('supermarkets.csv')
# print(df)

# cl = list(range(5))
# myit = iter(cl)

# print(next(myit))
# print(next(myit))

def numpat(n):
     
    # initialising starting number
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # re assigning num
        # num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver code
n = 5
numpat(n)