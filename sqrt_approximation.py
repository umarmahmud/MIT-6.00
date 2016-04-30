#exhaustive enumeration

x = 144
my_guess = 0.0
epsilon = .01
step = epsilon**2
counter = 0

while (abs(my_guess**2 - x)) >= epsilon and my_guess <= x:
	
	my_guess += step
	counter += 1

print str(my_guess) + ' in ' + str(counter) + ' iterations'

if (abs(my_guess**2 -x)) >= epsilon:
	print 'unacceptable'