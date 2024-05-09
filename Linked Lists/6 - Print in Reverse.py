# Author: Bintang Fajarianto
# Date: May 9 2024

def reversePrint(head):
    if head is not None:
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
            
        for el in arr[::-1]:
            print(el)