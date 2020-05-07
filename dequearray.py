from exceptions import Empty
class Arraydeque:
    def __init__(self):
        self.data=[]
        self.front=0
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self.data[self.front]
    def add_first(self,e):
        self.data.insert(self.front,e)
    def add_last(self,e):
        self.data.append(e)
    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        value=self.data.pop(self.front)
        return value
    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        value=self.data.pop()
        return value
q=Arraydeque()
q.add_last(10)
q.add_last(20)
q.add_last(30)
q.add_last(40)
q.add_last(50)
print('Deque',q.data)
print('Delete first',q.delete_first())
print('Deque',q.data)
print('Delete Last:',q.delete_last())
print('Deque',q.data)
q.add_first(50)
print('Deque',q.data)
q.add_last(60)
print('deque:',q.data)
print('Length',len(q))



    