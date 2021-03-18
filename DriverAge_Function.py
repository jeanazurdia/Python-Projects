#Learning to create new functions- check age.

def checkDriverAge(age):        #creating a new function that can be called later
	age = input("What is your age?: ")
	if int(age) < 18:             #creating user input into integer, in order to compare it to other integer (18)
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
		print("Powering On. Enjoy the ride!");
	elif int(age) == 18:          #could've used 'else' instead of another 'elif'?
		print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()        #calling the function when needed, starting user input
