''' 
Question -
Design a stack that supports increment operations on its elements.
Implement the CustomStack class:
CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
'''

'''
Difficulty - Medium
'''


class CustomStack:

    def __init__(self, n: int):
        self.n, self.stack, self.inc = n, [], []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n: self.stack.append(x), self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1: self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k, len(self.inc)) - 1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


'''
Time Complexity - O(1)
'''
