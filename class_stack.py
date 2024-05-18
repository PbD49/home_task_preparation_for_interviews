from typing import List


class Stack:
    def __init__(self):
        self.stack: List[str] = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item: str):
        self.stack.append(item)

    def pop(self) -> str:
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self) -> str:
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self) -> int:
        return len(self.stack)
