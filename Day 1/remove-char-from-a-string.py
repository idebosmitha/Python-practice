s1 = input("Enter a string : ")
s2 = input("Enter yet another string : ")

s = ''
st2 = set(s2)

for c in s1:
	if c not in st2:
		s += c

print(s)
