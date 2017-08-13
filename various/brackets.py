"""
Write a function to test if the given set of brackets are balanced or not. e.g. {{}}{)([][]
"""
def isBalancedBrackets(input):

    bracketsDict = {'{':'}', '[':']', '(':')'}

    bracketsStream = [x for x in input]

    bracketsStack = []

    for bracket in bracketsStream:
        if bracket in bracketsDict.keys():
            bracketsStack.append(bracket)
        elif len(bracketsStack) and     [bracketsStack.pop()] == bracket:
            continue
        else:
            return False

    if not len(bracketsStack):
        return True

    return False

print isBalancedBrackets('({[{()}]})')
