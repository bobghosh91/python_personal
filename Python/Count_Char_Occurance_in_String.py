import pprint
message = 'it was a bright cold day in April, and the clock was striking thirteen'
count = {}  # dictionary r appears 12 times

for character in message:
    count.setdefault(character, 0)  #setting the value of key character as 0
    count[character] = count[character] + 1

print(count) 
pprint.pprint(count) #pretty print