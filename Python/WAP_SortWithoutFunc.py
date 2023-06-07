list  = [56, 24, 58, 12, 10, 5, 68, 99, 1, 45]
new_list = []

while list:
    minimum = list[0]
    
    for x in list:
        if x > minimum:
            minimum = x
        
    new_list.append(minimum)
    list.remove(minimum)


print(new_list)
