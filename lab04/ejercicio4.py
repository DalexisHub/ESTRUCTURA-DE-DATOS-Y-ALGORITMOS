class TextEditor:
    def __init__(self):
        self.text = []            # To store current text as a list of characters
        self.undo_stack = []      # Stack to store undo operations

    def type(self, char):
        self.text.append(char)
        self.undo_stack.append(('delete', char))  # Save the inverse operation

    def delete(self):
        if self.text:
            char = self.text.pop()
            self.undo_stack.append(('type', char))  # Save the inverse operation

    def undo(self):
        if self.undo_stack:
            operation, char = self.undo_stack.pop()
            if operation == 'delete':
                self.text.pop()
            elif operation == 'type':
                self.text.append(char)

    def get_text(self):
        return ''.join(self.text)

editor = TextEditor()

editor.type('H')
editor.type('i')
editor.type('!')
print(editor.get_text())  # Output: Hi!

editor.delete()
print(editor.get_text())  # Output: Hi

editor.undo()
print(editor.get_text())  # Output: Hi!

editor.undo()
print(editor.get_text())  # Output: Hi
