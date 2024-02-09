
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
    
    def remove_duplicates(self):
    
    # Replace this placeholder return statement with your code
        while self.head.next is None:
            return 
    
        outer_node = self.head
        inner_node = self.head.next
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

        return 
    
    def search(self, value):

        # Replace this placeholder return statement with your code
        key = value
        curNode = self.head
        while(curNode!=None):
            if curNode.data == key:
                return True
            curNode=curNode.next
        return False

linked_list = LinkedList()

linked_list.insert_at_head(8)
print(linked_list.get_head())
print(linked_list.is_empty())




