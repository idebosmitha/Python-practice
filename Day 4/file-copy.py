with open('file.txt', 'r') as f:
	with open('copied-file.txt', 'w') as fc:
		fc.write(f.read())

