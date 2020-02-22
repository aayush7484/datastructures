from exceptions import Empty
class Arraystack:
    def __init__(self):
        self.data=[]
    def _len(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def push(self,e):
        return self.data.append(e)
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]
s=Arraystack()
s.push(10)
s.push(20)
print("stack:",s.data)
print("length:",len(s.data))
print("stack:",s.is_empty())
print("Popped:",s.pop())
print("stack:",s.data)
print("push:",s.push(30))
print("push:",s.push(40))
print("top:",s.top())
print("stack:",s.data)
print("length:",len(s.data))


