# Author: Bintang Fajarianto
# Date: May 9 2024

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
def reverse(head):
    if head is not None:
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
        
        head = SinglyLinkedListNode(arr[-1])
        current = head
        for el in arr[-2::-1]:
            next = SinglyLinkedListNode(el)
            current.next = next
            current = current.next
        
        return head