#Learning lists, and counters- initiating counters outside of loop at 0

midlist = [1,2,3,4,5,6,7,8,9,10,1,2,2,2,2,2,2,2]        #example of list
counter = 0

for items in midlist:       #for "x"/value in "list_name"
	counter += 1              #short notation of adding 1 everytime
print(counter)
                             #result: =18
