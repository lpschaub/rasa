import sys


def get_intentsnlu(file, out):
    nlu_intents = []
    for line in file.readlines():

        if '## intent' in line:
            line = line.split(':')
            line[1] = line[1][0].upper() + line[1][1:]
            intent = line[1].rstrip()

            if intent not in nlu_intents:
                nlu_intents.append(intent)
            line = ':'.join(line)
        out.write(line)
    return nlu_intents


def get_intentsdomain(file, out):
    nlu_domain = []
    for line in file.readlines():
        if line.startswith('-'):
            line = line[:2] + line[2].upper() + line[3:]
            intent = line[2:].strip()
            nlu_domain.append(intent)

        out.write(line)
    return nlu_domain


def get_intentsstories(file, out):
    nlu_stories = []
    for line in file.readlines():

        if line.startswith('*'):
            line = line[:2] + line[2].upper() + line[3:]
            intent = line[2:].split('{')[0].rstrip()
            nlu_stories.append(intent)
        out.write(line)
    return nlu_stories


def get_utterdomain(file, out):
    utterdomain = []
    for line in file.readlines():
        if line.startswith('-'):
            line1 = line.split('_')[0]
            line2 = line.replace(line1, '')
            line2 = line2[0] + line2[1].upper() + line2[2:]
            line = line1 + line2
            utter = line1.split('- ')[1] + line2.rstrip()
            # print(utter)
            utterdomain.append(utter)

        out.write(line)
    return utterdomain


#
def get_uttersstories(file, out):
    utterstories = []
    for line in file.readlines():

        if "utter_" in line or "action_" in line:
            line0 = "    - "

            line1 = line.replace(line0, '').split('_')[0] + '_'
            line2 = line.replace(line0, '').replace(line1, '')
            line2 = line2[0].upper() + line2[1:]
            line = line0 + line1 + line2
            utter = line1 + line2.rstrip()
            utterstories.append("- " + utter)
        out.write(line)
    return utterstories


def remove_uttersstories(file, out, l):
    for line in file.readlines():

        if "utter_" in line or "action_" in line:
            line0 = "- "
            line1 = line.replace(line0, '').split('_')[0] + '_'
            line2 = line.replace(line0, '').replace(line1, '')
            line2 = line2[0].upper() + line2[1:]
            line = line0 + line1 + line2
            utter = '- '+line1 + line2.rstrip()
            print(utter)
            print(l[0])
            if utter in l:
                out.write(line)
        else:

            out.write(line)


def check(l1, l2):
    for elem in l1:
        if elem not in l2:
            print(elem)
    print("###########################\n\nET LE CONTRAIRE###########################\n\n")
    for elem in l2:
        if elem not in l1:
            print(elem)


def get_utter():
    pass


def get_stories():
    pass


if __name__ == '__main__':
    # file = open('../data/nlu.md', encoding='utf-8')
    # out = open('../data/new_nlu.md', 'w', encoding='utf-8')
    # nlu = get_intentsnlu(file, out)
    #
    # file = open('../responses.yml', encoding='utf-8')
    # out = open('../new_res.yml', 'w', encoding='utf-8')
    # domain = get_intentsdomain(file, out, )
    #
    # file = open('../data/stories.md', encoding='utf-8')
    # out = open('../data/new_stories.md', 'w', encoding='utf-8')
    # stories = get_intentsstories(file, out)
    #
    # check(nlu, stories)

    file = open('../utter.yml', encoding='utf-8')
    out = open('../new_utter.yml', 'w', encoding='utf-8')
    # domainu = get_utterdomain(file, out)

    file = open('../data/stories.md', encoding='utf-8')
    out = open('../data/new_stories.md', 'w', encoding='utf-8')
    storiesu = get_uttersstories(file, out)
    file = open('../utter.yml', encoding='utf-8')
    out = open('../new_utter.yml', 'w', encoding='utf-8')

    remove_uttersstories(file, out, storiesu)
