# Author: Bintang Fajarianto
# Date: May 9 2024

def findMergeNode(head1, head2):
    while head1:
        current = head2
        while current:
            if head1 == current:
                return head1.data
            current = current.next
        head1 = head1.next