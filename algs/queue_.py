class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
        
    def put(self, elem):
        self.queue.insert(0, elem)
    
    def get(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None

'''
n = 0
que = Queue()
while(n != 5):
    n = int(input('Номер действия'))
    if n == 1:
        print(que.size())
    elif n == 2:
        print(que.isEmpty())
    elif n == 3:
        el = int(input('Введите значение'))
        que.put(el)
        print(que.queue)
    elif n == 4:
        print(que.get())
        print(que.queue)
'''
