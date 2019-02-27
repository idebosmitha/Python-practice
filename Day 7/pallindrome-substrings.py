s1 = input('Enter the string: ')
n = int(input('Enter a number: '))

def isPalin(s1):
	return s1[::-1] == s1

for i in range(0, len(s1) - n + 1):
	if(isPalin(s1[i:i+n])):
		print(s1[i:i+n])
