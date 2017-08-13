import itertools

f = open('similar-destinations.txt', 'r')

keydict = {}
tagsdict = []
tagGroupsQt = 0

i = 0
while True:

    try:    
        line = f.readline()

        if not i:
            tagGroupsQt = int(line)
            cities = {}
            tags = {}
            i = 1
            continue

        splitedline = line.split(':')

        tags = sorted(splitedline[1].replace('\n', '').split(','))

        cities[splitedline[0]] = tags

        for tag in tags:
            keydict[tag] = 1
    except:
        break
keydict = set(keydict)


def all_subsets(ss, mintag):
  return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(mintag, len(ss)+1)))


all_s = all_subsets(keydict, tagGroupsQt)

keylist = {}
for x in all_s:
    for city in cities:
        if set(x).issubset(cities[city]):
            key = ''.join([i + " " for i in x])

            if keylist.has_key(key):
                if not city in keylist[key]:
                    keylist[key].append(city) 
            else:
                keylist[key] = [city]


resultdict = {}
for item in keylist:
    if len((keylist[item])) == 1:
        continue

    key = ''.join([i + "," for i in keylist[item]])[:-1]

    if resultdict.has_key(key):
        words = item.split()
        b = resultdict[key]

        for word in words:
            if word not in b:
                resultdict[key].append(word)
    else:
        resultdict[key] = item.split()


resultdict = [(r.split(","), resultdict[r]) for r in resultdict]

for result in resultdict:
    result[0].sort()
    result[1].sort()

def sortkey(comp1, comp2):
    #print comp1[1], comp2[1]
    if len(comp1[1]) > len(comp2[1]):
        return -1
    elif len(comp1[1]) == len(comp2[1]):
        if ''.join(comp1[0]) < ''.join(comp2[0]):
            return -1
        else:            
            return 1
    else:
        return 1

resultdict = sorted(resultdict, cmp=sortkey)


for x in resultdict:
    print ','.join(x[0]) + ":" + ','.join(x[1]) 

