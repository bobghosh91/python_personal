str = 'aaabashfvjglwvbasdbclahsVshvcladv  HXla hvcbywqevbfq2eyvfh ajdvc had bb'

seenchar = set()
outputString = ''

for char in str:

    if char not in seenchar:
        seenchar.add(char)
        outputString += char

print(outputString)