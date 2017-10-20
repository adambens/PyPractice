import re


def find_urls(s):
	regex = r"https?:\/\/[A-Za-z0-9]{2,}(?:\.+[A-Za-z0-9]{2,})+"
	answer = re.findall(regex, s)
	print(answer)
	#parsed_urls = re.findall("http[s]?:\/\/[A-Za-z0-9]+(?:\.[A-Za-z0-9]{2,})\S+", input_string)
	#x = re.findall('(^https*:\S+\.\S\S+)', x)
	#print(parsed_urls)


find_urls('http://bbc.co.k')

#x = re.findall('^http:|https:\S+\.\S{2,}', x)