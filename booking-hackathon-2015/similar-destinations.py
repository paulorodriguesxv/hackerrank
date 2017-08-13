import itertools

f = open('similar-destinations.txt', 'r')

keydict = {}
tagsdict = []

def initialize():
    for i, line in enumerate(f.xreadlines()):

        if not i:
            tagGroupsQt = int(line)
            cities = {}
            tags = {}
            continue

        splitedline = line.split(':')

        tags = sorted(splitedline[1].replace('\n', '').split(','))

        cities[splitedline[0]] = tags

        for tag in tags:
            keydict[tag] = 1

    return set(keydict), tagGroupsQt


def all_subsets(ss, mintag):
  return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(mintag, len(ss)+1)))


keydict, tagsdict = initialize()

print keydict
#all_s = all_subsets(set(cities), tagGroupsQt)

