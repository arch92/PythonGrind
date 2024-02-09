from Node import Node
from LinkedList import LinkedList

def reverse(lst):
    curNode = lst.head
    prev = None
    next = None
    while curNode:
        next=curNode.next
        curNode.next=prev
        prev=curNode
        curNode=next
    lst.head = prev
    
    return lst


lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
lst.print_list()
reverse(lst)
lst.print_list()
