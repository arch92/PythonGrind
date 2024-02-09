from Node import Node
from LinkedList import LinkedList

def delete(lst, value):
    if lst.head.data == value:
        lst.head = lst.head.next
    prev=lst.head
    curNode = lst.head.next
    while(curNode.next!=None):
        if(curNode.data == value):
            prev.next=curNode.next
            curNode.next = None
            
            return True
        prev= prev.next
        curNode=curNode.next
    # Replace this placeholder return statement with your code
    return False

def length(lst):
    count = 0
    curNode = lst.head
    while(curNode != None):
        curNode = curNode.next
        count+=1
    # Replace this placeholder return statement with your code
    return count

lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
print('count ' + str(length(lst)))
print(delete(lst,25))
