# Copyright 2019-2020 by Akio, Akio Software.
# All rights reserved.
# This file is part of the Akio Chatbot project

"""
	Ce code concerne parfum moins cher et tout un tas de processus pour formater les données ou les traiter. 
	Il peut inclure des librairies externes précisées dans le requirements.txt telles que scikit learn, tensorflow ou encore pandas 
	code utilitaire pour formater les données

"""

import sys, glob, re, os, json

DATA = '../data/'


def ano2(conversation):
    """
    Prend une conversation anonymisée en format dégueu et la transforme en format clean (un tour par ligne)
    """
    p = re.compile(r"\( ?\d+:\d+ ?\)")
    conversation = conversation.replace("\n", " ")
    turns = re.findall(p, conversation)
    for turn in turns:
        conversation = conversation.replace(turn, '\n' + turn)
        turn2 = turn.replace(" ", "")
        conversation = conversation.replace(turn, turn2)
    return conversation[1:]


def build_cands(fic, out):
    """
        Deprecated
    """

    seen = []
    for line in open(fic, encoding='utf-8').readlines():
        if line in seen:
            continue
        else:
            seen.append(line)
            out.write('1 ' + line)


def allinonefile(filedir, outfile):
    """
    Concatene tous les fichiers de conversation en un csv
    """

    ptime = '\\(\\d\\d:\\d\\d\\)'

    puser = re.compile('(?<=(%s)) ?.?\\w+\s?:' % ptime)
    x = 0
    for file in glob.glob(filedir + '*'):
        conv = open(file, encoding='utf-8').readlines()
        conv_nbr = file.split('/')[-1].split('conv')[1]
        new_conv = clean_and_concat(conv, ptime, puser)
        # print(new_conv)
        #     for line in open(file, encoding='utf-8').readlines():
    #         new_file += line.rstrip() + '; ;\n'
        outfile.write(conv_nbr + '\t' + new_conv + '\n\n')
    # outfile.close()


def getAnotated(fic, out):
    """
    Deprecated : récupère les intents du corpus dump parfummoinscher annoté
    """
    head = fic.readline()
    out.write(head)
    for line in fic.readlines():
        if line.split('\t')[8] != "":
            print(line.split('\t')[1])
            out.write(line)


def movefile(filename):
    """
    Deprecated
    """
    print(filename)
    for elem in glob.glob(DATA + "anon/*"):
        print(elem.split("anon/")[-1])
        if filename in elem.split("anon/")[-1]:
            print("it is in both")
            try:
                os.rename(DATA + "raw/" + filename, DATA + "done/" + filename)
            except FileNotFoundError:
                print("tant pis")


def add_speaker(speaking):
    """
    DEPRECATED : use Conversation instead
    """
    print(speaking)
    pat = re.compile(r'^\(\d+:\d+\) [A-Za-zéèîôâêàùöïûÉÈ]+ *:')

    if not re.match(pat, speaking) or len(re.match(pat, speaking).group(0)) < 2 or not re.match(pat, speaking).group(0)[
        0].isupper():
        print("pas de user")

        speaking = re.sub(r'(^\(\d+:\d+\) )', r'\1userX:', speaking)
        print(speaking)
    return speaking


def extract_pmc_csv(filename, clean=True):
    """
    Get conversations from dumped csv and creates 1 file per conv
    """
    fstream = open(filename, 'r', encoding='utf-8')

    head = fstream.readline()

    conversation = []
    x = 0
    y = 0
    z = 0
    p = re.compile(r'^\(\d+:\d+\)')
    continueline = re.compile(r'\"(;\d+)+')
    speaking_turn = ""
    for elem in fstream.readlines():

        if re.match(continueline, elem):
            # print("fin conv")
            continue
        elem = elem.rstrip()

        if not elem.startswith('"Chat Parfums Moins Chers'):
            if re.match(p, elem) and z > 0:
                speaking_turn = speaking_turn.replace(" :", ":")
                conversation.append(speaking_turn + "\n")
                speaking_turn = elem
            # sys.exit()
            else:
                elem = elem.replace("\n", " ")
                speaking_turn += " " + elem

            z += 1
        elif x > 0:

            y += 1
            if clean:
                # print(conversation)
                speaking_turn = add_speaker(speaking_turn)
                print(type(speaking_turn))
                conversation.append(speaking_turn)
                speaking_turn = ""
                conversation = clean_conversation(conversation, y)
                # sys.exit()
                out = open(DATA + "raw/conv" + str(y), 'w', encoding='utf-8')
                out.write(''.join(conversation))
                conversation = []

        x += 1


def buildTXM(filepath):
    out = open(DATA + "CORPUSPMC/pmc.txt", 'w', encoding='utf-8')

    for fic in glob.glob(filepath + "/*"):
        conv = [elem for elem in open(fic, encoding='utf-8').readlines()]

        conv = ''.join([elem[6:] for elem in conv])

        out.write(conv)


def clean_conversation(conv, x):
    """
    Removes first turn
    """
    return conv[1:] if x > 1 else conv


def txt2csvUU(fic, out, sep='. '):
    """
    build csv for labo annotation
    """
    out.write("Date création;DOSSIER;SUJET;VERBATIM\n")
    y = 0
    for line in fic.readlines():
        y += 1
        new_line = ""
        x = 0
        empty = 0
        new_line = '28/02/2020;' + str(y) + ';pmc;"'
        for elem in line.split(sep):
            elem = elem.rstrip()
            elem = elem.replace(';', '')
            elem = elem.replace('"', "")
            elem = elem.replace("&#39", "'")
            elem = elem.replace("&#64", "@")
            elem = elem.replace("&#34 ;", "")
            elem = elem.replace("&#x1f61e ;", " :-(")
            elem = elem.replace("&#61 ;", " ")
            elem = elem.replace("  ", " ")

            if "span" not in elem and "RGB" not in elem:
                empty += 1
                x += 1
                new_line += str(x) + elem + ' '
            else:
                pass
            # continue
        new_line = new_line[:-1] + '"\n'
        if empty == 0:
            continue
        # out.write()
        # while x > 1 :
        # 	out.write('\t<ENTRER INTENTION ICI>')
        # 	x -= 1

        out.write(new_line)


def setAnnotations(fic, annots, out):
    annots = annots.read().split('\n')
    x = 0
    print(len(annots))
    for line in fic.readlines():
        line = line.rstrip()

        line += '\t' + annots[x] + '\n'

        out.write(line)

        x += 1

        if x == len(annots):
            break


def equalize(fic1, fic2, out):
    for i in range(len(fic1)):

        elems = fic1[i].split('\t')

        if not elems[3].startswith(' 1') and not elems[3].startswith('1'):
            print(elems[3])
            print(elems[1])


def get_treated_convs(parsed_json):
    return [key for key in parsed_json]


def clean_and_concat(conv, ptime, puser, final_conv="",user="", sequence="",first = 0, clean=True, concat=True ):
    if not conv:
        return final_conv
    else:
        turn = conv[0].rstrip()
        time = re.search(ptime, turn)
        try:
            time = time.group(0)
        except AttributeError:
            time = '(00:00)'
        this_user = re.search(puser, turn)
        try:
            this_user = this_user.group(0)
        except AttributeError:
            this_user = "_unk_"
        turn = turn.replace(time, '')
        turn = turn.replace(this_user, '')

        if not clean:
            turn = conv[0].rstrip()
        if concat:
            if this_user == user or first == 0:
                sequence += turn
            else:
                final_conv += sequence + '\n'
                sequence = turn
        else:
            final_conv += turn + '\n'
        return clean_and_concat(conv[1:], ptime, puser, final_conv, this_user, sequence,first + 1)

def getIntents(parsedcsv) :
    intents = {}
    pattern = re.compile(r'\d+$')
    for line in parsedcsv :
        if re.match(pattern,line[0]) :
            print(line[0])


def parsecsv(csv):
    convs = []
    conv = {}
    for line in csv[1:] :
        if line == '\n' :
            



if __name__ == '__main__':

    test = open("../input/50testfold.csv", 'w', encoding='utf-8')

    # allinonefile(testfold, testout)
    # allinonefile(evalfold, evalout)

    """
    # creating test and eval convs dirs from already treated data
    keys = get_treated_convs(json.load(open("../input/entitiesintents_dialogues1-100.json")))
    print(keys)
    dir = "../input/clean/"

    os.mkdir(testfold)
    os.mkdir(evalfold)
    for i in range(100):
        for conv in glob.glob(f'{dir}*'):
            if conv.split('/')[-1] not in keys and not os.path.isfile(
                    testfold + conv.split('/')[-1]) and not os.path.isfile(evalfold + conv.split('/')[-1]):
                print(conv)
                if i < 50:
                    os.system(f"cp {conv} {testfold}")
                else:
                    os.system(f"cp {conv} {evalfold}")
                break
    """
    # norm = open(DATA+'user_intentions_norm.txt')
    # out2 = open(DATA+'CSVDeSortie/colognenorm1000_annots.csv','w',encoding='utf-8')
    # pseudo = open(DATA + 'user_intentions_pseudo.txt')
    # out1 = open(DATA + 'CSVDeSortie/colognepseudo1000_annots.csv', 'w', encoding='utf-8')
    # txt2csvUU(norm,out2)
    # txt2csvUU(pseudo, out1)
    # fic1 = open(DATA+'cologneannotated.csv').readlines()
    # fic2 = open(DATA+'CSVDeSortie/colognepseudo1000_annots.csv').readlines()

    # outfinal = open(DATA+'pseudo1000.csv','w',encoding='utf-8')
    # equalize(fic1,fic2,outfinal)
    # outstream = open(DATA+'colognetrain.txt','w',encoding='utf-8')
    # allinonefile(glob.glob(DATA+"fbFormat/*"),outstream)
    # cands = open(DATA+'cologne-cands.txt','w',encoding='utf-8')
    # build_cands(DATA+'cologne_candidates.txt',cands)
    # out = open(DATA+'CSVDeSortie/cologneraw1000_annots.csv','w',encoding='utf-8')
    # fic = open(DATA+'CSVDeSortie/colognerawall.csv',encoding='utf-8')
    # annots = open(DATA+'annots_100.txt',encoding='utf-8')
    # setAnnotations(fic,annots,out)
    # getAnotated(fic,out)
    # open(DATA+'out','w',encoding='utf-8').write(('\n'.join([elem for elem in open(fic,encoding='utf-8').read().split('\n') if '?' in elem])))
    # os.mkdir('../input/clean')
    # for file in glob.glob("../input/norm/*"):
    #     f = open(file).read()
    #     print(file.split('/')[-1])
    #     out = open('../input/clean/' + file.split('/')[-1], 'w', encoding='utf-8')
    #
    #     out.write(ano2(f))
    # ls

    # extract_pmc_csv(DAfdfdTA+'pmc_extract.csv')
    # buildTXM(DATA+"raw/")
