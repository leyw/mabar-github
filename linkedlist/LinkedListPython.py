class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Linked:
    def __init__(self):
        self._Head = None


    def addend(self, value):
        
        node = Node(value)

        if self._Head is None:
            self._Head = node
            return
        
        current = self._Head

        while current is not None and current.next is not None:
            current = current.next

        current.next = node

    def adding(self, value):

        node = Node(value)

        if self._Head is None:
            self._Head = node
            return
        
        node.next = self._Head

        self._Head = node

    def addet(self, value, target):

        node = Node(value)

        if self._Head is None:
            self._Head = node
            return
        
        current = self._Head

        while current is not None and current.value is not target:
            current = current.next

        node.next = current.next

        current.next = node

    def delete(self, target):

        prev = None
        current = self._Head

        while current is not None and current.value is not target:
            prev = current
            current = current.next

        if current is None:
            return

        if prev is None:
            self._Head = current.next
        else:
            prev.next = current.next
        
        del current

list = Linked()

list.adding(40)
list.addend(20)
list.adding(30)
list.addet(50, 30)

print(list._Head.value)
print(list._Head.next.value)
print(list._Head.next.next.value)
print(list._Head.next.next.next.value)
