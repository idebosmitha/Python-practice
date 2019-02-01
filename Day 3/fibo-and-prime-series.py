primes = [2]


def is_prime(x):
	i = 0
	while primes[i] <= x//2:
		if x % primes[i] == 0:
			return False
		i += 1
	return True


def generate_prime():
	n = primes[-1] + 1
	while True:
		if is_prime(n):
			primes.append(n)
			return
		n += 1


n = int(input("Enter the number of terms - "))

a, b = 1, 1
for i in range(n):
	if(i % 2 == 0):
		print(a)
		a, b = b, a + b
	else:
		generate_prime()
		print(primes[-2])

