
from Node import Node

class LinkedList:
    
    
    
    def __init__(self):
        self.head = None
    
    def get_head(self):
        return self.head # O(1)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def insert_at_head(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return self.head
    
    def print_list(self): 
        if(self.is_empty()):
          print("List is Empty")
          return False   
        temp = self.head   
        while temp.next is not None:
         print(temp.data , end = " -> ")
         temp = temp.next    
        print(temp.data , "-> None")
        return True

linked_list = LinkedList()

linked_list.insert_at_head(8)
print(linked_list.get_head())
print(linked_list.is_empty())




