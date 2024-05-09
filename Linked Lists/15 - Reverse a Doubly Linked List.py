# Author: Bintang Fajarianto
# Date: May 9 2024

def reverse(head):
    c_prev = None
    
    current = head
    while current is not None:
        c_next = current.next
        current.next = c_prev
        c_prev = current
        current = c_next

    head = c_prev
    return head