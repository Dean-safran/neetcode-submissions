class MinStack:
    """

    make another stack that stores 
    the current smallest at each index

    Don't forget if we pop something from 
    minStack to update the current minimum value

    """

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None :
            self.min = val
        elif val < self.min :
            self.min = val
        self.stack.append(val)
        self.minStack.append(self.min)

    def pop(self) -> None:
        del self.stack[-1]
        if len(self.minStack) == 1 :
            self.min = None
        else : 
            self.min = self.minStack[-2]
        del self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
