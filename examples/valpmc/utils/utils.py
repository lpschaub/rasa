import re 
def get_convs(file, convs = []) : 
	p = re.compile(r"\d+")
	for line in file.readlines() : 
		if '##' in line :
			line = line.lower() 
			if 'story' in line : 
				num = line.split('story')[1]
				# print(num)
				res = re.findall(p, num)
				if res : 
					# print(res[0])
					if res[0] not in convs : 
						convs.append(res[0])
	return convs

if __name__ == '__main__':
	file = open('../data/stories.md')
	convs = get_convs(file)

	out = open("../input/done.txt",'w')
	out.write('\n'.join(convs))