import json, re, sys
from pprint import pprint


class Converter(object):

    def input_text(self):
        pass

    def nlu_converter(self):
        pass

    def stories_converter(self):
        pass

    def domain_builder(self):
        pass


class PMCverter(Converter):

    def __init__(self, input_format='json'):
        self.format = input_format
        if self.format == 'json':
            self.json = {}
        self.intents = {}
        self.stories = {}
        self.slots = []
        self.actions = ['action_Perform_action', 'action_Search_order', 'action_Look_for_customer file',
                        'action_Reset_working_memory']

    def json_parse(self, json_data):
        json_stream = open(json_data, encoding='utf-8')
        self.json = (json.load(json_stream))
        return [self.json[dialog] for dialog in self.json]

    def entity_extractor(self):
        pass

    def data_augmentation(self):
        pass

    def post_treatment_intent(self, intent_example):

        while intent_example[0].isdigit():
            intent_example = intent_example[1:]

        p = re.compile(r'\(\d\d?:\d\d?\)')
        p2 = re.compile(r'^\s+')
        intent_example = re.sub(p, '', intent_example)
        intent_example = re.sub(p2, '', intent_example)

        return intent_example

    def slots_retriever(self):

        for dialogue in self.json:
            for turn in self.json[dialogue]:
                for slot in turn['slots']:
                    self.slots += [name.replace('_', '') for name in slot]

        self.slots = list(set(self.slots))

    def utterance_builder(self, dialogues, utterances={}, utter_list=[('', '')]):
        if not dialogues:
            self.utterances = utterances
        else:
            def one_turn_utterance(turns, small_utterance={}, intent="", utter_list=utter_list):
                if not turns:
                    return small_utterance
                else:

                    try:
                        turns[0]['sys'] = self.post_treatment_intent(turns[0]['sys'])
                    except TypeError:
                        turns[0]['sys'][0] = self.post_treatment_intent(turns[0]['sys'][0])
                    new = '_'.join(turns[0]['intent'])
                    if not new:
                        if intent:
                            new = intent
                        else:
                            new = ''
                    try:
                        seen = True
                        ut = ""
                        print(f"before : {utter_list}")
                        for tpl in utter_list:
                            # print(tpl)
                            utter = tpl[1]
                            print(f"\tutter = {utter}")
                            seen = True

                            for elem in turns[0]['policy_funcs']:
                                elem = elem.replace(' ', '')
                                print(f"\t\telem = {elem}")

                                if elem not in utter:
                                    print(f"\t\t\tthis is new : {turns[0]['policy_funcs']}")
                                    seen = False
                                else:
                                    print("\t\t\tit is in, yeah")

                            if seen:
                                print(f"\t\tseen :{'_'.join(utter)}")
                                ut = '_'.join(utter)
                                break

                        print(f"\tseen = {seen}")

                        if not seen:
                            ut = '_'.join([elem.replace(' ', '') for elem in turns[0]['policy_funcs']])
                            utter_list.append((ut, [elem.replace(' ', '') for elem in turns[0]['policy_funcs']]))

                        if new + '_' + ut not in small_utterance:

                            small_utterance.update({new + '_' + ut: [turns[0]['sys']]})
                        else:
                            small_utterance[new + '_' + ut].append(turns[0]['sys'])
                        policy = new + '_' + ut
                        turns[0]['policy_funcs'] = [elem for elem in policy.split('_') if
                                                    elem]
                    except KeyError:
                        print("ERROR")
                        pass
                    print(f"after : {utter_list}")
                    return one_turn_utterance(turns[1:], small_utterance, new, utter_list)

            one_turn_utterance(dialogues[0], utterances)
            return self.utterance_builder(dialogues[1:], utterances)

    def get_attributes(self, dialogues, attribute, entities=[]):
        if not dialogues:
            return list(set([entity for entity in entities if entity != "''"]))
        else:
            def one_turn_intent(turns, attribute, entities=[]):
                if not turns:
                    return list(set(entities))
                else:
                    # print(turns[0][attribute])

                    entities += [k for dic in turns[0][attribute] for k in dic]
                    # print(entities)
                    return one_turn_intent(turns[1:], attribute, entities)

            one_turn_intent(dialogues[0], attribute, entities)
            return self.get_attributes(dialogues[1:], attribute, entities)

    def domain_builder(self, dialogues, entities, slots):

        self.slots_retriever()
        self.intents_extractor(dialogues)
        intents = self.intents
        self.entities_labelling(entities, intents)
        # pprint(dialogues)
        self.entities = self.get_attributes(dialogues, 'entities')
        self.slots = self.get_attributes(dialogues, 'slots')
        intents = [intent for intent in self.intents]
        self.utterance_builder(dialogues)
        for utterance in self.utterances:
            if utterance == '':
                for current in self.utterances[utterance]:
                    for utterance2 in self.utterances:
                        if utterance2 != '':
                            if current in self.utterances[utterance2]:
                                self.utterances[utterance].remove(current)
        # self.utterances.pop('')
        new_utter = {}
        for utterance in self.utterances:
            new_ut = []
            for ut in self.utterances[utterance]:
                new_ut.append(ut[0])
                ut[0].replace('"', "<>").replace("''", "'").replace('"', '\"')
            new_ut = list(set(new_ut))
            new_utter[utterance] = new_ut
        self.utterances = new_utter
        utterances = self.utterances
        self.utterances = self.utterance_labelling(slots, utterances)
        self.list_utterances = [utter for utter in self.utterances if utter]
        self.actions = ['action_Perform_action', 'action_Search_order', 'action_Look_for_customer_file',
                        'action_Reset_working_memory']

    def domain_writer(self, out='../domainperfume.yml'):
        out = open(out, 'w', encoding='utf-8')
        out.write('slots:\n  ')
        out.write(""":
    type: text
  """.join([slot for slot in self.slots]) + ':\n    type: text\n')
        out.write('\n\nentities:\n')
        out.write('  - ' + """
  - """.join([entity for entity in self.entities]))
        out.write('\n\nintents:\n')
        out.write('  - ' + """
  - """.join([intent.replace(" ", "_") for intent in self.intents if intent]))
        out.write('\n\nresponses:\n')
        for utterance in self.utterances:

            if utterance:
                out.write(f'\n  utter_{utterance.replace(" ", "")}:\n    - text: "')
                out.write(
                    '\n    - text: \"'.join([elem.replace('"', '') + '\"' for elem in self.utterances[utterance]]))
        out.write('\n\nactions:\n- ' + '\n- '.join([action for action in self.actions]))

    def stories_converter(self, dialogues):

        self.stories_builder(dialogues)

        stories_file = open('../data/stories.md', 'wb')
        for story in self.stories:
            stories_file.write(str(story + '\n\n').encode('utf-8'))

    def stories_converter_lite(self, file):

        self.get_stories(file)

        stories_file = open('../data/stories.md', 'wb')
        for story in self.stories:
            stories_file.write(str(story + ''.join(self.stories[story])).encode('utf-8'))

    def filter_intents(self, min=5):
        for intent in list(self.intents):
            if len(self.intents[intent]) < min:
                self.intents.pop(intent)

    def filter_entities(self, min=5):
        for intent in self.intents:
            for i in range(len(self.intents[intent])):
                for elem in self.entities:
                    if elem in self.intents[intent][i] and self.entities[elem] < min:
                        self.intents[intent][i].replace(elem, "")

    def nlu_converter(self, dialogues, entities):

        self.intents_extractor(dialogues)
        intents = self.intents
        self.intents = self.entities_labelling(entities, intents)
        self.filter_intents()
        self.filter_entities()
        # pprint(dialogues)
        nlu_file = open('../data/nlu.md', 'wb')
        # pprint(self.intents)
        for intent in self.intents:
            if intent:
                # print(intent)
                nlu_file.write(f'\n## intent:{intent}\n'.encode('utf-8'))
                nlu_file.write("\n- ".join(self.intents[intent]).encode('utf-8'))

    def get_intents(self, file):
        self.entities = {}
        p = re.compile("\[[\w _]+\]\([\w]+\)")
        for line in open(file).readlines():
            if "## intent:" in line:
                if line not in self.intents:
                    current = line
                    self.intents[current] = []
            else:
                entitiy = re.findall(p, line)
                if entitiy:
                    for ent in entitiy:
                        if ent not in self.entities:
                            self.entities[ent] = 1
                        else:
                            self.entities[ent] += 1
                self.intents[current].append(line)

    def nlu_converter_lite(self, fic):

        self.get_intents(fic)
        self.filter_intents(3)
        self.filter_entities()
        # pprint(dialogues)
        nlu_file = open('../data/nlu.md', 'wb')
        # pprint(self.intents)
        for intent in self.intents:
            if intent:
                # print(intent)
                nlu_file.write(intent.encode('utf-8'))
                nlu_file.write("".join(self.intents[intent]).encode('utf-8'))

    def get_stories(self, file):
        p = re.compile(r"\{.*\}")
        intents = list(set([key.split(':')[-1].replace('\n', '') for key in list(self.intents)]))
        entits = list(set([key.split('(')[1].split(')')[0] for key in list(self.entities)]))
        for line in open(file).readlines():
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
                        if ent not in self.entities:
                            line.replace(entities, "")
                self.stories[current].append(line)
        for story in list(self.stories):
            for turn in self.stories[story]:
                if "to_be_removed" in turn:
                    self.stories.pop(story)
                    break
        print(len(self.stories))
        pprint(self.stories)

    def intents_extractor(self, dialogues, intents={}):

        if not dialogues:
            self.intents = intents
        else:
            def one_turn_intent(turns, small_intents={}):
                if not turns:
                    return small_intents
                else:
                    turns[0]['usr'] = self.post_treatment_intent(turns[0]['usr'])
                    if '+'.join(turns[0]['intent']) not in small_intents:

                        small_intents.update({'+'.join(turns[0]['intent']): [turns[0]['usr']]})
                    else:
                        small_intents['+'.join(turns[0]['intent'])].append(turns[0]['usr'])
                    return one_turn_intent(turns[1:], small_intents)

            one_turn_intent(dialogues[0], intents)
            return self.intents_extractor(dialogues[1:], intents)

            # for dialog in self.json:
            #     print(dialog)
            #     for turn in self.json[dialog]:
            #         print(turn)

    def utterance_labelling(self, entities, intents):
        """
        This is a tricky one. We need to label the verbatim so they look like rasa intent format
        input : '_Name2_ : bonjour2 _Name2_ : bonjour je passerai commande '
                  'seulement si les frais de port  sont à 0 € free '
                  'surtout pour une commande de 220 €. très cordialement. '
                  '_Name2_3 _Name2_ : _Email1_',
        output :'_Name2_ : bonjour2 _Name2_ : bonjour je passerai commande '
                  'seulement si les [frais de port](fdp) sont à [0 €](free) '
                  'surtout pour une commande de 220 €. très cordialement. '
                  '_Name2_3 _Name2_ : [_Email1_](email)',
        Challenge : tokenize with space is mandatory because if you don't, the system will consider that 220 € can be labelled
        as 22[0 €](free). So the function is more complicated than it looks
        """
        new_intents = {}

        for intent in intents:
            if intent:

                for example in intents[intent]:
                    l_example = [elem.replace(',', '') for elem in example.split()]

                    for i in range(len(l_example)):
                        for key in entities:
                            for value in entities[key]:
                                if value == l_example[i]:
                                    l_example[i] = '{' + key + '}'
                                else:
                                    l_value = value.split()

                                    if l_example[i] == l_value[0]:
                                        new_l_ex = l_example[i:]
                                        # print(new_l_ex)
                                        good = False
                                        x = 0
                                        new = ''
                                        for elem in new_l_ex:
                                            new += elem + ' '
                                            if not l_value:
                                                good = True
                                                break
                                            if elem != l_value[0]:
                                                break
                                            else:
                                                # print(f"it is still on the race : {new}")
                                                l_value = l_value[1:]
                                                x += 1
                                        if good:

                                            l_example[i] = l_example[i] = '{' + key + '}'
                                            for j in range(i + 1, i + x):
                                                l_example[j] = ""
                                            # l_example.remove(value)
                                            # print(example)
                    # print(l_example)
                    # print(len(l_example))
                    example = ' '.join(l_example).replace('  ', ' ').replace('  ', ' ')
                    # print(example)

                    if not intent in new_intents:
                        new_intents[intent] = [example]
                    else:
                        new_intents[intent].append(example)

        return new_intents

    def stories_builder(self, dialogues, stories=[], x=0):

        if not dialogues:
            self.stories = stories

        else:
            x += 1

            def one_turn_story(turns, story='## story_' + str(x), slots={}):
                if not turns:
                    return story
                else:
                    new_slots = {}
                    for slot in turns[0]['entities']:
                        s = list(slot.keys())[0]
                        if s not in slots:
                            new_slots.update({s.replace(" ", "_"): slot[s]})
                            slots.update({s.replace(" ", "_"): slot[s]})
                    str_slots = ''
                    erase = False
                    if new_slots:
                        str_slots = '{'
                        for slot in new_slots:
                            if slot == "''":
                                erase = True
                                break
                            sslot = str(slot).replace("'", '"')
                            svalue = str(new_slots[slot].replace("'", '<apostrophe>')).replace('<apostrophe>', "'")
                            str_slots += '"' + sslot + '"' + ': ' + '"' + svalue + '"' + ','

                        str_slots = str_slots[:-1] + '}'
                    if erase:
                        str_slots = ''
                    if not turns[0]['intent']:
                        turns[0]['intent'] = ['rien']
                    intent = '\n* ' + '+'.join(turns[0]['intent']) + str_slots
                    try:
                        action = 'rien du tout'
                        action = ' - utter_' + '_'.join(
                            [elem.replace(" ", "") for elem in turns[0]['policy_funcs']])
                        # while action not in self.list_utterances:
                        # print(action)
                        for elem in turns[0]['policy_funcs']:
                            elem = 'action_' + elem.replace(" ", "_")
                            if elem in self.actions:
                                action += '\n - ' + elem.replace(" ", "")
                    except KeyError:
                        action = 'action_listen'
                    turn = intent + '\n' + action
                    story += turn
                    return one_turn_story(turns[1:], story, slots)

            story = one_turn_story(dialogues[0][1:])
            stories.append(story)
            return self.stories_builder(dialogues[1:], stories, x)

    def entities_labelling(self, entities, intents):
        """
        This is a tricky one. We need to label the verbatim so they look like rasa intent format
        input : '_Name2_ : bonjour2 _Name2_ : bonjour je passerai commande '
                  'seulement si les frais de port  sont à 0 € free '
                  'surtout pour une commande de 220 €. très cordialement. '
                  '_Name2_3 _Name2_ : _Email1_',
        output :'_Name2_ : bonjour2 _Name2_ : bonjour je passerai commande '
                  'seulement si les [frais de port](fdp) sont à [0 €](free) '
                  'surtout pour une commande de 220 €. très cordialement. '
                  '_Name2_3 _Name2_ : [_Email1_](email)',
        Challenge : tokenize with space is mandatory because if you don't, the system will consider that 220 € can be labelled
        as 22[0 €](free). So the function is more complicated than it looks
        """
        new_intents = {}

        for intent in intents:
            if intent:

                for example in intents[intent]:
                    l_example = [elem.replace(',', '') for elem in example.split()]

                    for i in range(len(l_example)):
                        for key in entities:
                            for value in entities[key]:
                                if value == l_example[i]:
                                    l_example[i] = f'[{value}]({key})'
                                else:
                                    l_value = value.split()

                                    if l_example[i] == l_value[0]:
                                        new_l_ex = l_example[i:]
                                        # print(new_l_ex)
                                        good = False
                                        x = 0
                                        new = ''
                                        for elem in new_l_ex:
                                            new += elem + ' '
                                            if not l_value:
                                                good = True
                                                break
                                            if elem != l_value[0]:
                                                break
                                            else:
                                                # print(f"it is still on the race : {new}")
                                                l_value = l_value[1:]
                                                x += 1
                                        if good:

                                            l_example[i] = f'[{value}]({key})'
                                            for j in range(i + 1, i + x):
                                                l_example[j] = ""
                                            # l_example.remove(value)
                                            # print(example)
                    # print(l_example)
                    # print(len(l_example))
                    example = ' '.join(l_example).replace('  ', ' ').replace('  ', ' ')
                    # print(example)

                    if not intent in new_intents:
                        new_intents[intent] = [example]
                    else:
                        new_intents[intent].append(example)

        return new_intents


conv = PMCverter()
#
# dialogues = conv.json_parse('../input/entitiesintents_dialogues1-100.json')
#
# entities = json.load(open('../input/entities.json'), encoding='utf-8')
# slots = json.load(open('../input/slots.json'), encoding='utf-8')

intent_file = '../v0/nlu.md'
stories_file = '../v0/stories.md'
conv.nlu_converter_lite(intent_file)
conv.stories_converter_lite(stories_file)
# conv.domain_builder(dialogues, entities, slots)
# conv.domain_writer()
# conv.stories_converter(dialogues)
# conv.entities_labelling(entities)
