# Author: Bintang Fajarianto
# Date: May 9 2024

def has_cycle(head):
    is_cycle = False
        
    s = set()
    while head:
        if head in s:
            is_cycle = True
            break
        s.add(head)
        head = head.next
        
    return is_cycle