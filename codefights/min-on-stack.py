class StackWithMin(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, n):
        self.stack.append(n)
        if len(self.min_stack) == 0 or n < self.min():
            self.min_stack.append(n)

    def pop(self):
        p = self.stack.pop()
        if p == self.min():
            self.min_stack.pop()
        return p

    def min(self):
        m = self.min_stack.pop()
        self.min_stack.append(m)
        return m

def minimumOnStack(operations):
    result = []
    s = StackWithMin()
    for op in operations:
        if op == 'min':
            result.append(s.min())
        elif op == 'pop':
            s.pop()
        else:
            s.push(int(op.split(' ')[1]))
    return result
