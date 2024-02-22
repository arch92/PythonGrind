from LinkedList import LinkedList

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.array=[]
        for i in range(vertices):
            self.array.append(LinkedList())
    
    def add_edge(self, source,destination):
        
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination) # directed graph from source->destination
            # self.array[destination].insert_at_head(source) # undirected graph

    def print_graph(self):
        
        for i in range(self.vertices):
            print(" "+ i)
            temp = self.array[i].get_head()
            while temp is not None:
                print("["+temp.data+"]")
                temp = temp.next_element
            print("None")
                
            
    




