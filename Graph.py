'''Graph
'''


#Implementation of Graph by Adjacency Matrix

'''
--> Define a class Graph to implement the adjacency matrix representation of a simple and undirected 
    graph.
--> Define an init method to initialise the vertex_count and adj_matrix(list of list) method.
--> Define add_edge method to add an edge in the matrix with the given weight.
--> Define remove_edge method to remove an edge from the graph.
--> Define has_edge method to check weather two given vertex are connected by an edge or not.
--> Define print_adj_matrix method to print adjacency matrix.'''

class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range(vno)] #to have vno list rows with vno number of [0] lists in it
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            raise IndexError("Invalid Vertex")
        
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            raise IndexError("Invalid Vertex")
        
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("has no edge")

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))


g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_matrix()

print("\nCheck edges:")
print("Has edge (0,1):", g.has_edge(0, 1))
print("Has edge (0,4):", g.has_edge(0, 4))

#2. Implementation of Graph using Adjacency List

'''
--> Define a class Graph to implement the representation of graph using adjacency list.
--> Define the init method to initialise the instance object variable vertex_count and dictionary
    adj_list where key is the vertex number and value is the list of adjacent vertices.
--> Define add_edge method to add an edge in the graph with the given vertices and the weights.
--> Define remove_edge method to remove an edge from the graph.
--> Define has_edge method to check weather an edge exists or not for a given pair of vertices.
--> Define print adj_list method to print the adjacency list of the graph.
'''

class Graph_list:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[] for v in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid vertex")

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("Invalid Vertex")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex,weight in self.adj_list[u])
        else:
            print("Invalid Vertex")

    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("V",vertex,":",n)



g2=Graph_list(5)
g2.add_edge(0,1)
g2.add_edge(1,2)
g2.add_edge(1,3)
g2.add_edge(2,4)
g2.add_edge(3,4)
g2.print_adj_list()

print("\nCheck edges:")
print("Has edge (0,1):", g2.has_edge(0, 1))
print("Has edge (0,4):", g2.has_edge(0, 4))