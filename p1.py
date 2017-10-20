import re


def find_urls(x):
	x = re.findall('(^https*:\S+\.\S\S+)', x)
	print(x)


find_urls('http://bbc.co.k.tnt.lll')

#x = re.findall('^http:|https:\S+\.\S{2,}', x)