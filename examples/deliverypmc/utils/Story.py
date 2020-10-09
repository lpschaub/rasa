from utils import get_convs
from Components import Intent
from pprint import pprint

class Story(object):
    def __init__(self, lines, symbol='*'):
        self.intents = []
        self.slots = []
        self.actions = []
        self.subdial = {}
        self.symbol = symbol
        self.lines = lines

    def getintents(self):
        current = ""
        for line in self.lines:
            # print(line)

            intent = Intent(line, self.symbol)
            if intent.is_intent:

                self.intents.append(intent.intent)
                current = intent.intent

            else:
                if len(line) > 1:
                    line = line.rstrip()
                    if 'slot' in line:
                        self.slots.append(line)
                    else:
                        self.actions.append(line)
                    if current not in self.subdial:
                        # print(current)
                        self.subdial[current] = [line]
                    else:
                        self.subdial[current].append(line)


if __name__ == '__main__':
    file = open('../data/stories.md')
    convs = get_convs(file)
    print(len(convs))
    stories = [Story(elem) for elem in convs]
    print(stories[0])
    first = stories[0]
    print(first.lines)
    stories[0].getintents()
    print(stories[0].subdial)
    # pprint(stories[0].subdial)
