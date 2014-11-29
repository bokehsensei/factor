from math import sqrt, floor, ceil

def factor(N):
	'''
		returns a tuple (a,b) such that N = a*b

		Note that factor only splits N in 2 factors, whichever are closer to sqrt(N)
		If N is prime, factor(N) will therefore return (1,N).

		Space cost: O(1).
		Time cost: worst case (when N is prime) is O(2^n) where n is N's length in bits.

		for example:
			factor(8) => (2,4)
			factor(39) => (3,13)
			factor(257) => (1,257) 257 is prime
	'''
	estimate = sqrt(N)
	a = floor(estimate)
	b = ceil(estimate)
	ab = a*b
	while True:
		delta = N - ab
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

def all_factors(N):
	'''
		returns a dictionary of prime factors in n with their respective exponents
		example:
			all_factors( 51 ) => { 3: 1, 17: 1 }

		Costs:

		Space: O(1)
		Time: worst case (prime) is O(2^n) where n is the bit length of the input.
	'''
	factors = {}
	stack = [N]
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
	
