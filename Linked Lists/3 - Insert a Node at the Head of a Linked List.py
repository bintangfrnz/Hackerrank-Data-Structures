# Author: Bintang Fajarianto
# Date: May 9 2024

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
def insertNodeAtHead(head, data):
    if (head is None):
        head = SinglyLinkedListNode(data)
        return head
    else:
        current = head
        head = SinglyLinkedListNode(data)
        head.next = current
        return head