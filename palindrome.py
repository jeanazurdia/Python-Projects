#learning palindromes through string slicing, reversing the 'user input' by stating: [start,stop,stepover]
#by placing stepover as -1, it will start working from the end, to the beginning
#thus by taking the user input (ex. RATSTAR), and starting from end to beginning, and comparing, one can check if it's a palindrome

user_input = input('Enter a word: ')

if user_input == user_input[::-1]:
	print("YAY CHAMP, you entered a palindrome")
else:
	print("no sir, no palindrome for you. Now GIT!")
