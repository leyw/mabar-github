class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Link:
    def __init__(self):
        self.head = None

    def __addHeadIsNone(self, head, new_node):
        if head is None:
            head = new_node
            return
        
    def retNode(self):
        return self.head

    def addStart(self, value):
        head = self.head
        new_node = Node(value)

        self.__addHeadIsNone(head, new_node)
        
        new_node.next = head
        self.head = new_node

    def addEnd(self, value):
        head = self.head
        new_node = Node(value)

        self.__addHeadIsNone(head, new_node)

        while head.next is not None:
            head = head.next

        self.head.next = new_node

    def view(self):
        head = self.head
        
        while head.next is not None:
            print(head.value)
            head = head.next

link = Link()