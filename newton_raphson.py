# x**2 - 1234560

num = 1234560.0
epsilon = 0.01
guess = 1000
counter = 0

while abs(guess**2 - num) >= epsilon:

	guess = guess - (((guess**2) - num)/(2*guess))
	counter += 1 

print guess
print counter
