# Graph Implementation - Challenge 2: Adding Vertices and Basic Structure
# This implementation focuses on dynamic vertex addition with proper validation

# Global list to store test results for tracking
test_results = []

def record_test(test_name, condition):
    """
    Records test results with visual indicators
    Args:
        test_name (str): Name/description of the test
        condition (bool): Whether the test passed or failed
    """
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    """
    Graph data structure implementation using adjacency list representation
    Supports dynamic vertex addition with duplicate prevention
    """
    
    def __init__(self):
        """
        Initialize empty graph with adjacency list structure
        adjacency_list: Dictionary where keys are vertices and values are lists of neighbors
        """
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph with empty adjacency list
        Prevents duplicate vertices by checking if vertex already exists
        
        Args:
            vertex: The vertex to add (can be string, number, or any hashable type)
        
        Returns:
            None
        
        Time Complexity: O(1) - Dictionary lookup and assignment
        Space Complexity: O(1) - Only adds one entry per vertex
        """
        # Check if vertex doesn't already exist to prevent duplicates
        if vertex not in self.adjacency_list:
            # Add vertex with empty list (no connections initially)
            self.adjacency_list[vertex] = []
        
        # If vertex already exists, do nothing (duplicate prevention)
    
    def get_vertices(self):
        """
        Get all vertices in the graph
        
        Returns:
            list: List of all vertices in the graph
        """
        return list(self.adjacency_list.keys())
    
    def get_vertex_count(self):
        """
        Get the total number of vertices in the graph
        
        Returns:
            int: Number of vertices currently in the graph
        """
        return len(self.adjacency_list)
    
    def has_vertex(self, vertex):
        """
        Check if a vertex exists in the graph
        
        Args:
            vertex: The vertex to check for existence
            
        Returns:
            bool: True if vertex exists, False otherwise
        """
        return vertex in self.adjacency_list

def run_tests():
    """
    Comprehensive test suite for vertex addition functionality
    Tests all required scenarios: single addition, multiple additions,
    duplicate prevention, vertex isolation, and size tracking
    """
    # Create new graph instance for testing
    graph = Graph()
    
    # Test 1.2.1: Single vertex addition
    # Verify that adding one vertex works correctly
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))
    
    # Test 1.2.2: Multiple vertex addition
    # Verify that multiple vertices can be added successfully
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)
    
    # Test 1.2.3: Duplicate prevention
    # Verify that adding the same vertex twice doesn't create duplicates
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")  # Adding duplicate vertex
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    
    # Test 1.2.4: Vertex isolation
    # Verify that new vertices have no connections initially
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)
    
    # Test 1.2.5: Graph size tracking
    # Verify that vertex count and vertex list are properly maintained
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

def demonstrate_vertex_addition():
    """
    Additional demonstration of vertex addition functionality
    Shows various use cases and edge cases
    """
    print("🏗️ Graph Vertex Addition Demonstration")
    print("=" * 50)
    
    # Create demonstration graph
    demo_graph = Graph()
    
    # Demonstrate adding different types of vertices
    print("\n📍 Adding different types of vertices:")
    vertices_to_add = ["Lima", "Cusco", 1, 2, "Arequipa"]
    
    for vertex in vertices_to_add:
        demo_graph.add_vertex(vertex)
        print(f"   Added vertex: {vertex} | Total vertices: {demo_graph.get_vertex_count()}")
    
    # Demonstrate duplicate prevention
    print("\n🚫 Testing duplicate prevention:")
    initial_count = demo_graph.get_vertex_count()
    demo_graph.add_vertex("Lima")  # Duplicate
    demo_graph.add_vertex(1)       # Duplicate
    print(f"   Before duplicates: {initial_count}")
    print(f"   After duplicate attempts: {demo_graph.get_vertex_count()}")
    print(f"   Duplicates prevented: {initial_count == demo_graph.get_vertex_count()}")
    
    # Show current graph state
    print(f"\n📊 Current graph vertices: {demo_graph.get_vertices()}")
    print(f"📈 Total vertex count: {demo_graph.get_vertex_count()}")

# 🚀 Run main test suite
print("🧪 Running Test Suite for Challenge 2")
print("=" * 40)
run_tests()

# 📋 Display test results summary
print("\n📋 Test Results Summary:")
print("-" * 25)
for result in test_results:
    print(result)

# 🎯 Calculate success rate
passed_tests = sum(1 for result in test_results if "✅" in result)
total_tests = len(test_results)
success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

print(f"\n🎯 Success Rate: {passed_tests}/{total_tests} ({success_rate:.1f}%)")

# 🔍 Run additional demonstration
print("\n" + "=" * 60)
demonstrate_vertex_addition()