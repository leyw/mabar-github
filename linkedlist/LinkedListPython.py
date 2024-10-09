class Node:

    # Node[value | next]
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Linked:

    # _Node = None
    def __init__(self):
        self._Node = None


    def insert(self, value):
        # Return Explaination
        # case: value = 5
        
        # node = Node[value | next]
        node = Node(value)
        # node = Node[5 | next]

        # This conditional code only executed when
        # the first node is inserted, just imagine if
        # _Node == None
        if self._Node is None:
            
            # _Node = node (node = Node[5 | next])
            self._Node = node
            return self._Node

        # This code executed if there is a first node
        # just imagine if the first node is
        # _Node = node (node = Node[6 | next])
        # node = Node[5 | next]
        # node.next = next
        node.next = self._Node
        # node.next = _Node
        # node = Node[5 | _Node] (_Node = node (node = Node[6 | next]))

        # _Node = node
        self._Node = node

list = Linked()

list.insert(19)
list.insert(20)