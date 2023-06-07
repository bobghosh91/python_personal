#this is guess the number game
import random

print('Hello, what is your name')
name = input()

print('Well, '+name+', i am thinking of a number betweeen 1 to 20')
secretnumber = random.randint(1,20)

#print('DEBUG: the secret number is:'+ str(secretnumber))

for guessTaken in range(1,7):
    print ('Take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('your guess is too low')
    elif guess > secretnumber:
        print('your guess is too high')
    else:
        break # this is correct condition

if guess == secretnumber:
    print('Good job '+name+'! you guessed your number in '+str(guessTaken)+' guesses')
else:
    print('Nope the number is was thinking of is'+ str(secretnumber))

