# Author: Bintang Fajarianto
# Date: May 9 2024

def deleteNode(head, position):
    if position == 0:
        return head.next
    else:
        current = head
        for _ in range(position - 1):
            current = current.next
        
        current.next = (current.next).next
        return head