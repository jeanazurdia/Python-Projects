#Learning while loops on a number guessing game. Also using 'break' to end loop

import random                                         #importing Random module

rando = random.randint(1,9)                           #range from 1-9
guess = 0                                             #initiate at 0

while guess != rando and guess != 'exit':             #stay on the while loop, until guess=rando, or user types exit

guess = input('Enter your guess, from 1-9, or leave by typing exit: ')
	if guess == 'exit':
		break
	guess = int(guess)
	if guess < rando:
		print('Guess is too low. Try again.\n')
	elif guess > rando:
		print('Guess is too high. Try again.\n')
	else:
		print('Choice is correct!')       #either it is higher, lower, and if neither, it is correct!
