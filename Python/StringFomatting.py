user_input = input("Enter your name")
message = "Hello %s" % user_input  #this was supported in older Py version
message = f"Hello {user_input}"  #latest chnages after v3.6

print(message)

#String formatting multiple inputs
name = input("Enter your name")
surname = input("Enter your surname ")

message2 = "Hello %s %s" % (name, surname) #multiple ways to formatting
message3 = f"Hello {name}{surname}"

print(message2)
print(message3)