"""
    HackerRank 
    Trees: Is This a Binary Search Tree?
    https://www.hackerrank.com/challenges/ctci-is-binary-search-tree


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

def checkBST(nnode, nmin, nmax):
    
    if not nnode:
        return True
    
    if (nmin and (nnode.data <= nmin)) or (nmax and (nnode.data >= nmax)):
        return False
    
    if (not checkBST(nnode.left, nmin, nnode.data) or not checkBST(nnode.right, nnode.data, nmax)):
        return False
    
    return True
    
    
def check_binary_search_tree_(root):
    
    return checkBST(root, None, None)