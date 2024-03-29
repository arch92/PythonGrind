# A directed graph in the form of an adjacency list and a starting vertex.
# A string containing the vertices of the graph listed in the correct order of traversal.

from unittest import registerResult
from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input directed graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
# Depth First Traversal of Graph "g" from source vertex



def dfs_traversal_helper(g,source,visited):
    result = ""
    stack = MyStack()
    
    stack.push(source)
    visited[source] = True
    
    while not stack.is_empty():
        current_node = stack.pop()
        
        result += str(current_node)
        temp = g.array[current_node].get_head()
        while temp is not None: 
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data] = True
            temp=temp.next_element
    return result,visited

def dfs_traversal(g, source):
    result = ""
    no_of_vertices = g.vertices
    if no_of_vertices == 0:
        return result
    visited = []
    for i in range(no_of_vertices):
        visited.append(False)
    
    
    result,visited = dfs_traversal_helper(g,source,visited)
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
            
    return result

    return result


if __name__ == "__main__" :
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        print(dfs_traversal(g, 1))
