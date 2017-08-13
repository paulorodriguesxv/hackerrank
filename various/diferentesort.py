"""
Given a list/array of names(String) sort them such that each name is followed by a name which starts with the last character of the previous name. 
# input 
[ 
Luis 
Hector 
Selena 
Emmanuel 
Amish 
] 

# output: 
[ 
Emmanuel 
Luis 
Selena 
Amish 
Hector 
]
"""

names = ["Luis", "Hector", "Selena", "Emmanuel", "Amish"]
#names = ["Raymond", "Nora", "Daniel", "Louie", "Peter", "Esteban"]


firsts = { x[0].lower():x for x in names }
lasts = { x[-1].lower():x for x in names }

start = list(set(firsts.keys()) - set(lasts.keys()))[0]

result = []

for index in xrange(len(names)):
    if not index:
        result.append(firsts[start])
        last = firsts[start][-1]
        continue

    result.append(firsts[last])
    last = firsts[last][-1]

print result