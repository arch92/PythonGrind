from os import link
from Node import Node
from LinkedList import LinkedList


def insert_at_tail(lst, value):

    # Write your code here
    newNode = Node(value)
    head = lst.head
    if lst.is_empty():
        lst.head=newNode
        
        return head
    else:
        curNode=lst.head
        while(curNode.next !=None):
            curNode=curNode.next
        curNode.next = newNode
        return head
    
lst = LinkedList()
lst.insert_at_head(4)
print(insert_at_tail(lst,6))
curNode = lst.get_head()
while(curNode != None):
    print(curNode.data)
    curNode=curNode.next
