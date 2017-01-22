"""
    HackerRank 
    Stacks: Balanced Brackets
    https://www.hackerrank.com/challenges/ctci-balanced-brackets


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

def is_matched(expression):
    
    pairs = {'(':')', '{':'}', '[':']'}

    stack = []
    for bracket in expression:
        if bracket in pairs:
            stack.append(bracket)
        elif stack and pairs[stack.pop()] == bracket:
            continue
        else:
            return False
        
    if not stack:
        return True
    
    return False
        

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"