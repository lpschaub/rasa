import glob
# from Automatization import Automatization
import os

# auto = Automatization(glob.glob('../formats/*.csv'))
# corpus = '../results/'
# # auto.getcombinations()
# # auto.preparedata()
# auto.getresults(corpus)
#

data = '../data/'
x = 0 
models = '../models'
while  os.path.isdir(f'{models}/model{x}/') :
    x += 1
new_model = f'{models}/model{x}'
os.system(f'mkdir{new_model}')
os.system(f'rasa train --config ../config_supervised.yml --data {data}-d ../domainperfume.yml --out {new_model}')


# for fic in glob.glob('../data_perfume/*') :
#     print(fic)
# # fic = '../nlus2/nlu_cologneraw1000_annots.md'
#     fic_ext = fic.split('/')[-1]
#     ficdir = fic_ext.split('.md')[0]
#     print(ficdir)
#     tts= '../train_test_split/'
#     os.system(f'mkdir {tts}')
#     os.system(f'mkdir {tts}{ficdir}')
#     # os.system(f'rasa data split nlu -u {fic} --out {tts}{ficdir}')
#     # os.system(f'rasa train nlu --config ../config_supervised.yml -u {tts}{ficdir}/training_data.md --fixed-model-name ../mods/{ficdir} --out ../mods/')
#     os.system(f'rasa test core -u {tts}{ficdir}/test_data.md --config ../config_supervised.yml  --out ../res/{ficdir} --model ../mods/{ficdir}.tar.gz')
#     # --threshold
#     # 0.75
#     # fic_ext = fic.split('/')[-1]
#     # ficdir= fic_ext.split('.')[0]
#     # print(ficdir)
#     # print(fic_ext)
#     # os.system(f'mkdir ../results2/{ficdir}')
#     # os.system(f'rasa test nlu -u {fic} --cross-validation -f 2 --config ../config_supervised.yml --out ../results2/{ficdir}')
