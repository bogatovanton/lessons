#Класс узлов списка
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Узел со значением {self.val}"

#Класс самого списка    
class LinkedList:
    def __init__(self, value=None):
        self.head = ListNode(value) #Узел в начале списка
        self.tail = self.head #Узел в конце списка
        self.length = 1 #Длина списка
    
    #Добавление узла в конец списка
    def append(self, val):
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    #Добавление узла в начало списка
    def prepend(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def _print(self):
        curNode = self.head
        while(curNode.next != None):
            print(curNode)
            curNode = curNode.next
        print(self.tail)


nodelist = LinkedList(1)
nodelist.append(2)
nodelist.append(3)
nodelist.prepend(4)
nodelist.prepend(5)
nodelist.prepend(6)
nodelist._print()
