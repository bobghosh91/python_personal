def loopWhile():
    todos = []
    password = ''
    while True:
        inp = input("enter a value")
        todos.append(inp.capitalize())
        print(todos)
        if inp == 'break':
            break

    while password != 'pass123':
        password = input("enter a password")

#loopWhile()

#for Loop
def loopFor():
    todos = range(1,5,1)
    for item in todos:
        print(item)

#loopFor()
x = [str(i) for i in range(1,5)]
print(x)

b, c, d, e = 5,6.4, 'Great', 2 + 3j
print("{}{}".format('value is: ', b))
#print(type(e))

x= (1,3,5)
print(x.__contains__(5))

print("\u201c :bbb")
print("\"")

rng = range(1,101)
[print(i, end=' ') if i%2==0 else "continue" for i in rng]
