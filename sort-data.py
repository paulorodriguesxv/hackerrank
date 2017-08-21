"""
https://www.hackerrank.com/challenges/python-sort-sort?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""

n, m = [int(x) for x in input().split()]

class DataRow():    
    def __init__(self, data, orderby):
        self.data = data
        self.order = orderby
        
    def __repr__(self):
        return ' '.join([str(x) for x in self.data])
       
    def getOrder(self):
        return self.data[self.order]
    
rows = []
for x in range(n):
    o = DataRow([int(m) for m in input().split()], 0)
    rows.append(o)

k = int(input().strip())
        
for row in rows:
    row.order = k
    
    
rows.sort(key= lambda x: x.getOrder())      
        
print(*filter(None, rows), sep="\n")    