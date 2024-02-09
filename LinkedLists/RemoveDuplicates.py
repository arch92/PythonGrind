from Node import Node
from LinkedList import LinkedList

def remove_duplicates(lst):
    
    # Replace this placeholder return statement with your code
    while lst.head.next is None:
        return lst
    
    outer_node = lst.head
    inner_node = lst.head.next
    prev = outer_node
    while outer_node:
        inner_node=outer_node.next
        while inner_node:
            
            if outer_node.data == inner_node.data:
                prev.next = inner_node.next
                inner_node.next = None
                inner_node = prev.next

            else:
                prev=inner_node
                inner_node = inner_node.next
        outer_node=outer_node.next

    return lst

lst = LinkedList()
lst.insert_at_head(10)
lst.insert_at_head(23)
lst.insert_at_head(25)
lst.insert_at_head(25)
lst.print_list()
print(remove_duplicates(lst))
lst.print_list()