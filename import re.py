import re
fname = input("enter: ")
fhandle = open(fname, 'r')

lis = []
for line in fhandle:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	for number in x:
		lis.append(int(number))

print(sum(lis))
