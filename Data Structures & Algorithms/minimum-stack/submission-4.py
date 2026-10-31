class MinStack:

    def __init__(self):
        self.stack = []
        # self.minStack = []

    def push(self, val: int) -> None:
        currentMin = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, currentMin))
        # self.minStack.append(min(val, self.minStack[-1]) if self.minStack else val)

    def pop(self) -> None:
        self.stack.pop()
        # self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]