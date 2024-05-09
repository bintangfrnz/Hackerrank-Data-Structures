# Author: Bintang Fajarianto
# Date: May 9 2024

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
      
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(position - 1):
        current = current.next
    
    next = current.next
    current.next = new_node
    new_node.next = next
    return head