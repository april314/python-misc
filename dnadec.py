#reads contracted dna-line from file and decodes it
#encoding in file dnaenc.py
with open('dataset_3363_2.txt', 'r') as inf, open('outp.txt', 'w') as ouf:
	line = inf.readline().strip()
	letter = ""
	for i in range(len(line)):
		if line[i].isalpha():
			letter = line[i]
		elif line[i].isdigit():
			if line[(i+1)%len(line)].isalpha():
				letter *= int(line[i])
			elif line[i+1].isdigit():
				letter *= (10*int(line[i])+int(line[(i+1)%len(line)]))
				i += 1
			ouf.write(letter)
	ouf.write('\n')
