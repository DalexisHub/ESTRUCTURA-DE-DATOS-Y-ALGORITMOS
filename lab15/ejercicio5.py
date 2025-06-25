from collections import deque
# Stores results of the test cases using visual symbols for clarity
test_results = []
def record_test(test_name, condition):
    """Records the result of a test with a check (✅) or cross (❌)"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")
class Graph:
    def __init__(self):
        # Graph structure represented as an adjacency list (dictionary of lists)
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """Adds a vertex to the graph if it doesn't already exist"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices.
        Ensures both vertices exist in the graph.
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        # Add connections if not already present (to avoid duplicates)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def get_degree(self, vertex):
        """
        Returns the number of connections (edges) of the given vertex.
        If the vertex is not present, returns 0.
        """
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])
        return 0  # Optionally, could use None for invalid vertex

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        """
        Finds all simple paths (no cycles) between two vertices using DFS.
        Optional: max_length restricts the length of discovered paths.
        """
        def dfs(current, target, path, all_paths):
            # If path exceeds the allowed length, stop exploring this branch
            if max_length is not None and len(path) > max_length:
                return
            if current == target:
                all_paths.append(list(path))  # Add a copy of the valid path
                return
            # Explore neighbors not yet visited in the current path
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, target, path, all_paths)
                    path.pop()  # Backtrack

        # If either vertex doesn't exist, no path can be found
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []

        all_paths = []
        dfs(start_vertex, end_vertex, [start_vertex], all_paths)
        return all_paths

    def get_connected_components(self):
        """
        Identifies and returns all connected components in the graph.
        Each component is a list of connected vertices.
        """
        visited = set()
        components = []

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                queue = deque([vertex])
                visited.add(vertex)

                while queue:
                    current = queue.popleft()
                    component.append(current)

                    for neighbor in self.adjacency_list[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                # Store the entire connected group as one component
                components.append(component)

        return components

# 🧪 Test suite to verify all advanced graph operations
def run_tests():
    graph = Graph()
    
    # Create a graph with two separate components
    # Component 1: Lima - Cusco - Arequipa (fully connected triangle)
    # Component 2: Trujillo - Piura
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # disconnected from Lima cluster

    # 1.5.1: Check degree (number of connections) for Lima (should be 2)
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)
    
    # 1.5.2: Find multiple paths between Lima and Arequipa
    # Should find direct and indirect (through Cusco) paths
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)
    
    # 1.5.3: Get connected components – there should be 2 groups
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)
    
    # 1.5.4: Analyze an empty graph – should return no components
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])
    
    # 1.5.5: Handle query on missing vertex – should return 0 or None
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0 or degree is None)

# 🚀 Execute test cases
run_tests()

# 📋 Print test results
for r in test_results:
    print(r)
