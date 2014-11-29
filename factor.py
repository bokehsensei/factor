from math import sqrt, floor, ceil

def factor(n):
	'''
		return a tuple (a,b) such that n = a*b

		Note that factor only splits n in 2 factors, whichever are closer to sqrt(n)

		for example:
			factor(8) => (2,4)
			factor(39) => (3,13)
			factor(257) => (1,257) 257 is prime
	'''
	estimate = sqrt(n)
	a = floor(estimate)
	b = ceil(estimate)
	ab = a*b
	while True:
		delta = n - ab
		if delta == 0:
			break
		if delta > 0:
			delta_b = max(delta//a, 1)
			b += delta_b
			ab += delta_b*a
		if delta < 0:
			delta_a = min(delta//b, -1)
			a += delta_a
			ab += delta_a*b

	
	return a,b

def all_factors(n):
	'''
		return a dictionary of prime factors in n with their respective exponents
		example:
			all_factors( 51 ) => { 3: 1, 17: 1 }
	'''
	factors = {}
	stack = [n]
	while stack:
		a,b = factor(stack.pop())
		if a == 1:
			if b in factors.keys():
				factors[b] += 1
			else:
				factors[b] = 1
		else:
			stack += (a,b)
	return factors
	
