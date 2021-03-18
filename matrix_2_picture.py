#turning the 1s into *, and 0 into blanks

matrix = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

for i in matrix:            #for row in matrix
	for j in i:               #for cell in row
		if j == 0:              #if cell equals 0
			print(" ", end = "")  #make it blank "". The end="" section stops print from creating a new line after every cell
		else:
			print('*', end = "")  #if it's anything else (not zero), then make it *
	print('')                 #this last print is within first loop (outside of second), so the when we finish the entire row, we print nothing, but 
                            #the "end" on print(,end), which we left blank/no arguement, allows for a new line to be added after every row
