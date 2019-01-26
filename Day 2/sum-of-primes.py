from functools import reduce


def is_prime(x):
	if x == 1:
		return False
	for i in range(2, x//2 + 1):
		if x % i == 0:
			return False
	return True


n1 = int(input('Enter the value of n1'))
n2 = int(input('Enter the value of n2'))
sum_of_primes = 0

for i in range(n1, n2 + 1):
	if is_prime(i):
		sum_of_primes += i

print(sum_of_primes)


# Do not read if you're a beginner
# And if you're not, you already know not to do this :)
print(reduce(lambda a, b: a + b, filter(is_prime, list(range(n1, n2+1)))))
