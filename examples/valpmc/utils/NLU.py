import re
from pprint import pprint


class NLU(object):
    def __init__(self, lines, nlu={}):
        self.intents = []
        self.example = []
        self.entities = []
        self.nlu = nlu
        self.lines = lines

    def getIntents(self):
        current = ""
        for line in self.lines:

            int = Intent(line)
            if int.is_intent:

                self.intents.append(int.intent)
                current = int.intent

            else:
                if len(line) > 1:
                    line = line.rstrip()
                    self.example.append(line)
                    if current not in self.nlu:
                        print(current)
                        self.nlu[current] = [line]
                    else:
                        self.nlu[current].append(line)

    def writeNlu(self, out):
        for key in self.nlu:
            # print(key)
            out.write(key + '\n')
            out.write('\n'.join([elem for elem in self.nlu[key]])+'\n\n')
        out.close()


class Intent(object):
    def __init__(self, line):
        self.intent = ''
        self.name = ''
        self.is_intent = False
        if '##' in line:
            self.is_intent = True
            self.intent = line.rstrip()
            self.name = self.intent.split('## ')[1]


class Entity(object):
    def __init__(self, line):
        pattern = re.compile(r"\[\w+\]\(\w+\)]")
        self.entities = {}
        entities = re.findall(pattern, line)
        for elem in entities:
            item = elem.split('](')
            key = item[1].replace(')', '')
            value = item[0].replace('[', '')
            if key not in self.entities:
                self.entities[key] = [value]
            else:
                self.entities[key].append(value)

def removeDouble(old, new) : 
    new_l = []
    for line in old.readlines() : 
        if line not in new_l : 
            new_l.append(line)
    for line in new_l : 
        new.write(line)

if __name__ == '__main__':
    old = open('../data/nlu.md',encoding='utf-8')
    new = open('../data/new_nlu.md','w',encoding='utf-8')
    removeDouble(old, new)
    # train = NLU(open('../data/oldnlu.md', encoding='utf-8').readlines())
    # train.getIntents()
    # print(len(train.nlu))

    # evale = NLU(open("../data/nlutest.md", encoding='utf-8').readlines(), train.nlu)
    # # pprint(evale.nlu)
    # print(len(evale.nlu))
    # evale.getIntents()
    # allnlu = open("../data/nlu.md", 'w', encoding='utf-8')
    # evale.writeNlu(allnlu)
