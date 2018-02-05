# ctrl+c will kill the program if you're stuck in an infinite loop
#go to search, file extensions, uncheck hide known file types
#can escape a character by putting a \ in front of it, if you want to put a slash in your string type \\ so you escape the escape

## if you use 2='s, it checks if something is true instead of setting something equal to something, ex. x==5 checks if x is 5 vs x=5 sets x to 5
print "Hello world!"
print ("Which Version works?")
#def_space_ starts a function
def avg(a, b):
	c=(a+b)/2.0 # need the 2.0 to make sure it's a float
	return c
x =avg (3,6)
return(x)