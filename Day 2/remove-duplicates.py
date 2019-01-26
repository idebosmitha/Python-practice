s = input("Enter a string: ")

string_set = set()
s2 = ''

for c in s:
	if c not in string_set:
		string_set.add(c)
		s2 += c

print(s2)
