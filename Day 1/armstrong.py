'''
153 == 1³ + 5³ + 3³
'''

def sum_of_digits(x):
	no_of_digits = len(str(x))
	sum_ = 0
	while x > 0:
		digit = x % 10
		x //= 10
		sum_ += pow(digit, no_of_digits)
	return sum_

n = int(input('Enter a number: '))
s = sum_of_digits(n)
print(n == s)