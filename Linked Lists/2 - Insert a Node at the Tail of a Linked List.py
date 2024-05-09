# Author: Bintang Fajarianto
# Date: May 9 2024

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head