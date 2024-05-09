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
    
def mergeLists(head1, head2):
    head = SinglyLinkedListNode(None)
    while head1 and head2:
        if (head1.data < head2.data):
            head = insertNodeAtTail(head, head1.data)
            head1 = head1.next
        else:
            head = insertNodeAtTail(head, head2.data)
            head2 = head2.next
    
    tail = head
    while tail.next is not None:
        tail = tail.next
        
    # Merge the rest
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2
    
    return head.next