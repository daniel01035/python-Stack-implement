class stack:
    def __init__(self):
        self.sta = [0]
        self.top = -1
        self.isEmpty

    def push(self, n):
        self.top += 1
        self.sta.insert(self.top, n)

    def pop(self):
        if self.isEmpty():
            return print("Stack is Empty.")
        else:
            self.top -= 1

    def peek(self):
        return self.sta[self.top]

    def getSize(self):
        return self.top+1

    def check(self):
        if self.isEmpty():
            return print("Stack is Empty.")
        else:
            return self.sta[0 : self.top+1]

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False