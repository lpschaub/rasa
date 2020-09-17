import os, json, glob
path = "/home/tf/Documents/projets/repos/rasa/examples/perfumebot/input/"
source  = path + 'clean/'
iteration = '3/'
extract = path+iteration
os.system(f'mkdir {extract}')
current = path+'done.txt'

def extractor(fun, list_files, nbr = 20, x = 0) :
	list_convs = fun()
	# print(list_convs)
	for file in glob.glob(source+'*') : 
		
		if x == nbr : 
			break

		if file.split('/')[-1] not in list_convs :
			print(file.split('/')[-1])
			opened = open(file)
			if len(opened.readlines()) > 2 :
				os.system(f'cp {file} {extract}')
				x += 1

def listing() :

	return [dic for dic in json.load(open(out+current))]

def listing2() : 
	return ["conv"+elem.rstrip() for elem in open(current).readlines() ]

if __name__ == '__main__':
	
	extractor(listing2, path, nbr = 50)







