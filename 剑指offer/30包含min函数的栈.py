class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.temp_stack = []


    def push(self, x: int) -> None:
        if not self.temp_stack:
            self.temp_stack.append(x)
        elif x <= self.temp_stack[-1]:
            self.temp_stack.append(x)
        self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack.pop(-1) == self.temp_stack[-1]:
            self.temp_stack.pop(-1)

    def top(self) -> int:
        return self.min_stack[-1]

    def min(self) -> int:
        return self.temp_stack[-1]