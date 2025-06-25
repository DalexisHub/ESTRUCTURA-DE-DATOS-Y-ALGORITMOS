class Graph:
    def __init__(self):
        """
        #Initializes an empty graph using a dictionary as the adjacency list.
        Each key in the dictionary represents a vertex and maps to a list of adjacent vertices.
        """
        self.adjacency_list = {}

    def get_vertices(self):
        """
        Returns a list of all vertices in the graph.
        """
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        """
        Returns the total number of vertices in the graph.
        """
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        """
        Checks if the specified vertex exists in the graph.
        
        Parameters:
        vertex: The vertex to check for existence in the graph.
        
        Returns:
        True if the vertex exists, False otherwise.
        """
        return vertex in self.adjacency_list

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph if it doesn't already exist.
        
        Parameters:
        vertex: The vertex to be added to the graph.ss
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            
#TEST CASES
        
# Create an instance of the Graph class
g = Graph()

# Test on empty graph
print("Vertices (expected []):", g.get_vertices())
print("Vertex Count (expected 0):", g.get_vertex_count())
print("Has vertex 'A'? (expected False):", g.has_vertex('A'))

# Add some vertices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

# Test after adding vertices
print("Vertices (expected ['A', 'B', 'C']):", g.get_vertices())
print("Vertex Count (expected 3):", g.get_vertex_count())
print("Has vertex 'A'? (expected True):", g.has_vertex('A'))
print("Has vertex 'D'? (expected False):", g.has_vertex('D'))

