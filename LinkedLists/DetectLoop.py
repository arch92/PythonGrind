from Node import Node
from LinkedList import LinkedList

def detect_loop(lst):
    slow = lst.head
    fast = lst.head
    while(slow and fast and fast.next ):
        slow=slow.next
        fast=fast.next.next
        
        if fast==slow:
            return True
    # Replace this placeholder return statement with your code
    return False

lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
lst.print_list()
detect_loop(lst)
lst.print_list()