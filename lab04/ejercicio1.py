class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def reverse_string(input_str):
    # Create a stack
    stack = Stack()

    # Push each character onto the stack
    for char in input_str:
        stack.push(char)

    # Create an empty string for the result
    reversed_str = ""

    # Pop characters from the stack and add them to the result
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Example usage
original = "Data Structures and Algorithms"
reversed_result = reverse_string(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_result}")
