# Author: Bintang Fajarianto
# Date: May 9 2024

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None
        
def sortedInsert(head, data):
    new_data = DoublyLinkedListNode(data)
    
    if head.data >= data:
        head.prev = new_data
        new_data.next = head
        return new_data
    
    current = head
    while current.next:
        if current.next.data >= data:
            # save next in temp var
            c_next = current.next
            
            current.next = new_data
            new_data.prev = current
            new_data.next = c_next
            c_next.prev = new_data
            break
        current = current.next
        
    if current.next is None:
        current.next = new_data
        new_data.prev = current
        
    return head