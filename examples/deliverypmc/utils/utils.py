import re


def get_convs(file, convs=[]):
    current = ""
    story = []
    x = 0
    for line in file:
        print(line)

        if 'story' in line and x > 0:
            convs.append(story)
            story = []

        else:
            if len(line) > 1:
                line = line.rstrip()
                story.append(line)
        x += 1
    return convs


if __name__ == '__main__':
    file = open('../all-data/stories.md')
    convs = get_convs(file)

    out = open("../input/done.txt", 'w')
    out.write('\n'.join(convs))
