x = 0.0

for i in range(10):
	x = x + 0.2
if x == 2.0:
	print x, ' = 2.0'
else:
	print x, ' is not 2.0'

#floating point fix
if abs(2.0 - x) < .00001:
	print x, ' is 2.0'
