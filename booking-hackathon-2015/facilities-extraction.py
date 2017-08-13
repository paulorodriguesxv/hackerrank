import re

f = file('facilities-extraction.txt', 'r')

numOfWords = int(f.readline())
words = [f.readline().replace('\n', '') for x in xrange(numOfWords)]

partnerDesc = f.readline()

extraction = [w for w in words if re.search(w, partnerDesc, re.IGNORECASE) != None]

print '\n'.join(sorted(extraction))