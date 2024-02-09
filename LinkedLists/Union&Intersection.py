# Given two lists, A and B, the union is the list that contains elements or objects that belong to either A, B, or to both.
# Given two lists, A and B, the intersection is the largest list which contains all the elements that are common to both the sets.
from Node import Node
from LinkedList import LinkedList


def union(list1, list2):
    # Replace this placeholder return statement with your code
    curNode = list1.head
    while curNode.next:
        curNode = curNode.next
    curNode.next = list2.get_head()
    curNode = list1.head_node
    list1.remove_duplicates()
    return list1

def intersection(list1, list2):
    # Replace this placeholder return statement with your code
    intersection = LinkedList()
    curNode = list1.head
    while curNode is not None:
        key = curNode.data
        if list2.search(key) is not None:
            intersection.insert_at_head(key)
        curNode = curNode.next

    intersection.remove_duplicates()
    return intersection

ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
lst.print_list()

