import re
from pprint import pprint
from utils.Components import Intent


class NLU(object):
    def __init__(self, lines, nlu={}, symbol='##'):
        self.intents = []
        self.example = []
        self.entities = []
        self.nlu = nlu
        self.lines = lines
        self.symbol = symbol

    def getintents(self):
        current = ""
        for line in self.lines:

            intent = Intent(line, self.symbol)
            if intent.is_intent:

                self.intents.append(intent.intent)
                current = intent.intent

            else:
                if len(line) > 1:
                    line = line.rstrip()
                    self.example.append(line)
                    if current not in self.nlu:
                        print(current)
                        self.nlu[current] = [line]
                    else:
                        self.nlu[current].append(line)

    def writenlu(self, out):
        for key in self.nlu:
            # print(key)
            out.write(key + '\n')
            out.write('\n'.join([elem for elem in self.nlu[key]]) + '\n\n')
        out.close()


def removedouble(old, new):
    new_l = []
    for line in old.readlines():
        if line not in new_l:
            new_l.append(line)
    for line in new_l:
        new.write(line)


if __name__ == '__main__':
    old = open('../all-data/oldnlu.md', encoding='utf-8')
    new = open('../all-data/newold_nlu.md', 'w', encoding='utf-8')
    removedouble(old, new)
    # train = NLU(open('../all-data/oldnlu.md', encoding='utf-8').readlines())
    # train.getIntents()
    # print(len(train.nlu))

    # evale = NLU(open("../all-data/new_nlu.md", encoding='utf-8').readlines(), train.nlu)
    # # pprint(evale.nlu)
    # print(len(evale.nlu))
    # evale.getIntents()
    # allnlu = open("../all-data/nlu.md", 'w', encoding='utf-8')
    # evale.writeNlu(allnlu)
