from pprint import pprint
import re
import yaml


class Regulator(object):
    def __init__(self):
        self.intent = {}
        self.stories = {}
        self.domain = {}

    def get_intents(self):
        pass

    def get_stories(self):
        pass

    def get_domain(self):
        pass

    def update(self):
        pass

    def reset(self):
        pass

    def filter(self):
        pass


class PMCRegulator(Regulator):
    def __init__(self, intent_file, stories_file, domain_file):
        Regulator.__init__(self)
        self.intent_file = intent_file
        self.stories_file = stories_file
        self.domain_file = domain_file

    def get_intents(self):
        self.entities = {}
        p = re.compile(r"\[[\w _]+\]\([\w]+\)")
        for line in open(self.intent_file).readlines():
            if "## intent:" in line:
                if line not in self.intent:
                    current = line
                    self.intent[current] = []
            else:
                entitiy = re.findall(p, line)

                if entitiy:
                    for ent in entitiy:
                        if ent not in self.entities:
                            self.entities[ent] = 1
                        else:
                            self.entities[ent] += 1
                self.intent[current].append(line)

    def filter_intents(self, min=3):
        for intent in list(self.intent):
            if len(self.intent[intent]) < min:
                self.intent.pop(intent)
        # print(len(list(self.intent)))

    def filter_entities(self, min=3):
        to_remove = []
        for intent in self.intent:
            for i in range(len(self.intent[intent])):
                for elem in self.entities:
                    if elem in self.intent[intent][i] and self.entities[elem] < min:
                        self.intent[intent][i].replace(elem, "")
                        to_remove.append(elem)
        for elem in list(self.entities):
            if self.entities[elem] < min:
                self.entities.pop(elem)

    def get_domain(self):
        self.domain = yaml.load(open(self.domain_file))

    def domain_writer(self, out='../domainperfume.yml'):
        intents = list(set([key.split(':')[-1].replace('\n', '') for key in list(self.intent)]))
        entits = list(set([key.split('(')[1].split(')')[0]for key in list(self.entities)]))
        out = open(out, 'w', encoding='utf-8')
        out.write('slots:\n  ')
        out.write(""":
       type: text
     """.join([slot for slot in self.domain["slots"]]) + ':\n    type: text\n')
        out.write('\n\nentities:\n')
        out.write('  - ' + """
  - """.join([entity for entity in entits]))
        out.write('\n\nintents:\n')
        out.write('  - ' + """
  - """.join([intent.replace(" ", "_") for intent in intents if intent]))
        out.write('\n\nresponses:\n')
        # for utterance in self.utterances:
        #
        #     if utterance:
        #         out.write(f'\n  utter_{utterance.replace(" ", "")}:\n    - text: "')
        #         out.write(
        #             '\n    - text: \"'.join([elem.replace('"', '') + '\"' for elem in self.utterances[utterance]]))
        # out.write('\n\nactions:\n- ' + '\n- '.join([action for action in self.actions]))
    def update(self):

        for elem in self.domain:
            if elem == 'entities':
                print(len(self.domain[elem]))
                entities = list(set([key.split('(')[-1].replace(')', '') for key in list(self.entities)]))
                for entity in self.domain[elem]:
                    if entity not in entities:
                        self.domain[elem].remove(entity)
                print(len(self.domain[elem]))
            if elem == 'intents':
                print(len(self.domain[elem]))
                intents = list(set([key.split(':')[-1].replace('\n', '') for key in list(self.intent)]))
                for intent in self.domain[elem]:
                    if intent not in intents:
                        self.domain[elem].remove(intent)
                print(len(self.domain[elem]))
        yaml.dump(self.domain, open("../domain2.yml", 'w'))

    def get_stories(self):
        p = re.compile(r"\{.*\}")

        intents = list(set([key.split(':')[-1].replace('\n', '') for key in list(self.intent)]))
        entits = list(set([key.split('(')[1].split(')')[0]for key in list(self.entities)]))
        for line in open(self.stories_file).readlines():
            if "## story_" in line:
                if line not in self.stories:
                    current = line
                    self.stories[current] = []
            else:
                if line.startswith("*"):
                    if '{' in line:
                        intent = line.split('* ')[1].split('{')[0]
                    else:
                        intent = line.split('* ')[1].split('\n')[0]

                    if intent not in intents:
                        line = "to_be_removed"

                entities = re.findall(p, line)
                if entities:
                    # print(entities)
                    entity = [eval(entitiy) for entitiy in entities][0]
                    entities = ''.join(entities)
                    for ent in entity:
                        print(ent)
                        if ent not in self.entities:
                            line.replace(entities, "")
                self.stories[current].append(line)
        for story in list(self.stories):
            for turn in self.stories[story]:
                if "to_be_removed" in turn:
                    self.stories.pop(story)
                    break
        print(len(list(self.stories)))
    def filter_stories(self):
        pass


if __name__ == '__main__':
    Path = "../data/"
    intents = f"{Path}nlu.md"
    stories = f"{Path}stories.md"
    domain = "../old_domain.yml"
    reg = PMCRegulator(intents, stories, domain)
    reg.get_intents()
    reg.filter_intents()
    reg.filter_entities()
    reg.get_domain()
    reg.update()
    reg.domain_writer()
    reg.get_stories()
