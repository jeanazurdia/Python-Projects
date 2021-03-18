#Creating a function to find the highest even number in a list provided
#the list can be created before, or created during the function callout (line 11)

def highest_even(list): #new function created, can be called elsewhere/anytime without having to code it again
	evens = []            #creating an empty list to store 'result'
	for x in list:        #for cell in list
		if x % 2 == 0:      #if cell valuem divided by 0, has no remainder, then the value is even
			evens.append(x)   #adding all the even numbers to the empty list ('evens')
	return max(evens)     #out of the 'evens' list, return the largest number

print(highest_even([1,2,3,4,8,11]))   #example of the function call w/list input in the same line
