#prompting user to input option between rock, paper, scissors
#any other option is given "Incorrect input"
#learning application of if, elif, else


first = input('First move: ')
second = input('Second move: ')

if first == 'rock' and second == 'rock':
	print('Tied game')

elif first == 'rock' and second == 'paper':
	print('second player wins')

elif first == 'rock' and second == 'scissors':
	print('first player wins')

elif first == 'paper' and second == 'paper':
	print('Tied game')

elif first == 'paper' and second == 'scissors':
	print('Second player wins')

elif first == 'paper' and second == 'rock':
	print('First player wins')

elif first == 'scissors' and second == 'scissors':
	print('Tied game')

elif first == 'scissors' and second == 'paper':
	print('First player wins')

elif first == 'scissors' and second == 'rock':
	print('Second player wins')

else:
	print('Incorrect input. Try again')
