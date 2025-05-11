class Node:
    def __init__(self, value):
        """Inicializa un nodo del árbol binario con un valor y punteros a los hijos izquierdo y derecho."""
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """Inicializa un árbol binario con una raíz nula."""
        self.root = None

    def build_tree_from_list(self, values):
        """Construye un árbol binario a partir de una lista de valores usando BFS."""
        if not values:
            return None

        # Crear la raíz del árbol
        self.root = Node(values[0])
        queue = [self.root]
        index = 1

        # Recorremos la lista para asignar hijos izquierdo y derecho
        while index < len(values):
            current = queue.pop(0)

            # Asignar hijo izquierdo
            if index < len(values) and values[index] is not None:
                current.left = Node(values[index])
                queue.append(current.left)
            index += 1

            # Asignar hijo derecho
            if index < len(values) and values[index] is not None:
                current.right = Node(values[index])
                queue.append(current.right)
            index += 1

def lowest_common_ancestor(root, n1, n2):
    """Encuentra el ancestro común más bajo (LCA) de dos nodos en el árbol binario."""
    # Caso base: si el nodo actual es None, retornar None
    if root is None:
        return None

    # Si el nodo actual coincide con n1 o n2, retornarlo como posible LCA
    if root.value == n1 or root.value == n2:
        return root

    # Recursivamente buscar en los subárboles izquierdo y derecho
    left_lca = lowest_common_ancestor(root.left, n1, n2)
    right_lca = lowest_common_ancestor(root.right, n1, n2)

    # Si ambos subárboles devuelven un nodo, significa que n1 y n2 están en ramas diferentes
    # por lo tanto, el nodo actual es el LCA
    if left_lca and right_lca:
        return root

    # Si solo uno de los subárboles devuelve un nodo, ese es el LCA
    return left_lca if left_lca else right_lca

# Función para ejecutar los casos de prueba
def test_lowest_common_ancestor():
    """Prueba la función lowest_common_ancestor con varios casos de prueba."""
    # Caso de prueba 1
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    print(f"LCA de 4 y 6: {lowest_common_ancestor(tree1.root, 4, 6).value}")  # Esperado: 1

    # Caso de prueba 2
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    print(f"LCA de 2 y 4: {lowest_common_ancestor(tree2.root, 2, 4).value}")  # Esperado: 2

    # Caso de prueba 3
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    print(f"LCA de 2 y 3: {lowest_common_ancestor(tree3.root, 2, 3).value}")  # Esperado: 1

    # Caso de prueba 4
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    print(f"LCA de 1 y 3: {lowest_common_ancestor(tree4.root, 1, 3).value}")  # Esperado: 1

    # Caso de prueba 5: Nodo no presente
    print(f"LCA de 2 y 99: {lowest_common_ancestor(tree4.root, 2, 99)}")  # Esperado: None

# Ejecutar las pruebas
test_lowest_common_ancestor()
