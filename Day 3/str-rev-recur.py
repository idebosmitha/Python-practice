def rev(s):
	if s == '':
		return ''
	return s[-1] + rev(s[:-1])


s = input('Enter a string: ')
print(rev(s))
