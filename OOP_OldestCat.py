#Learning to use Object Oriented Programming- setting classes, and instantiating objects

class Cat:
	def __init__(self, name, age):    #using self to instintiate class, with name and age parameters
		self.name = name
		self.age = age

cat1 = Cat(MrWhiskers,3)            #instintiating objects, using Cat class, giving them names and ages
cat2 = Cat(Mittens,2)
cat3 = Cat(Bibi, 6)

def oldest(*args):                  #new method for oldest value, using *args to remove limit of arguements that could be called     
	return max(args)                  #given the inputs/args, return the max/highest value. The value, as age, will be defined below by 

print( f' The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old')    #using oldest method, taking age parameter of objects, returning max age value
