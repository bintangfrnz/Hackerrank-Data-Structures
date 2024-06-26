# Author: Bintang Fajarianto
# Date: May 9 2024

def removeDuplicates(head):
    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
            
    return head