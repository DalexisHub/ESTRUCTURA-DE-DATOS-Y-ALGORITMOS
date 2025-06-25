from collections import deque

# List to store test results with visual indicators
test_results = []

def record_test(test_name, condition):
    """Records test outcomes using visual icons (✅ for pass, ❌ for fail)"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        # Graph represented as an adjacency list (dictionary)
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """Adds a vertex to the graph if it does not already exist"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices.
        If the vertices don't exist, they are created.
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add connections if not already present
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)
    
    def find_path(self, start_vertex, end_vertex):
        """
        Finds a path between two vertices using Breadth-First Search (BFS).
        Returns a list representing the path, or an empty list if no connection exists.
        """
        # Special case: path to self
        if start_vertex == end_vertex:
            return [start_vertex]
        
        # Validate that both vertices exist
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []
        
        # BFS queue: holds tuples (current_vertex, path_so_far)
        queue = deque([(start_vertex, [start_vertex])])
        visited = set()  # To prevent revisiting nodes
        visited.add(start_vertex)
        
        while queue:
            current_vertex, path = queue.popleft()
            
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor in visited:
                    continue
                
                new_path = path + [neighbor]  # Extend the current path
                
                if neighbor == end_vertex:
                    return new_path  # Found the path
                
                visited.add(neighbor)
                queue.append((neighbor, new_path))
        
        # If all paths have been explored and end_vertex is not reached
        return []
    
    def is_connected(self, vertex1, vertex2):
        """
        Determines whether there is any path between two vertices.
        Uses `find_path` to check connectivity.
        """
        path = self.find_path(vertex1, vertex2)
        return len(path) > 0

# Test function to validate graph behavior
def run_tests():
    graph = Graph()
    
    # Build a test graph:
    # Lima --- Cusco --- Arequipa
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")  # Trujillo is isolated (no edges)
    
    # 1.4.1 Direct connection between Lima and Cusco
    path = graph.find_path("Lima", "Cusco")
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])
    
    # 1.4.2 Indirect connection: Lima -> Cusco -> Arequipa
    path = graph.find_path("Lima", "Arequipa")
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"
    record_test("1.4.2 Indirect connection path", is_valid_path)
    
    # 1.4.3 No path: Lima and Trujillo are not connected
    path = graph.find_path("Lima", "Trujillo")
    record_test("1.4.3 No path case", path == [])
    
    # 1.4.4 Path to self: should return [Lima]
    path = graph.find_path("Lima", "Lima")
    record_test("1.4.4 Self path", path == ["Lima"])
    
    # 1.4.5 Connectivity check: Lima is connected to Arequipa, not to Trujillo
    connected = graph.is_connected("Lima", "Arequipa")
    not_connected = graph.is_connected("Lima", "Trujillo")
    record_test("1.4.5 Connectivity check", connected and not not_connected)

# 🚀 Run tests
run_tests()

# 📋 Display summary
for r in test_results:
    print(r)
