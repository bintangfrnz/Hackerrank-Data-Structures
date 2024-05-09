# Author: Bintang Fajarianto
# Date: May 9 2024

def getNode(head, positionFromTail):
    length = 0
    current = head
    while current:
        current = current.next
        length += 1
    
    idx = 0
    while idx < length - positionFromTail - 1:
        head = head.next
        idx += 1
        
    return head.data