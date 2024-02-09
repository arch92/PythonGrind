# You have to implement the find_mid() function which will take a linked list as an input and return the value of the middle node
from Node import Node
from LinkedList import LinkedList

def find_mid(lst):
    # Replace this placeholder return statement with your code
    curNode = lst.head_node
    length = 0
    while(curNode):
        length+=1
        curNode = curNode.next_element
    print(length)
    if length%2 == 0 :
        mid=length//2
    else:
        mid=(length//2)+1
    print(mid)
    curNode = lst.head_node
    i=1
    while(i<mid):
        i+=1
        curNode = curNode.next_element
        print(i)
    
    return curNode.data

lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
lst.print_list()
print(find_mid(lst))
lst.print_list()