# We initialize two different stack. When we push the element we append that in the first stack.
# When we pop the element we transfer all the element from first stack to second stack and popped the last element.
# In case of peek we just return the last element.

# Time Complexity : O(1)
#Space Complexity : O(1)

class MyQueue:

    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        

    def push(self, x: int) -> None:
        self.first_stack.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.second_stack.pop()

        

    def peek(self) -> int:
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1] if self.second_stack else None
        

    def empty(self) -> bool:
        return not self.first_stack and not self.second_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()