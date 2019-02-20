# s = input("Enter a string: ")
s = 'aabababacccccc'

# 1: WRITING ALL THE CODE
freq = dict()

for c in s:
	if c in freq:
		freq[c] += 1
	else:
		freq[c] = 1

	# freq[c] = freq.get(c, 0) + 1
print(freq)


# 2: WRITING A BIT LESS CODE
freq = dict()
chars = set(s)
for c in chars:
	freq[c] = s.count(c)
print(freq)


# 3: WRITING EVEN LESS CODE
freq = {c:s.count(c) for c in set(s)}
print(freq)


# 4: USING INBUILT SHIT XD
from collections import Counter

freq = Counter(s)
print(freq)

max1, max2 = s[0], s[0]
for c in freq:
	if freq[c] > freq[max1]:
		max2 = max1
		max1 = c
	elif freq[c] > freq[max2] and freq[max1] != freq[max2]:
		max2 = c

print(max2)


items = list(freq.items())
print(items)

items.sort(key=lambda t: t[1], reverse=True)
print(items)
