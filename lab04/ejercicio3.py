class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.min_value = value

class LinkedStack:
    def __init__(self):
        self.top_node = None

    def push(self, x):
        new_node = Node(x)
        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next = self.top_node
            new_node.min_value = min(x, self.top_node.min_value)
            self.top_node = new_node

    def pop(self):
        if self.top_node is not None:
            popped_node = self.top_node
            self.top_node = self.top_node.next
            popped_node.next = None
            return popped_node.value
        return None

    def top(self):
        if self.top_node is not None:
            return self.top_node.value
        return None

    def getMin(self):
        if self.top_node is not None:
            return self.top_node.min_value
        return None

    def get_stack(self):
        # Returns the stack as a list of values
        current = self.top_node
        stack_list = []
        while current:
            stack_list.append(current.value)
            current = current.next
        return stack_list

# Example usage
stack = LinkedStack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

# Show results
print("Current stack:", stack.get_stack())
print("Top element:", stack.top())
print("Minimum element:", stack.getMin())

stack.pop()
print("Current stack after pop:", stack.get_stack())
print("Top element after pop:", stack.top())
print("Minimum element after pop:", stack.getMin())

stack.pop()
print("Current stack after another pop:", stack.get_stack())
print("Top element after another pop:", stack.top())
print("Minimum element after another pop:", stack.getMin())
