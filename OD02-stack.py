class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    # def peek(self):
    #     if not self.is_empty():
    #         return self.stack[-1]
    #     raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0
    #
    # def size(self):
    #     return len(self.stack)


def is_balanced(string):
    stack = Stack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False
    return stack.is_empty()


# Пример использования:
stack = Stack()
print(is_balanced("([{}])"))  # True
print(is_balanced("([)]"))  # False
print(is_balanced("((("))  # False


