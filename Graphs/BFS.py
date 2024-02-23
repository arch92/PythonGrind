# Input : A directed graph in the form of an adjacency list and an integer indicating the starting vertex number
# Output: A string containing the vertices of the graph listed in the correct order of traversal.



from Graph import Graph
from Queue import MyQueue

def bfs_traversal_helper(g,source,visited):
    queue = MyQueue()
    result = ""
    queue.enqueue(source)
    visited[source] = True
    
    
    while not queue.is_empty():
        current_node = queue.dequeue()
        result += str(current_node)
        
        temp = g.array[current_node].get_head()
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
           
    return result,visited                
            

def bfs_traversal(g,source):
    result = ""
    visited=[]
    
    if g.vertices == 0:
        return result

    for i in range(g.vertices):
        visited.append(False)
    
    result,visited = bfs_traversal_helper(g,source,visited)
    print(result)
    for i in range(g.vertices):
        if not visited[i]:
            result_new,visited = bfs_traversal_helper(g,i,visited)
            result += result_new
    
    
    return result

if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    print(num_of_vertices)
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(g.print_graph())
        print(bfs_traversal(g, 0))

