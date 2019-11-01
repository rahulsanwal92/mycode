class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printlist(self):
        pos = self.head
        while pos:
            print(pos.data)
            pos = pos.next

    def append(self, data):
        newNode = Node(data)
        currentLast = self.tail
        currentLast.next = newNode
        newNode.prev = currentLast
        self.tail = newNode

    def preappend(self,data):
        newNode = Node(data)
        currentFirst = self.head
        currentFirst.prev = newNode
        newNode.next = currentFirst
        self.head = newNode