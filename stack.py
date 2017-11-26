class Stack:
    def __init__(self):
        self.stack = []
        return

    def isempty(self):
        return self.stack == []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        assert len(self.stack) != 0
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)
