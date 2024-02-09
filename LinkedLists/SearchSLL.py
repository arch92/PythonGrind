from Node import Node
from LinkedList import LinkedList

def search(lst, value):

    # Replace this placeholder return statement with your code
    key = value
    curNode = lst.head
    while(curNode!=None):
        if curNode.data == key:
            return True
        curNode=curNode.next
    return False

lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
print(search(lst,10))