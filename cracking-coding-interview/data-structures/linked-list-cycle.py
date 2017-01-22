"""
    HackerRank 
    Linked Lists: Detect a Cycle
    https://www.hackerrank.com/challenges/ctci-linked-list-cycle


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

def has_cycle(head):
    slow = head
    fast = head
    
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return False
    
    slow = head
    while (slow != fast):
        slow = slow.next
        fast = fast.next

    return fast == slow