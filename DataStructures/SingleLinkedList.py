class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        pos = self.head
        while pos:
            print(pos.data)
            pos = pos.next
    #Appends a new Node at the end of the list
    def append(self, data):
        pos = self.head
        if pos:
            while pos.next:
                pos = pos.next
            newnode = Node(data)
            pos.next = newnode
            newnode.next = None
        else:
            newnode = Node(data)
            self.head = newnode
            newnode.next = None

    # Appends a new Node at the beginning of the list
    def prepend(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # Deletes the node with value as 'data'
    def deletewithvalue(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        pos = self.head
        while pos.next:
            if pos.next.data == data:
                pos.next = pos.next.next
                return
            pos = pos.next
    #Fetches the middle value of the SingleLinked List in O(n) time
    def getmiddlenode(self):
        onesteppointer=self.head
        twosteppointer=self.head

        while twosteppointer.next is not None:
            onesteppointer=onesteppointer.next
            twosteppointer=twosteppointer.next.next
        return onesteppointer.data
    def detectloop(self):
        s= set()
        temp=self.head
        while(temp):
            if temp in s:
                return True
            else:
                s.add(temp)
        return False

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(20)
    llist.append(12)
    llist.append(222)
    llist.prepend(100)
    llist.prepend(101)
    #llist.deletewithvalue(100)
    llist.printlist()
    middleValue = llist.getmiddlenode()
    print('Middle element is : ', middleValue)

    llist.head.next.next.next.next = llist.head

    if (llist.detectloop()):
        print("Loop found")
    else:
        print("No Loop ")

