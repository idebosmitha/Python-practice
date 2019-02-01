vowels = set('aeiouAEIOU')
s = input('Enter a string: ')

sum_ = 0
for vowel in vowels:
	sum_ += s.count(vowel)

print(sum_)

sum_ = 0
for c in s:
	if c in vowels:
		sum_ += 1

print(sum_)
