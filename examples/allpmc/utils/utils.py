import re 

from pprint import pprint 

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


def get_stories(file): 
	stories = []
	current = []
	for line in file.readlines() : 
		if '##' in line and current : 
			stories.append(current)
			current = [line]
		else : 
			current.append(line)
	return stories

def get_elems(stories) : 
	intents = {}
	utterances = {}
	for story in stories : 
		for line in story : 
			if '*' in line : 
				if '{' in line : 
					line = line.split('{')[0]
				if line not in intents :
					intents[line] = 1 
				else:
					intents[line] += 1

			elif 'utter_' in line : 
				if line not in utterances :
					utterances[line] = 1 
				else:
					utterances[line] += 1
	return intents, utterances

def new_stories(stories,intents,utterances, out):

	for story in stories : 
		dont = False
		for line in story : 
			if '*' in line : 
				if '{' in line : 
					line = line.split('{')[0]
				if intents[line] < 3 : 
					dont = True
				

			elif 'utter_' in line : 
				if utterances[line] < 3 : 
					dont = True

		if not dont : 
			out.write(''.join(story))


def get_utter(domain) : 
	utters = []
	utter = ["    "+domain.readline()]
	for line in domain.readlines() :
		if ('utter_' in line or 'action_' in line) and utter  : 
			utters.append(utter)
			line = "    "+line
			line = line.replace(':','')
				# sys.exit()
			utter = [line]
		else : 
			utter.append(line)
	return utters

def new_domain(utterances,inp, out) : 
	print(inp[0])
	for line in inp : 
		print(line[0])
		if line[0] in utterances:
			out.write("".join(line))

# def new_nlu(intents) : 

if __name__ == '__main__':
	file = open('../data/stories.md')
	out = open('../data/new_stories.md','w')
	convs = get_stories(file)
	intents, utters = get_elems(convs)
	pprint(intents)
	pprint(utters)
	new_stories(convs,intents,utters, out)
	domain = open("../responses.yaml")
	new = open("../new_responses.yml",'w')
	domain = get_utter(domain)

	new_domain(utters, domain, new)