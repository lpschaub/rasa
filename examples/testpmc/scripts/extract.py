import os, json, glob

path = '/home/schaub/Documents/Akio/TA/PMC/data/clean/norm/'
out = '/home/schaub/Documents/these/tests/repo/rasa/examples/perfumebot/input/'
iteration = '2'
extract = out+iteration
os.system(f'mkdir {extract}')
current = 'entitiesintents_dialogues1-100.json'

def extractor(fun, list_files, nbr = 20, x = 0) :
	list_convs = fun()
	print(list_convs)
	for file in glob.glob(path+'*') : 
		
		if x == nbr : 
			break

		if file.split('/')[-1] not in list_convs :
			print(file.split('/')[-1]) 
			os.system(f'cp {file} {extract}')
		x += 1

def listing() :

	return [dic for dic in json.load(open(out+current))]

if __name__ == '__main__':
	
	extractor(listing, path)







