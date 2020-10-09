class Intent(object):
    def __init__(self, line, symbol):
        self.intent = ''
        self.name = ''
        self.is_intent = False
        if symbol in line:
            self.is_intent = True
            self.intent = line.rstrip()
            self.name = self.intent.split(symbol + ' ')[1]


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