from pprint import pprint
import glob
def concat_nlu(files, out):
	intents = {}
	for fic in files: 
		streamin = open(fic,encoding="utf-8")
		current = ""
		for line in streamin.readlines() : 
			if '## intent' in line : 
				current = line
				if line not in intents : 
					intents.update({line:[]})
			else : 
				if len(line)> 1:
					intents[current].append(line)
	return intents
if __name__ == '__main__':
	
	files = ['trainpmc/data/nlu.md','testpmc/data/nlu.md','evalpmc/data/nlu.md']
	out = open('nlu.md','w', encoding='utf-8')
	intents = concat_nlu(files,out)
	for elem in intents : 
		out.write('\n'+elem)
		for intent in intents[elem]:
			out.write(intent)