class Graph:
    def __init__(self):
        # Initializes an empty adjacency list to store vertices and their connections
        self.adj_list = {}

    def get_vertices(self):
        # Returns a list of all vertices currently in the graph
        return list(self.adj_list.keys())

    def get_vertex_count(self):
        # Returns the total number of vertices in the graph
        return len(self.adj_list)

    def has_vertex(self, vertex):
        # Checks if a given vertex exists in the graph
        return vertex in self.adj_list

    def add_vertex(self, vertex):
        # Adds a vertex to the graph only if it doesn't already exist
        if not self.has_vertex(vertex):
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Ensures both vertices exist; if not, add them
        if not self.has_vertex(vertex1):
            self.add_vertex(vertex1)
        if not self.has_vertex(vertex2):
            self.add_vertex(vertex2)

        # Adds vertex2 to vertex1's adjacency list if not already present
        if vertex2 not in self.adj_list[vertex1]:
            self.adj_list[vertex1].append(vertex2)

        # Adds vertex1 to vertex2's adjacency list (undirected graph)
        if vertex1 not in self.adj_list[vertex2]:
            self.adj_list[vertex2].append(vertex1)

    def display(self):
        # Prints the entire adjacency list of the graph
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
#TEST CASES
# Create a new graph
g = Graph()

# Test: Add edge between two new vertices
g.add_edge("A", "B")
g.display()


# Test: Add edge between existing and new vertex
g.add_edge("A", "C")
g.display()

# Test: Add edge between two existing vertices (should not duplicate)
g.add_edge("A", "B")
g.display()


# Test: Add self-loop
g.add_edge("C", "C")
g.display()



