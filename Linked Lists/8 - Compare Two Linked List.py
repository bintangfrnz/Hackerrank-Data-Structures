# Author: Bintang Fajarianto
# Date: May 9 2024

def compare_lists(head1, head2):
    is_equal = True
    while head1 and head2 and is_equal:
        if head1.data != head2.data:
            is_equal = False
        
        head1 = head1.next
        head2 = head2.next
    
    is_equal = head1 is None and head2 is None
    return is_equal